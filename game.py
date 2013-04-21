#!/usr/local/bin/python3
import time
from time import *
from grid import *
from route import *
from storage import *
from StoppableClock import *



class Game:
	def __init__(self):
		"""
		Game.objects = [Stations[[X,Y],["Name",state,Needs,Goods]]
					,RoadObjects[[X,Y],Type,SpeedMultiplyer]
					,Trains[[X,Y],Type,Name,BuildYear,Speed]
					,Buildings[[X,Y],Type,Name,Money/Coins]]
		Game.routes = [[TrainID,[stations 1,2,3...],actpos]]
		"""
		#self.matrix =   {(1,1):("station","data","data")}
		#self.objects = {"station":((1,1),("data","data"))}
		#self.objects = [[[[1,1],["Station",]]],[[[2,2],"UpCurve",1.42]],
		#[[[3,3],"OldieTrain","MyShittyTrain",1642,42]],[[[4,4],"Library","Max's Bookstore",42]]]
		#self.routes =  []
		#self.clock = time()
		self.year = 1830
		self.month = "Janurary"
		self.highlighted = [0,0]
		self.screensize = [0,0]
		self.trainlist = [[[4,4],"OldieTrain","MyShittyTrain",1642,42,"train_hr"]]
		self.ctrain = 0
		self.stationlist = [] #[Coords],Status
		#self.grid = Grid(30,30)
		self.matrix = []
		self.routelist = []
		self.newsstrings = [["NEWS",5],["10 Sek",10],["5 Sek",5],["2 Sek",2],["20 Sek",10],["Info",1]]
		self.newsstringstimer = 0
		self.newsclock = StoppableClock(running = True)
		self.storage = Storage()
	#def elapsedtime(self):
	#	return self.storage.clock.getTime()
	def tick(self):
		#print("Year:",int(self.year))
		self.tick_move()
	def idletick(self):
		self.year = int((self.storage.clock.getTime()/60)+1830)
		months = ["   Jan","   Feb","   Mar","   Apr","  May","  June","  July","   Aug","   Sep","   Oct","   Nov","   Dec"]
		self.month = months[int(((self.storage.clock.getTime()/60)+1830-int((self.storage.clock.getTime()/60)+1830))*12)]
	def idleanimate(self):
		for route in self.routelist:
			route.next()
		#self.uiobj.refresh("all")
		
	def tick_move(self):
		#for train in self.objects[2]:
		#	pass
		#	#print("Train",train)
		#for station in self.objects[0]:
		#	pass
		#	#print("Station",station)
		self.refresh_matrix()
	def refresh_matrix(self):
		self.matrix = self.storage.grid.returnmatrix()
		self.stationlist = self.storage.grid.returnstations()
	def addobj(self,type,coords,data):
		pass
		#self.matrix[coords] = (type,data)
		#self.objects[type] = (coords,data)
	def move_highlight(self,direction):
		if direction == "LEFT" and self.highlighted[1]>0:
			self.highlighted[1] += -1
		if direction == "RIGHT" and self.highlighted[1]<self.screensize[1]:
			self.highlighted[1] += 1
		if direction == "UP" and self.highlighted[0]>0:
			self.highlighted[0] += -1
		if direction == "DOWN" and self.highlighted[0]<self.screensize[0]:
			self.highlighted[0] += 1
	def spend_money(self,val):
		if val > self.storage.money:
			return False
		else:
			self.storage.money += -val
			return True
	def gain_money(self,val):
		self.storage.money += val
	def getNews(self):
		#if self.newsstringstimer <= 0:
		#	self.newsstrings.remove(self.newsstrings[0])
		#	self.newsstringstimer = self.newsstrings[1]
		if self.newsclock.getTime() >= self.newsstrings[0][1]:
			if len(self.newsstrings) > 1:
				self.newsstrings.remove(self.newsstrings[0])
				self.newsclock.setTime(self.newsstrings[0][1])
			else:
				pass
		string = ""
		#if self.newsstrings != []:
		string = self.newsstrings[0][0]
		return string
	def pause(self):
		self.storage.clock.stop()
	def resume(self):
		self.storage.clock.start()

if __name__ == "__main__":
	game = Game()
	running = True
	#print(game.objects)
	game.tick()
	game.addobj("train",(1,2),("notsoshitty","Coolest Train Ever",4242,42))
	#print(game.objects)
	game.tick()
	#print(game.objects)
	while 1:
		time.sleep(5)
		game.tick()