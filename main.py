#!/usr/local/bin/python3

import os,random


from game import *
from uirender import *


def newgame():
	testmatrix =   [["down_right","left_right","left_right","left_right","left_down"],
					["station","left_down","down_right","left_down","up_down"],
					["up_down","up_down","station","up_down","up_down"],
					["up_down","up_right","side","left_up","up_down"],
					["up_right","left_right","left_right","left_right","left_up"],
					["left_right","left_right","left_right","left_right","left_right","left_right","left_right"]]
	stringsfile = StringsFile("data/strings.txt")
	game = Game()
	ui = UI(game,stringsfile)
	eventobj = Event(ui,game)
	#ui.hud(42,1999,[10,10])
	game.matrix = testmatrix
	ui.refresh()
	while 1:
		event = ui.cursesinstance.getch()
		eventobj.parseevent(event)
		game.tick()
		ui.refresh()
		#pass
	endwin()


def main():
	newgame()



if __name__ == "__main__":
	main()
