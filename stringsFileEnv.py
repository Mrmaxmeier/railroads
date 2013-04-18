import curses,time,logger
from stringBasics import *

def combine(*args):
	res = {}
	for d in args:
		for k, v in d.items():
			res[k] = v
	return res

def format(img, mask, **conf):
	res = {}
	for key, ch in img.items():
		if mask.__contains__(key):
			mchar = mask[key]
			fs = conf[mchar.char]
			for f in fs:
				ch = f(ch)
		res[key] = ch
	return res
