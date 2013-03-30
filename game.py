#!/usr/local/bin/python3
import time




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
		self.objects = {"station":((1,1),("data","data"))}
		self.objects = [[[[1,1],["Station",]]],[[[2,2],"UpCurve",1.42]],
		[[[3,3],"OldieTrain","MyShittyTrain",1642,42]],[[[4,4],"Library","Max's Bookstore",42]]]
		self.routes =  []
		self.clock = time.time()
		self.year = 1830
		self.money = 500
		self.highlighted = [0,0]
		self.screensize = [0,0]
		self.trainlist = [[[3,3],"OldieTrain","MyShittyTrain",1642,42,"train_hr"]]
	def elapsedtime(self):
		return (time.time() - self.clock)
	def tick(self):
		self.year = self.elapsedtime()/60
		#print("Year:",int(self.year))
		self.tick_move()
	def tick_move(self):
		for train in self.objects[2]:
			print("Train",train)
		for station in self.objects[0]:
			print("Station",station)
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