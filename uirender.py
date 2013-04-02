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
	def __init__(self,gameobj,stringsfile,stdscr):
		self.stringsfile = stringsfile
		self.gameobj = gameobj
		self.cursesinstance = self.initcurses(stdscr)
		self.screensize = self.cursesinstance.getmaxyx() #Y,X
		self.tilesize = [3,9]
		self.gameobj.screensize = self.screensize
		self.inmenu = 0
	def initcurses(self,stdscr):
		#stdscr = initscr()
		#start_color()
		noecho()
		start_color()
		cbreak()
		curs_set(0)
		stdscr.keypad(1)
		#stdscr.nodelay(1)
		locale.setlocale(locale.LC_ALL,"")
		return stdscr
	def cprint(self,Y,X,str,type = None):
		#print "Printing:",str
		if Y >= self.screensize[0] or X >= self.screensize[1]: pass
		else:
			if type == None:
				self.cursesinstance.addstr(Y,X,str.encode('utf_8'))
			else:
				self.cursesinstance.addstr(Y,X,str.encode('utf_8'),type)
	def charprint(self,Y,X,charobj):
		if Y >= self.screensize[0] or X >= self.screensize[1]: pass
		else: charobj.draw(Y,X,self.cursesinstance)
	def hud(self):
		string = "Coins: "+str(self.gameobj.money)
		self.cprint(0,self.screensize[1]-(len(string)+1),string)
		string = self.gameobj.month+" "+str(self.gameobj.year)
		self.cprint(1,self.screensize[1]-(len(string)+1),string)
		if self.inmenu == 0:
			string = "[M]enu: [B]uildMode [R]efresh"
		elif self.inmenu == 2:
			string = "Your in BuildMode!"
			self.cprint(self.screensize[0]-3,self.screensize[1]-(len(string)+1),string)
			string = "<W,D,A,S> to toggle Connections, 'Return' to create a Station;"
			self.cprint(self.screensize[0]-2,self.screensize[1]-(len(string)+1),string)
			string = "[E]xit BuildMode [R]efresh"
		else:
			string = "..."
		self.cprint(self.screensize[0]-1,self.screensize[1]-(len(string)+1),string)
	def printdict(self,dict,Y,X):
		for yi,xi in dict.keys():
			#print "Printing:",dict[(yi,xi)]
			self.charprint(yi+Y,xi+X,dict[(yi,xi)])
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
			
			self.gameobj.refresh_matrix()
		self.printmatrix()
		self.printdict(self.stringsfile.dict["highlighted"],self.gameobj.highlighted[0]*3,self.gameobj.highlighted[1]*9)
		for station in self.gameobj.stationlist:
			self.printdict(self.stringsfile.dict["station_vl"],station[0][0]*3,station[0][1]*9)
		self.render_trains()
		self.hud()
		if self.inmenu == 1:
			self.printdict(self.stringsfile.dict["menu"],int(self.screensize[0]/2),int(self.screensize[1]/2))
		self.cursesinstance.refresh()
	def render_trains(self):
		for route in self.gameobj.routelist:
			train_y,train_x,rotation = route.get()
			if rotation ==   "up":   dict = "vu"
			elif rotation == "down": dict = "vd"
			elif rotation == "left": dict = "hr"
			elif rotation == "right":dict = "hl"
			dict = "train_"+dict
			self.printdict(self.stringsfile.dict[dict],train_y*3,train_x*9)
	def idlerefresh(self):
		self.screensize = self.cursesinstance.getmaxyx() #Y,X
		self.gameobj.screensize = self.screensize
		self.refresh()