#!/usr/local/bin/python3
import codecs
class StringsFile:
	def __init__(self, name):
		self.dict = {}
		f = open(name)#, "r")
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
	print(StringsFile("data/strings.txt").dict.keys())
