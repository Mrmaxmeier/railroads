import curses

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

def combine(*args):
	res = {}
	for d in args:
		for k, v in d.items():
			res[k] = v

def format(img, mask, **conf):
	res = {}
	for key, ch in img:
		fs = conf.get(mask.get(key, None), [])
		for f in fs:
			ch = f(ch)
		res[key] = ch
