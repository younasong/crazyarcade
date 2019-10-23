

#### 15-112 Term Project ####
     Youna Song (younas)

My term project is a version of NEXON Korea's bomberman-style online multiplayer game - Crazy Arcade. It utilizes Python3, Pygame, Pymongo (MongoDB). 

## Instructions ##

This program runs on Python 3, which can be easily downloaded from the following link: 
	https://www.python.org/downloads/
Installation of Pygame, Pymongo, and MongoDB is also necessary in order to run this program. 

-- Installing pip -- 
The best way to install the following libraries is with pip
The process is easily explained in the following link: 
	https://pip.pypa.io/en/stable/installing/

-- Installing Pygame -- 
Tutorial: https://www.pygame.org/wiki/GettingStarted

After pip has been installed, the following commands can be run one at a time in the command line to install and test Pygame: 

	MacOS-
	python3 -m pip install pygame --user
	python3 -m pygame.examples.aliens

	Windows-
	py -m pip install pygame --user
	py -m pygame.examples.aliens

-- Installing MongoDB -- 

Download MongoDB from the following link: 
	https://www.mongodb.com/download-center#community

Then, follow the respective tutorials: 
Tutorial for macOS: https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/
Tutorial for Windows: https://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows/

-- Installing Pymongo -- 
Tutorial: https://api.mongodb.com/python/current/installation.html

Pymongo can also be installed with pip by running the following command: 

	$ python -m pip install pymongo

## Executing the Program ## 

To start, a MongoDB instance must be running on the default host and port. It can be started with the following command: 
	$ mongod
	(if this does not work, try the following command: brew services start mongodb )

To run the program, run the main file "termproject.py" 

## Game Play ##

Instructions
One Player - Kill all the monsters!
Two Player - Fight off each other!

 ONE PLAYER 
 - Arrow keys to move 
 - Space Bar in order to drop balloons 
 - Left Shift to use items 

 TWO PLAYER 
 - Arrow Keys and WASD to move 
 - Left Shift and Right Shift to drop balloons
 - Left control and space bar to use items 

* Line 56 (“collection.remove({})) can be run in order to clear all user accounts 


