## Catalog App - FSND P3
### Poject Description:
Web application that provides a list of items within a variety of catagories as well as provide a user registration and authentication sytem. Registed user will have the ability to post, edit, and delete their own items.

### Function Details
- API Endpoints: JSON
- CRUD: Read, Create(create new item), Update(edit item), Delete(delete item)

### What's included
catalog/   
|--- client_secrets.json          
|--- database_setup.json           
|--- demo_items.json           
|--- project.py                
|--- static/              
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|--- bg.jpg            
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|--- styles.css               
|--- templates/             
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|--- catagory.html          
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|--- catalog.html         
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|--- delete_item.html          
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|--- edit_item.html          
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|--- header.html            
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|--- item.html             
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|--- login.html           
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|--- main.html              
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|--- new_item.html               

### Quick start
1. install vagrant and VM in your machine, intallation detail:
    https://www.udacity.com/wiki/ud088/vagrant
2. download and put folder catalog within '~/fullstack/vagrant' which is the shared folder between VM and local file system

### Running locally
1. locate your terminal to directory '~/fullstack/vagrant'
2. run command 'vagrant up' in terminal to start VM
3. run command 'vagrant ssh' in terminal to login
4. setup and run application within folder '/vagrant/catalog'
5. set up database: python database_setup.py
6. add data to database: python demo_items.py
7. access and test application by visiting 'http://localhost:5000' locally
8. run 'exit' to logout
9. run 'vagrant halt' to shut down VM

### Further Improvements
1. additional API endpoints: RSS, Atom, XML
2. add item images and image operations

### Result
All tests passed!

### Creator
WEN GUO
