from curses import *
import sys
class Event:
	def __init__(self,uiobject,gameobject):
		self.uiobj = uiobject
		self.gameobj = gameobject
	def parseevent(self,event):
		if self.uiobj.inmenu == 0:
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
			elif event == ord("M") or event == ord("m"):
				self.uiobj.inmenu = 1
				self.uiobj.refresh("all")
		elif self.uiobj.inmenu == 1:
			if event == ord("E") or event == ord("e") or event == ord("M") or event == ord("m"):
				self.uiobj.inmenu = 0
				self.uiobj.refresh("all")