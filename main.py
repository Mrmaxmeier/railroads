#!/usr/local/bin/python3

import os,random,threading,queue,time,sys


from game import *
from uirender import *
from eventcatcher import *
from curses import *
from logger import *
from route import *
import queue


def newgame(std):
	log("Starting new Game...")
	stringsfile = StringsFile("data/strings17*7.txt")
	game = Game()
	ui = UI(game,stringsfile,std)
	eventobj = Event(ui,game)
	eventqueue = queue.Queue()
	eventthread = Event_Catcher(eventqueue,ui.cursesinstance)
	eventthread.start()
	#ui.hud(42,1999,[10,10])
	#game.matrix = testmatrix
	ui.refresh()
	r_test = Route("TRAIN_ID",1,1,1)#y,x,right
	r_test.add("forward")
	r_test.add("right")
	r_test.add("forward")
	r_test.add("right")
	r_test.add("forward")
	r_test.add("right")
	r_test.add("forward")
	r_test.add("right")
	r_test.add("forward")
	r_test.add("right")
	r_test.add("forward")
	r_test.add("forward")
	r_test.add("left")
	r_test.add("forward")
	r_test.add("left")
	r_test.add("forward")
	r_test.add("left")
	r_test.add("forward")
	r_test.add("forward")
	r_test.add("right")
	r_test.add("forward")
	r_test.add("right")
	game.routelist.append(r_test)
	timecounter = -5
	while 1:
		timecounter += 1
		try:
			event = eventqueue.get(False,1)
			eventobj.parseevent(event)
			game.tick()
			ui.refresh()
		except queue.Empty:
			if timecounter % 300 == 0:
				game.idleanimate()
				ui.refresh()
			game.idletick()
			ui.idlerefresh()
		time.sleep(0.01)
		#pass
	endwin()


def main(std):
	newgame(std)



if __name__ == "__main__":
	sys.setrecursionlimit(50000)
	wrapper(main)
