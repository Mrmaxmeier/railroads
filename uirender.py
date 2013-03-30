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
	def __init__(self,gameobj,stringsfile):
		self.stringsfile = stringsfile
		self.gameobj = gameobj
		self.cursesinstance = self.initcurses()
		self.screensize = self.cursesinstance.getmaxyx() #Y,X
		self.tilesize = [3,9]
		self.gameobj.screensize = self.screensize
		self.inmenu = 0
	def initcurses(self):
		stdscr = initscr()
		#start_color()
		noecho()
		start_color()
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
		string = "Coins: "+str(self.gameobj.money)
		self.cprint(0,self.screensize[1]-(len(string)+1),string)
		string = "Year: "+str(self.gameobj.year)
		self.cprint(1,self.screensize[1]-(len(string)+1),string)
		string = "Menu: [B]uildMode [Q]uit [P]ause [R]efresh"
		self.cprint(self.screensize[0]-1,self.screensize[1]-(len(string)+1),string)
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
				self.printdict(self.stringsfile.dict[dict],coords[0],coords[1])
	def railmatrix_to_matrix(railmatrix):
		pass
	def refresh(self,option = None):
		self.cursesinstance.clear()
		if option == "all":
			self.screensize = self.cursesinstance.getmaxyx() #Y,X
			self.gameobj.screensize = self.screensize
		self.printmatrix()
		self.printdict(self.stringsfile.dict["highlighted"],
		self.gameobj.highlighted[0]*3,self.gameobj.highlighted[1]*9)
		for train in self.gameobj.trainlist:
			self.printdict(self.stringsfile.dict[train[5]],train[0][0]*3,train[0][1]*9)
		self.hud()
		self.cursesinstance.refresh()
import time