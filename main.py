#!/usr/local/bin/python3

import os,random


from game import *

import uirender as renderengine

#import guirender as renderengine





def main():
	game = Game()
	running = True
	print(game.objects)
	game.tick_move()
	game.addobj("train",(1,2),("load",9))
	print(game.objects)
	game.tick_move()
	print(game.objects)

if __name__ == "__main__":
	main()