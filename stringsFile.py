#!/usr/local/bin/python3
import curses
import codecs
import copy
import stringsFileEnv
from stringsFileEnv import black, white, red, green, blue, cyan, magenta, yellow
from curses import *
from logger import *

class Img(dict):
	def getDim(self):
		maxx = -1; maxy = -1
		for y, x in self.keys():
			maxx = max(x, maxx)
			maxy = max(y, maxy)
		return (maxy+1, maxx+1)
	
	def __str__(self):
		ydim, xdim = self.getDim()
		res = "\n"
		for y in range(ydim):
			for x in range(xdim):
				res += str(self.get((y, x), " "))
			res += "\n"
		return res
	__repr__ = __str__

class Char:
	def __init__(self, char):
		self.char = char
		
		self.vitalic = False
		self.vbold = False
		self.vunderline = False
		self.vblink = False
		
		self.vtextCol = white
		self.vbackCol = black
		
		self.initColorPairs()
	
	def __str__(self):
		return self.char
	
	def copy(self):
		return copy.deepcopy(self)
	
	def withCopy(self, prop, val):
		new = self.copy()
		new.__dict__[prop] = val
		return new
	
	def encode(self, *args, **kwd):
		return self.char.encode(*args, **kwd)
	
	def italic(self,b=True): return self.withCopy("vitalic", b)
	def bold(self,b=True): return self.withCopy("vbold", b)
	def underline(self,b=True): return self.withCopy("vunderline", b)
	def blink(self,b=True): return self.withCopy("vblink", b)
	
	def textCol(self,color): return self.withCopy("vtextCol", color)
	def backCol(self,color): return self.withCopy("vbackCol", color)
	
	def getattrs(self):
		c = 0
		if self.vbold: c = c | A_BOLD
		if self.vitalic: c = c | A_ITALIC
		if self.vunderline: c = c | A_UNDERLINE
		if self.vblink: c = c | A_BLINK
		c = c | color_pair(self.getColor())
		if self.vtextCol > 0 and self.vbackCol > 0: pass
		return c
	def getColor(self):
		if self.vtextCol == green and self.vbackCol == black: return 1
		if self.vtextCol == red and self.vbackCol == black: return 2
		curses.init_pair(44, self.vtextCol, self.vbackCol)
		return 44
	def initColorPairs(self):
		curses.init_pair(1, green, black)
		curses.init_pair(2, red, black)
	
	def draw(self,Y,X,cursesinstance):
		cursesinstance.addstr(Y,X,self.char,self.getattrs())



class StringsFile:
	def __init__(self, name):
		self.dict = copy.copy(stringsFileEnv.__dict__)
		f = codecs.open(name, encoding='utf-8')
		curImg = None
		for line in f:
			line = line[:-1]
			if line == "":
				curImg = None
			elif curImg != None:
				img, y, colKey = curImg
				for (x, ch) in enumerate(line):
					if ch != colKey:
						img[y, x] = Char(ch)
				curImg = img, y+1, colKey
			elif line.startswith("#"):
				pass
			elif "=" in line:
				name, _, expr = line.partition("=")
				val = eval(expr, self.dict)
				self.dict[name.strip()] = val
			else:
				colKey = ""
				if ":" in line:
					line, _, colKey = line.partition(":")
				img = {}
				self.dict[line.strip()] = img
				curImg = (img, 0, colKey)
		f.close()


if __name__ == "__main__":
	print(StringsFile("data/strings17*7.txt").dict.keys())
