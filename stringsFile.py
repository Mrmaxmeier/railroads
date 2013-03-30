import curses
import copy

black = curses.COLOR_BLACK
white = curses.COLOR_WHITE
red = curses.COLOR_RED
green = curses.COLOR_GREEN
blue = curses.COLOR_BLUE
cyan = curses.COLOR_CYAN
magenta = curses.COLOR_MAGENTA
yellow = curses.COLOR_YELLOW

class Char:
	def __init__(self, char):
		self.char = char
		
		self.vitalic = False
		self.vbold = False
		self.vunderline = False
		self.vblink = False
		
		self.vtextCol = white
		self.vbackCol = black
	
	def copy(self):
		return copy.deepcopy(self)
	
	def withCopy(self, prop, val):
		new = self.copy()
		new.__dict__[prop] = val
		return new
	
	def italic(b=True): self.withCopy("vitalic", b)
	def bold(b=True): self.withCopy("vbold", b)
	def underline(b=True): self.withCopy("vunderline", b)
	def blink(b=True): self.withCopy("vblink", b)
	
	def textCol(color): self.withCopy("vtextCol", color)
	def backCol(color): self.withCopy("vbackCol", color)



class StringsFile:
	def __init__(self, name):
		self.dict = {}
		f = open(name, "r")
		curImg = None
		for line in f:
			line = line[:-1]
			if line == "":
				curImg = None
			elif curImg != None:
				img, y, colKey = curImg
				for (x, ch) in enumerate(line):
					if ch != colKey:
						img[y, x] = ch
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
	print StringsFile("data/strings.txt").dict.keys()
