import pickle
from logger import *
class Storage():
	def __init__(self):
		super(Storage, self).__init__()
		self.newGame()
	def newGame(self):
		self.year = 0
		self.playername = ""
		#TrainData
		#			Year	Rank
		self.trainProducers = [["Simens",2010,99]]
		#		ModelName FirmIndex Year Cost
		self.trains = [["BeepBeep",0,2011,120]]
		#		ProductName    Cost
		self.products = [["Electronics",1300]]
	def save(self):
		pickle.dump(self,open("StorageSave.pickle","wb" ))
	def load(self):
		try:
			load = pickle.load(open("StorageSave.pickle","rb" ))
		except:
			print("Failed to Load...")
			log("Failed to LoadSavegame...")
			load = self
		#self.playername = load.playername
		datas = ["playername","year","trainProducers","trains","products"]
		for data in datas:
			exec("self."+data+" = load."+data)




if __name__ == "__main__":
	s = Storage()
	print(s)
	s.load()
	print(s)
	print(s.playername)
	s.playername = s.playername+"Test"
	s.save()