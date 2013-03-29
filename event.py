from curses import *
def parseevent(event,gameobj):
	if event == KEY_LEFT:
		gameobj.move_highlight("LEFT")
	elif event == KEY_RIGHT:
		gameobj.move_highlight("RIGHT")
	elif event == KEY_UP:
		gameobj.move_highlight("UP")
	elif event == KEY_DOWN:
		gameobj.move_highlight("DOWN")