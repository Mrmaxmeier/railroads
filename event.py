from curses import *
from grid import *
import sys
class Event:
	def __init__(self,uiobject,gameobject):
		self.uiobj = uiobject
		self.gameobj = gameobject
	def parseevent(self,event):
		if self.uiobj.inmenu == 0:#Ingame
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
			elif event == ord("B") or event == ord("b"):
				self.uiobj.inmenu = 2
				self.uiobj.refresh("all")
		elif self.uiobj.inmenu == 1:#Menu
			if event == ord("E") or event == ord("e") or event == ord("M") or event == ord("m"):
				self.uiobj.inmenu = 0
				self.uiobj.refresh("all")
		elif self.uiobj.inmenu == 2:#BuildMode
			if event == ord("E") or event == ord("e"):
				self.uiobj.inmenu = 0
				self.uiobj.refresh("all")
			if event == ord("W") or event == ord("w"):
				self.gameobj.grid.dict[self.gameobj.highlighted[0],self.gameobj.highlighted[1]].buildRail(UP)
			if event == ord("D") or event == ord("d"):
				self.gameobj.grid.dict[self.gameobj.highlighted[0],self.gameobj.highlighted[1]].buildRail(RIGHT)
			if event == ord("A") or event == ord("a"):
				self.gameobj.grid.dict[self.gameobj.highlighted[0],self.gameobj.highlighted[1]].buildRail(LEFT)
			if event == ord("S") or event == ord("s"):
				self.gameobj.grid.dict[self.gameobj.highlighted[0],self.gameobj.highlighted[1]].buildRail(DOWN)
			if event == KEY_LEFT:
				self.gameobj.move_highlight("LEFT")
			elif event == KEY_RIGHT:
				self.gameobj.move_highlight("RIGHT")
			elif event == KEY_UP:
				self.gameobj.move_highlight("UP")
			elif event == KEY_DOWN:
				self.gameobj.move_highlight("DOWN")