from flask import(
    Flask, render_template, request, redirect, jsonify, url_for,
    flash, make_response, session as login_session)
from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Catagory, CatagoryItem
from oauth2client.client import flow_from_clientsecrets, FlowExchangeError
from werkzeug.contrib.atom import AtomFeed

import datetime
import random
import string
import httplib2
import json
import requests

app = Flask(__name__)

CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Catalog Application"

# Connect to Database and Create Database Session
engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# create anti-forgery state token
@app.route('/login')
def showLogin():
    state = ''.join(random.choice(
        string.ascii_uppercase+string.digits) for x in xrange(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state)


# connect to gplus
@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_credentials = login_session.get('credentials')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_credentials is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps(
            'Current user is already connected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['credentials'] = credentials
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    global username
    username = data['name']
    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: '
    output += '150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;">'
    flash("you are now logged in as %s" % login_session['username'])
    print "done!"
    return output


@app.route('/gdisconnect')
def gdisconnect():
    # only disconnect a connected user
    credentials = login_session.get('credentials')
    if credentials is None:
        message = 'Current user is not connected.'
        response = '<p>'+message+'</p></br> <a href="/">Back to home.</a>'
        return response
    access_token = credentials.access_token
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    if result['status'] == '200':
        # reset the user's session
        del login_session['credentials']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        message = 'Successfully disconnected!'
    response = '<p>'+message+'</p></br> <a href="/">Back to home.</a>'
    return response


# JSON APIs to View Catagory Information
@app.route('/catalog/<string:catagory_name>/items/JSON')
def catagoryJSON(catagory_name):
    items = session.query(CatagoryItem).filter_by(
        catagory_name=catagory_name).all()
    return jsonify(CatagoryItems=[i.serialize for i in items])


# Catatory Item JSON
@app.route('/catalog/<string:catagory_name>/items/<string:item_name>/JSON')
def catagoryItemJSON(catagory_name, item_name):
    item = session.query(CatagoryItem).filter_by(name=item_name).one()
    return jsonify(item=item.serialize)


# Catalog JSON
@app.route('/catalog/JSON')
def catalogJSON():
    catagories = session.query(Catagory).all()
    return jsonify(catagories=[c.serialize for c in catagories])


# Show catalog
@app.route('/')
@app.route('/catalog/')
def showCatalog():
    username = ''
    if 'username' in login_session:
        username = login_session['username']
    catagories = session.query(Catagory).all()
    items = session.query(CatagoryItem).order_by(CatagoryItem.edit_time.desc())
    return render_template(
        'catalog.html', catagories=catagories, items=items, username=username)


# Show item list
@app.route('/catalog/<string:catagory_name>/')
@app.route('/catalog/<string:catagory_name>/items/')
def showItemList(catagory_name):
    username = ''
    if 'username' in login_session:
        username = login_session['username']
    catagories = session.query(Catagory).all()
    items = session.query(CatagoryItem).filter_by(
        catagory_name=catagory_name).all()
    return render_template(
        'catagory.html', catagories=catagories,
        catagory_name=catagory_name, items=items, username=username)


# Show Item
@app.route('/catalog/<string:catagory_name>/items/<string:item_name>/')
def showItem(catagory_name, item_name):
    username = ''
    if 'username' in login_session:
        username = login_session['username']
    item = session.query(CatagoryItem).filter_by(name=item_name).filter_by(
        catagory_name=catagory_name).one()
    return render_template('item.html', item=item, username=username)


# Create new item
@app.route('/catalog/items/new/', methods=['GET', 'POST'])
def newItem():
    if 'username' not in login_session:
        return redirect('/login')
    username = login_session['username']
    if request.method == 'POST':
        if request.form['submit'] == 'submit' and request.form['name']:
            catagory = session.query(Catagory).filter_by(
                name=request.form['catagory_name']).one()
            new_item = CatagoryItem(
                name=request.form['name'],
                description=request.form['description'],
                edit_time=datetime.datetime.now(),
                catagory=catagory)
            session.add(new_item)
            session.commit()
        return redirect(url_for('showCatalog'))
    catagories = session.query(Catagory).all()
    return render_template(
        'new_item.html', catagories=catagories, username=username)


# Edit item
@app.route('/catalog/items/<string:item_name>/edit/', methods=['GET', 'POST'])
def editItem(item_name):
    if 'username' not in login_session:
        return redirect('/login')
    username = login_session['username']
    edit_item = session.query(CatagoryItem).filter_by(name=item_name).one()
    if request.method == 'POST':
        if request.form['submit'] == 'submit':
            if request.form['name']:
                edit_item.name = request.form['name']
            if request.form['description']:
                edit_item.description = request.form['description']
            if request.form['catagory_name']:
                edit_item.catagory_name = request.form['catagory_name']
            edit_item.edit_time = datetime.datetime.now()
            session.add(edit_item)
            session.commit()
        return redirect(url_for('showCatalog'))
    catagories = session.query(Catagory).all()
    return render_template(
        'edit_item.html', catagories=catagories,
        item=edit_item, username=username)


# Delete item
@app.route(
    '/catalog/items/<string:item_name>/delete/', methods=['GET', 'POST'])
def deleteItem(item_name):
    if 'username' not in login_session:
        return redirect('/login')
    username = login_session['username']
    delete_item = session.query(CatagoryItem).filter_by(name=item_name).one()
    if request.method == 'POST':
        if request.form['submit'] == 'delete':
            session.delete(delete_item)
            session.commit()
        return redirect(url_for('showCatalog'))
    return render_template(
        'delete_item.html', item=delete_item, username=username)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.run(host='0.0.0.0', port=5000, debug=True)
