import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Catagory, CatagoryItem

engine = create_engine('sqlite:///catalog.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

action = Catagory(name="Action")
session.add(action)
session.commit()

shooter = Catagory(name="Shooter")
session.add(shooter)
session.commit()

action_adventure = Catagory(name="Action-adventure")
session.add(action_adventure)
session.commit()

adventure = Catagory(name="Adventure")
session.add(adventure)
session.commit()

role_playing = Catagory(name="Role-playing")
session.add(role_playing)
session.commit()

simulation = Catagory(name="Simulation")
session.add(simulation)
session.commit()

strategy = Catagory(name="Strategy")
session.add(strategy)
session.commit()

sports = Catagory(name="Sports")
session.add(sports)
session.commit()

other = Catagory(name="Other")
session.add(other)
session.commit()

ball = CatagoryItem(name="Ball and paddle", description="The predecessor of all console game genres, a ball-and-paddle game was the first game implemented on a home console (Pong). Later renditions have included Breakout, which was a driving influence behind the Apple II computer, and Arkanoid, an arcade staple for many years. A version of Breakout called Block Buster was also packaged with the first handheld console with swappable cartridges, the Microvision.", 
	edit_time=datetime.datetime.now(), catagory=action)
session.add(ball)
session.commit()

tradi_fight = CatagoryItem(name="Traditional Fighting game", description="Fighting games emphasize one-on-one combat between two characters, one of which may be computer controlled.[6][7] These games are usually played by linking together long chains of button presses on the controller to use physical attacks to fight. Many of the movements employed by the characters are usually dramatic and occasionally physically impossible. Combat is always one-on-one.", 
	edit_time=datetime.datetime.now(), catagory=action)
session.add(tradi_fight)
session.commit()

ring_fight = CatagoryItem(name="Ring Fighting game", description="Fighting games where you can move your character freely through a fight ring, some of these games even allow movements of jumping like Ehrgeiz and Power Stone.",
	edit_time=datetime.datetime.now(), catagory=action)
session.add(ring_fight)
session.commit()

moba = CatagoryItem(name="MOBA", description="Multiplayer online battle arena (MOBA), also known as action real-time strategy (ARTS), is a subgenre of the real-time strategy (RTS) genre of video games, in which often two teams of players compete with each other in discrete games, with each player controlling a single character through an RTS-style interface.", 
	edit_time=datetime.datetime.now(), catagory=action)
session.add(moba)
session.commit()

maze_game = CatagoryItem(name="Maze game", description="Maze games have a playing field which is entirely a maze, which players must navigate. Quick thinking and fast reaction times are encouraged by the use of a timer, monsters obstructing the player's way, or multiple players racing to the finish.", 
	edit_time=datetime.datetime.now(), catagory=action)
session.add(maze_game)
session.commit()

pinball = CatagoryItem(name="Pinball game", description="Pinball games are designed to replicate the look and feel of a real-life pinball table in virtual reality.",
	edit_time=datetime.datetime.now(), catagory=action)
session.add(pinball)
session.commit()

first_shooter = CatagoryItem(name="First-person shooter", description="First-person shooter video games, commonly known as FPSs, emphasize shooting and combat from the perspective of the character controlled by the player. This perspective is meant to give the player the feeling of \"being there\", and allows the player to focus on aiming.", 
	edit_time=datetime.datetime.now(), catagory=shooter)
session.add(first_shooter)
session.commit()

light_gun = CatagoryItem(name="Light gun shooter", description="Light gun shooters are a genre of shooter genre designed for use with a pointing device for computers and a control device for arcade and home consoles.",
	edit_time=datetime.datetime.now(), catagory=shooter)
session.add(light_gun)
session.commit()

shoot_em = CatagoryItem(name="Shoot'em up", description="A shoot 'em up, or arcade shooter, is a genre of shooter game in which the player controls a character or vehicle (most often a spacecraft) and shoots large numbers of enemies, while dodging incoming projectiles.", 
	edit_time=datetime.datetime.now(), catagory=shooter)
session.add(shoot_em)
session.commit()

stealth = CatagoryItem(name="Stealth game", description="Stealth games are a somewhat recent subgenre, sometimes referred to as \"sneakers\" or \"creepers\" to contrast with the action-oriented \"shooter\" subgenre.", 
	edit_time=datetime.datetime.now(), catagory=action_adventure)
session.add(stealth)
session.commit()

survival = CatagoryItem(name="Survival horror", description='Survival horror games focus on fear and attempt to scare the player via traditional horror fiction elements such as atmospherics, death, the undead, blood and gore.', 
	edit_time=datetime.datetime.now(), catagory=action_adventure)
session.add(survival)
session.commit()

real_3d = CatagoryItem(name="Real-time 3D adventure", description='Around this time, real-time 3D adventure games appeared. These included Nightfall in 1998, realMyst in 2000, and Uru: Ages Beyond Myst in 2003.', 
	edit_time=datetime.datetime.now(), catagory=adventure)
session.add(real_3d)
session.commit()

text_adventure = CatagoryItem(name="Text adventure", description='The earliest adventure games were text adventures, also known as interactive fiction. Games such as the popular Zork series of the late 1970s and early 1980s allowed the player to use a keyboard to enter commands such as "get rope" or "go west" while the computer describes what is happening. A great deal of programming went into parsing the player\'s text input.', 
	edit_time=datetime.datetime.now(), catagory=adventure)
session.add(text_adventure)
session.commit()

role_choices = CatagoryItem(name="Role-playing Choices", description='Some RPGs give the player several choices in how their story will unfold. Typically the player can have an effect on whether the enemies in the game will be taken out lethally or non-lethally.', 
	edit_time=datetime.datetime.now(), catagory=role_playing)
session.add(role_choices)
session.commit()

cms = CatagoryItem(name="Construction and management simulation", description='Construction and management simulations (or CMSs) are a type of simulation game which task players to build, expand or manage fictional communities or projects with limited resources.', 
	edit_time=datetime.datetime.now(), catagory=simulation)
session.add(cms)
session.commit()

life_simu = CatagoryItem(name="Life simulation", description='Life simulation games (or artificial life games) involve living or controlling one or more artificial lives. A life simulation game can revolve around individuals and relationships, or it could be a simulation of an ecosystem.', 
	edit_time=datetime.datetime.now(), catagory=simulation)
session.add(life_simu)
session.commit()

fourx = CatagoryItem(name="4X", description='4X refers to a genre of strategy video game with four primary goals: eXplore, eXpand, eXploit and eXterminate. A 4X game can be turn-based or real-time.', 
	edit_time=datetime.datetime.now(), catagory=strategy)
session.add(fourx)
session.commit()

tower_defense = CatagoryItem(name="Tower defense", description='Tower defense games have a very simple layout. Usually, computer-controlled monsters called creeps move along a set path, and the player must place, or "build" towers along this path to kill the creeps. In some games, towers are placed along a set path for creeps, while in others towers can interrupt creep movement and change their path.', 
	edit_time=datetime.datetime.now(), catagory=strategy)
session.add(tower_defense)
session.commit()

racing = CatagoryItem(name="Racing", description='One competes against time or opponent using some means of transportation. Most popular subgenre is racing simulators.', 
	edit_time=datetime.datetime.now(), catagory=strategy)
session.add(racing)
session.commit()

sports_game = CatagoryItem(name="Sports game", description='Sports games emulate the playing of traditional physical sports. Some emphasize actually playing the sport, while others emphasize the strategy behind the sport (such as Championship Manager). Others satirize the sport for comic effect (such as Arch Rivals). ', 
	edit_time=datetime.datetime.now(), catagory=strategy)
session.add(sports_game)
session.commit()

casual_game = CatagoryItem(name="Casual game", description='Casual games are the games that, regardless of specific gameplay features, are targeted at audiences (casual gamers) who do not wish to dedicate much time and effort to playing video games (unlike hardcore gamers who do).', 
	edit_time=datetime.datetime.now(), catagory=other)
session.add(casual_game)
session.commit()

music_game = CatagoryItem(name="Music game", description='Music games most commonly challenge the player to follow sequences of movement or develop specific rhythms. Some games require the player to input rhythms by stepping with their feet on a dance pad, or using a device similar to a specific musical instrument, like a replica drum set. These games have changed the way players\' interact with their consoles by making the gaming experience more active and sociable, and paving the way for exergaming.', 
	edit_time=datetime.datetime.now(), catagory=other)
session.add(music_game)
session.commit()

party_game = CatagoryItem(name="Party game", description='Party games are video games developed specifically for multiplayer games between many players. Normally, party games have a variety of mini-games that range between collecting more of a certain item than other players or having the fastest time at something.', 
	edit_time=datetime.datetime.now(), catagory=other)
session.add(party_game)
session.commit()

logic_game = CatagoryItem(name="Logic game", description='logic games require the player to solve logic puzzles or navigate complex locations such as mazes. They are well suited to casual play, and tile-matching puzzle games are among the most popular casual games.', 
	edit_time=datetime.datetime.now(), catagory=other)
session.add(logic_game)
session.commit()

print "Added catatory items!"