import cmd
import textwrap
import sys
import os
import time
import random

import self as self

screen_width = 100

#### Player setup

class digimon:
    def __init__(myself):
        myself.name = ''
        myself.level = ''
        myself.type = ''
        myself.attribute = ''
        myself.evolution = ''
myDigimon = digimon()

class player:
    def __init__(self):
        self.name = ''
        self.hp = 0
        self.xp = 0
        self.DigiCoin = 0
        self.crest = ''
        self.location ='B2'
        self.game_over = False
        self.digimon = ''

myPlayer = player()

##### Title Screen

def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        setup_game()
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ('quit'):
        sys.exit()
    while option.lower() not in ['play', 'help','quit']:
        print('Please enter a valid command')
        option = input("> ")
        if option.lower() == ("play"):
            setup_game()
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ('quit'):
            sys.exit()


def title_screen():
    print('###############################')
    print('Welcome to the Digital World! #')
    print('###############################')
    print('             -Play-            ')
    print('             -Help-            ')
    print('             -Quit-            ')
    title_screen_selections()


def help_menu():
    print('###############################')
    print('Welcome to the Digital World! #')
    print('###############################')
    print('-Use up, down ,left, right, to move')
    print('-Type your commands to do then')
    print('-Use look to inspect something')
    print('-Good luck and have fun!')









####### Map ##########

#a1 ,a2 .... # PLAYER STARTS AT B2
#_____________
#|__|__|__|__|  a4
#|__|__|__|__|  b4
#|__|__|__|__|
#|__|__|__|__|
ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examination'
SOLVED = False
UP = 'up' , 'u'
DOWN = 'down' , 'd'
NORTH ='north' ,'n'
WEST = 'west' , 'w'
EAST = 'east' , 'e'
SOUTH = 'south' ,'s'


solved_places = {'A1':False,'A2':False,'A3':False,'A4':False,
                'B1':False,'B2':False,'B3':False,'B4':False,
                'C1':False,'C2':False,'C3':False,'C4':False,
                'D1':False,'D2':False,'D3':False,'D4':False,
                 }
