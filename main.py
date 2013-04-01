#!/usr/local/bin/python3

import os,random,threading,queue


from game import *
from uirender import *
from eventcatcher import *
from curses import *
import queue


def newgame(std):
	testmatrix =   [["right_down","left_right","left_right","left_right","left_down"],
			["station","left_down","right_down","left_down","up_down"],
			["up_down","up_down","station","up_down","up_down"],
			["up_down","right_up","left_right","left_up","up_down"],
			["right_up","left_right","left_right","left_right","left_up"],
			["left_right","left_right","left_right","left_right","left_right","left_right","left_right"]]
	stringsfile = StringsFile("data/strings.txt")
	game = Game()
	ui = UI(game,stringsfile,std)
	eventobj = Event(ui,game)
	eventqueue = queue.Queue()
	eventthread = Event_Catcher(eventqueue,ui.cursesinstance)
	eventthread.start()
	#ui.hud(42,1999,[10,10])
	#game.matrix = testmatrix
	ui.refresh()
	while 1:
		try:
			event = eventqueue.get(False,1)
			eventobj.parseevent(event)
			game.tick()
			ui.refresh()
		except queue.Empty:
			game.idletick()
			ui.idlerefresh()
		#pass
	endwin()


def main(std):
	newgame(std)



if __name__ == "__main__":
	wrapper(main)
