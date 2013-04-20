from curses import *
import curses,time,logger
import copy

black = curses.COLOR_BLACK
white = curses.COLOR_WHITE
red = curses.COLOR_RED
green = curses.COLOR_GREEN
blue = curses.COLOR_BLUE
cyan = curses.COLOR_CYAN
magenta = curses.COLOR_MAGENTA
yellow = curses.COLOR_YELLOW

italic = lambda *args: lambda ch: ch.italic(*args)
bold = lambda *args: lambda ch: ch.bold(*args)
underline = lambda *args: lambda ch: ch.underline(*args)
blink = lambda *args: lambda ch: ch.blink(*args)

textCol = lambda *args: lambda ch: ch.textCol(*args)
backCol = lambda *args: lambda ch: ch.backCol(*args)


def right(pos, strlen):
	(y, x) = pos
	return (y, x)

def left(pos, strlen):
	(y, x) = pos
	return (y, x-strlen)

class Img(dict):
	def __init__(self, *args, **kwd):
		dict.__init__(self, *args, **kwd)
		self.textPoss = {}
	
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
	
	def copy(self):
		return copy.deepcopy(self)
	
	def setTextPos(self, name, pos, align=right):
		self.textPoss[name] = pos, align
	
	def giveText(self, texts={}, **texts2):
		texts.update(texts2)
		for k, text in texts.items():
			pos, align = self.textPoss[k]
			(y, x) = align(pos, len(text))
			for i, ch in enumerate(text):
				self[y, x+i] = Char(ch)

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