zonemap = {


    'A1': {
            ZONENAME: "Tropical Jungle" ,
            DESCRIPTION : 'description' ,
            EXAMINATION : 'examination',
            SOLVED : False ,
            DOWN : 'B1',
            NORTH :' ',
            UP : '' ,
            WEST : '',
            EAST : 'A2',
            SOUTH : 'B1',
            },
    'A2': {
            ZONENAME: "Ancient Dino Region" ,
            DESCRIPTION : 'description' ,
            EXAMINATION : 'examination',
            SOLVED : False ,
            DOWN : ' ',
            NORTH :' ',
            UP : '' ,
            WEST : 'A1',
            EAST : 'A3',
            SOUTH : 'B2',
            },
    'A3': {
            ZONENAME: "Unwavering Forest" ,
            DESCRIPTION : 'description' ,
            EXAMINATION : 'examination',
            SOLVED : False ,
            DOWN : ' ',
            NORTH :' ',
            UP : '' ,
            WEST : 'A2',
            EAST : 'A4',
            SOUTH : 'B3',
            },
    'A4': {
            ZONENAME: "Village of Beginnings" ,
            DESCRIPTION : 'description' ,
            EXAMINATION : 'examination',
            SOLVED : False ,
            DOWN : ' ',
            NORTH :' ',
            UP : '' ,
            WEST : 'A3',
            EAST : '',
            SOUTH : 'B4',
            },
    'B1': {
            ZONENAME: "Dragon Eye Lake" ,
            DESCRIPTION : 'description' ,
            EXAMINATION : 'examination',
            SOLVED : False ,
            DOWN : '',
            NORTH :'A1',
            UP : '' ,
            WEST : '',
            EAST : 'B2',
            SOUTH : 'C1',
            },
    'B2': {
            ZONENAME: "Mount Panorama" ,
            DESCRIPTION : 'description' ,
            EXAMINATION : 'examination',
            SOLVED : False ,
            DOWN : '',
            NORTH :'A2',
            UP : '' ,
            WEST : 'B1',
            EAST : 'B3',
            SOUTH : 'C2',
            },
    'B3': {
            ZONENAME: "Gear Savannah" ,
            DESCRIPTION : 'description' ,
            EXAMINATION : 'examination',
            SOLVED : False ,
            DOWN : ' ',
            NORTH :'A3',
            UP : '' ,
            WEST : 'B2',
            EAST : 'B4',
            SOUTH : 'C3',
            },
    'B4': {
            ZONENAME: "Pyocomon Village" ,
            DESCRIPTION : 'description' ,
            EXAMINATION : 'examination',
            SOLVED : False ,
            DOWN : '',
            NORTH :'A4',
            UP : '' ,
            WEST : 'B3',
            EAST : '',
            SOUTH : 'C4',
            },
    'C1': {
            ZONENAME: "Factorial Tower" ,
            DESCRIPTION : 'description' ,
            EXAMINATION : 'examination',
            SOLVED : False ,
            DOWN : '',
            NORTH :'B1',
            UP : '' ,
            WEST : '',
            EAST : 'C2',
            SOUTH : 'D1',
            },
    'C2': {
            ZONENAME: "Sewers" ,
            DESCRIPTION : 'description' ,
            EXAMINATION : 'examination',
            SOLVED : False ,
            DOWN : '',
            NORTH :'B2',
            UP : '' ,
            WEST : 'C1',
            EAST : 'C3',
            SOUTH : 'D2',
            },
    'C3': {
            ZONENAME: "Misty Trees" ,
            DESCRIPTION : 'description' ,
            EXAMINATION : 'examination',
            SOLVED : False ,
            DOWN : '',
            NORTH :'B3',
            UP : '' ,
            WEST : 'C2',
            EAST : 'C4',
            SOUTH : 'D3',
            },
    'C4': {
            ZONENAME: "Toy Town" ,
            DESCRIPTION : 'description' ,
            EXAMINATION : 'examination',
            SOLVED : False ,
            DOWN : '',
            NORTH :'B4',
            UP : '' ,
            WEST : 'A1',
            EAST : 'A3',
            SOUTH : 'B2',
            },
    'D1': {
            ZONENAME: "Freezeland",
            DESCRIPTION: 'description',
            EXAMINATION: 'examination',
            SOLVED: False,
            DOWN: '',
            NORTH: 'C1',
            UP: '',
            WEST: '',
            EAST: 'D2',
            SOUTH: '',
            },
    'D2': {
            ZONENAME: "Great Canyon",
            DESCRIPTION: 'description',
            EXAMINATION: 'examination',
            SOLVED: False,
            DOWN: '',
            NORTH: 'C2',
            UP: '',
            WEST: 'D1',
            EAST: 'D3',
            SOUTH: '',
            },
    'D3': {
            ZONENAME: "Overdell Cementary",
            DESCRIPTION: 'description',
            EXAMINATION: 'examination',
            SOLVED: False,
            DOWN: '',
            NORTH: 'C3',
            UP: '',
            WEST: 'C2',
            EAST: 'C4',
            SOUTH: '',
            },
    'D4': {
            ZONENAME: "Infinity Mountain",
            DESCRIPTION: 'description',
            EXAMINATION: 'examination',
            SOLVED: False,
            DOWN: ' ',
            NORTH: 'C4',
            UP: '',
            WEST: 'C3',
            EAST: '',
            SOUTH: '',
            },


}

### GAME INTERACTIVITY ###
def print_location():
    print('\n'+ ('#' + (4 + len(myPlayer.location))))
    print('# ' + myPlayer.location.upper() + ' #')
    print('# ' + zonemap[myPlayer.location][DESCRIPTION] + ' #')
    print('\n' + ('#' + (4 + len(myPlayer.location))))

def prompt():
    print('\n' + "----------------------------")
    print("< What would you like to do?")
    action = input("> ")
    acceptable_actions = ["move", " camp", "explore", "hunt", "training"]
    while action.lower() not in acceptable_actions:
        print("You cant do that.\n")
        action = input("> ")
    if action.lower() == 'quit':
        sys,exit()
    elif action.lower() in ["move", " travel", "explore", "go", "walk"]:
        player_move(action.lower())


    elif action.lower() in ['exmine', 'inspect', 'interact', 'look']:
        player_examine(action.lower())

