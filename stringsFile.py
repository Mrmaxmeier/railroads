#!/usr/local/bin/python3
import curses
import codecs
import copy
import stringsFileEnv
from curses import *
from logger import *
from stringBasics import *


class StringsFile:
	def __init__(self, name):
		self.dict = copy.copy(stringsFileEnv.__dict__)
		f = codecs.open(name, encoding='utf-8')
		curImg = None
		for line in f:
			print("TEST")
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
				print("Lalal")
				name, _, expr = line.partition("=")
				print(name, _, expr)
				name = name.strip()
				val = eval(expr, self.dict)
				if name:
					self.dict[name] = val
			else:
				colKey = ""
				if ":" in line:
					line, _, colKey = line.partition(":")
				img = Img()
				self.dict[line.strip()] = img
				curImg = (img, 0, colKey)
		f.close()


if __name__ == "__main__":
	 print(StringsFile("data/strings17*7.txt").dict.keys())
