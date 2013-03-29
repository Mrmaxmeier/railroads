#!/usr/local/bin/python3
from stringsFile import *
from game import *
from event import *

def combine_strings(strings):
	result = ""
	resultdict = {}
	xlength = len(strings)
	ylength = len(strings[0].split("\n"))
	dictcoords = (-1,-1)
	#print("X,Y",xlength,ylength)
	for string in strings:
		dictcoords = (dictcoords[0]+1,-1)
		#print("Aussen",dictcoords)
		#print("Hudshauidha:",string.split("\n"))
		for line in string.split("\n"):
			dictcoords = (dictcoords[0],dictcoords[1]+1)
			#print("innen",dictcoords)
			resultdict[dictcoords] = (line)
	#print(resultdict)
	for y in range(ylength):
		for x in range(xlength):
			result += resultdict[(x,y)]
		if not y == ylength-1:
			result += "\n"
	return result

















from curses import *
import locale
class UI:
	def __init__(self,gameobj):
		self.gameobj = gameobj
		self.cursesinstance = self.initcurses()
		self.screensize = self.cursesinstance.getmaxyx() #Y,X
		self.tilesize = [3,9]
		self.gameobj.screensize = self.screensize
	def initcurses(self):
		stdscr = initscr()
		#start_color()
		noecho()
		cbreak()
		curs_set(0)
		stdscr.keypad(1)
		locale.setlocale(locale.LC_ALL,"")
		return stdscr
	def cprint(self,Y,X,str,type = None):
		#print "Printing:",str
		if Y >= self.screensize[0] or X >= self.screensize[1]:
			print("FAIL")
		else:
			if type == None:
				self.cursesinstance.addstr(Y,X,str.encode('utf_8'))
			else:
				self.cursesinstance.addstr(Y,X,str.encode('utf_8'),type)
	def hud(self):
		self.cprint(0,self.screensize[1]-12,"Coins: "+str(self.gameobj.money))
		self.cprint(1,self.screensize[1]-12,"Year: "+str(self.gameobj.year))
		self.cprint(self.screensize[0]-1,self.screensize[1]-12,"Menu: "+str("Quit"))
	def printdict(self,dict,Y,X):
		for yi,xi in dict.keys():
			#print "Printing:",dict[(yi,xi)]
			self.cprint(yi+Y,xi+X,dict[(yi,xi)])
	def printmatrix(self,matrix = None,Y = 0,X = 0):
		if matrix == None:
			matrix = self.gameobj.matrix
		coords = [-self.tilesize[0],-self.tilesize[1]]
		for line in matrix:
			coords = [coords[0]+3,-self.tilesize[1]]
			for dict in line:
				#print(yi)
				coords = [coords[0],coords[1]+self.tilesize[1]]
				self.printdict(stringsfile.dict[dict],coords[0],coords[1])
	def railmatrix_to_matrix(railmatrix):
		pass
	def refresh(self):
		self.cursesinstance.clear()
		self.printmatrix()
		ui.printdict(stringsfile.dict["highlighted"],
		self.gameobj.highlighted[0]*3,self.gameobj.highlighted[1]*9)
		self.hud()
		self.cursesinstance.refresh()


class Renderer(UI):
	pass
import time

if __name__ == "__main__":
	testmatrix =   [["down_right","side","side","side","left_down"],
					["station","left_down","down_right","left_down","up"],
					["up","up","station","up","up"],
					["up","up_right","side","left_up","up"],
					["up_right","side","side","side","left_up"]]
	railmatrix = [[True,1,1,1],
				  [1,0,0,1],
				  [],
				  [],
				  []]
	#print()
	#for i in testmatrix:
	#	print(combine_strings(i))
	game = Game()
	ui = UI(game)
	stringsfile = StringsFile("data/strings.txt")
	ui.printmatrix(testmatrix)
	ui.printdict(stringsfile.dict["highlighted"],0*3,0*9)
	ui.printdict(stringsfile.dict["highlighted"],1*3,0*9)
	ui.printdict(stringsfile.dict["highlighted"],0*3,1*9)
	ui.printdict(stringsfile.dict["train_hr"],3*3,2*9)
	#ui.hud(42,1999,[10,10])
	game.matrix = testmatrix
	while 1:
		event = ui.cursesinstance.getch()
		parseevent(event,game)
		ui.refresh()
		#pass
	endwin()