def player_move(myAction):
    ask = "Where would you like to move to?\n"
    dest = input(ask)
    if dest in  ['up', 'u']:
        destination = zonemap[myPlayer.location][UP]
        movement_handler(destination)
    elif dest  in ['down' , 'd']:
        destination = zonemap[myPlayer.location][DOWN]
        movement_handler(destination)
    elif dest  in ['north', 'n']:
        destination = zonemap[myPlayer.location][NORTH]
        movement_handler(destination)
    elif dest  in ['south', 's']:
        destination = zonemap[myPlayer.location][SOUTH]
        movement_handler(destination)
    elif dest  in ['west' , 'w']:
        destination = zonemap[myPlayer.location][WEST]
        movement_handler(destination)
    elif dest  in ['east' , 'e']:
        destination = zonemap[myPlayer.location][EAST]
        movement_handler(destination)

def player_examine(action):
    if zonemap[myPlayer.location][SOLVED] == True:
        print("You have already exhausted this zone")
    else:
        print("You can triggre puzle")
def  movement_handler(destination):
    print("\n" + "You have move to the " + destination + ".")
    myPlayer.location = destination
    print_location()
### GAME FUNCTIONALITY ###
def start_game():
    return

def main_game_loop():
    while myPlayer.game_over == False:
        prompt()











def setup_game():

    question1= 'Hello Digi Destiny Child,what is your name?\n'
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input('> ')
    myPlayer.name = player_name

    question2 = 'Good. Choose your heart?\n'
    question2added = "You can choose :\nCourage, Friendship, Love, Knowledge, Purity, Sincerity, Hope, ight, Kidness, Miracles, Destiny"
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in question2added:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    player_crest = input('> ')
    valid_crests = ['courage', 'friendship', 'love', 'knowledge',
                    'purity', 'sincerity', 'hope',
                    'light', 'kidness', 'miracles', 'destiny']
    if player_crest.lower() in valid_crests:
        myPlayer.crest = player_crest
        print("You are now chose " + player_crest + " path\n")
    else :
        while player_crest.lower() not in valid_crests:
            player_crest = input('> ')
            if player_crest.lower() in valid_crests:
                myPlayer.crest = player_crest
                print("You are now chose " + player_crest + " path\n")



        if myPlayer.crest == "courage":
            self.hp = 100
            self.xp = 200
            self.digimon = 'Agumon'
            self.DigiCoin = 100
        if myPlayer.crest == "friendship":
            self.hp = 200
            self.xp = 500
            self.digimon = 'Gabumon'

            self.DigiCoin = 100
        if myPlayer.crest == "love":
            self.hp = 100
            self.xp = 200
            self.digimon = 'Piyomon'
            self.DigiCoin = 100
        if myPlayer.crest == "knowledge":
            self.hp = 100
            self.xp = 700
            self.digimon = 'Tentomon'
            self.DigiCoin = 100
        if myPlayer.crest == "purity":
            self.hp = 100
            self.xp = 200
            self.digimon = 'Palmon'
            self.DigiCoin = 100
        if myPlayer.crest == "sincerity":
            self.hp = 100
            self.xp = 200
            self.digimon = 'Gomamon'
            self.DigiCoin = 100
        if myPlayer.crest == "hope":
            self.hp = 100
            self.xp = 200
            self.digimon = 'Patamon'
            self.DigiCoin = 100
        if myPlayer.crest == "light":
            self.hp = 100
            self.xp = 200
            self.digimon = 'Tailmon'
            self.DigiCoin = 100
        if myPlayer.crest == "kidness":
            self.hp = 100
            self.xp = 200
            self.digimon = 'V-mon'
            self.DigiCoin = 100
        if myPlayer.crest == "miracles":
            self.hp = 100
            self.xp = 200
            self.DigiCoin = 100
        if myPlayer.crest == "destiny" :
            self.hp = 100
            self.xp = 200
            self.DigiCoin = 100



    question3 = 'Welcome, ' + player_name + ' with crest of ' + player_crest + '\n'
    for character in question3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input('> ')
    myPlayer.name = player_name

    speech1 = 'Welcome to this big and beautifull world of numbers\n'
    speech2 = 'You been choosen to save digital world from Darkness\n'
    speech3 = 'Just make sure you dont get too lost\n'
    speech4 = 'Hehehehe...\n'
    for character in speech1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in speech2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in speech3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)
    for character in speech4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.2)

    print('############################')
    print('# Lets start now #')
    print('############################')
    main_game_loop()
title_screen()
