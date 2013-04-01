#!/usr/local/bin/python3

import os,random,threading,queue


from game import *
from uirender import *
from eventcatcher import *
from curses import *
from logger import *
import queue


def newgame(std):
	log("Starting new Game...")
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
