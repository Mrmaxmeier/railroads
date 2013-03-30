#!/usr/local/bin/python3

import os,random


from game import *
from uirender import *


def newgame():
	testmatrix =   [["down_right","side","side","side","left_down"],
					["station","left_down","down_right","left_down","up"],
					["up","up","station","up","up"],
					["up","up_right","side","left_up","up"],
					["up_right","side","side","side","left_up"],
					["side"]]
	stringsfile = StringsFile("data/strings.txt")
	game = Game()
	ui = UI(game,stringsfile)
	eventobj = Event(ui,game)
	ui.printdict(stringsfile.dict["highlighted"],0*3,0*9)
	#ui.hud(42,1999,[10,10])
	game.matrix = testmatrix
	while 1:
		event = ui.cursesinstance.getch()
		eventobj.parseevent(event)
		ui.refresh()
		#pass
	endwin()


def main():
	newgame()



if __name__ == "__main__":
	main()