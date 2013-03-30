from curses import *
import sys
class Event:
	def __init__(self,uiobject,gameobject):
		self.uiobj = uiobject
		self.gameobj = gameobject
	def parseevent(self,event):
		if event == KEY_LEFT:
			self.gameobj.move_highlight("LEFT")
		elif event == KEY_RIGHT:
			self.gameobj.move_highlight("RIGHT")
		elif event == KEY_UP:
			self.gameobj.move_highlight("UP")
		elif event == KEY_DOWN:
			self.gameobj.move_highlight("DOWN")
		elif event == ord("R") or event == ord("r"):
			self.uiobj.refresh("all")
		elif event == ord("Q") or event == ord("q"):
			sys.exit()