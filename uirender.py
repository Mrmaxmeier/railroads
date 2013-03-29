#!/usr/local/bin/python3
from stringsFile import *



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
		self.screensize = [100,100] #X,Y
		self.tilesize = [3,9]
	def initcurses(self):
		stdscr = initscr()
		#start_color()
		noecho()
		cbreak()
		stdscr.keypad(1)
		locale.setlocale(locale.LC_ALL,"")
		return stdscr
	def cprint(self,Y,X,str,type = None):
		#print "Printing:",str
		if type == None:
			self.cursesinstance.addstr(Y,X,str.encode('utf_8'))
		else:
			self.cursesinstance.addstr(Y,X,str.encode('utf_8'),type)
		self.cursesinstance.refresh()
	def hud(self,coins,year,size):
		self.cprint(0,self.screensize[1]-5,"Coins: "+str(self.gameobj.money))
	def printdict(self,dict,Y,X):
		for yi,xi in dict.keys():
			#print "Printing:",dict[(yi,xi)]
			self.cprint(yi+Y,xi+X,dict[(yi,xi)])
	def printmatrix(self,matrix,Y = 0,X = 0):
		coords = [-self.tilesize[0],-self.tilesize[1]]
		for line in matrix:
			coords = [coords[0]+3,-self.tilesize[1]]
			for dict in line:
				#print(yi)
				coords = [coords[0],coords[1]+self.tilesize[1]]
				self.printdict(stringsfile.dict[dict],coords[0],coords[1])






class Renderer(UI):
	pass
import time

if __name__ == "__main__":
	testmatrix =   [["down_right","side","side","side","left_down"],
					["station","left_down","down_right","left_down","up"],
					["up","up","station","up","up"],
					["up","up_right","train","left_up","up"],
					["up_right","side","side","side","left_up"]]
	#print()
	#for i in testmatrix:
	#	print(combine_strings(i))
	ui = UI("GAIL")
	stringsfile = StringsFile("data/strings.txt")
	#ui.printdict(stringsfile.dict["down_right"],0,0)
	ui.printmatrix(testmatrix)
	ui.printdict(stringsfile.dict["highlighted"],0,0)
	#ui.hud(42,1999,[10,10])
	ui.cursesinstance.getch()
	endwin()