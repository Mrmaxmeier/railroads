from logger import *

UP,RIGHT,DOWN,LEFT = "UP","RIGHT","DOWN","LEFT"


class Route():
	def __init__(self, trainID,y,x,dir = 0,startdir = "right"):
		self.trainID = trainID
		self.y,self.x = y,x
		self.current_frame = 0
		self.current_pos = [self.y,self.x]
		self.current_dir = dir
		self.start_dir = startdir
		self.route = []
		log("New Route")
	def add(self,dir):
		self.route.append(dir)
		#log("RouteOBJ: "+str(self.route))
	def reset(self):
		self.__init__(self,self.trainID,self.y,self.x)
	def get(self,frame = -1):
		if frame == -1:
			frame = self.current_frame
		elif frame == 0:
			return self.y,self.x,self.start_dir
		framed_route = []
		for i in range(frame+1):
			framed_route.append(self.route[i])
		list = [UP,RIGHT,DOWN,LEFT]
		listindex = 0
		past_gdir = self.start_dir
		past_y,past_x = self.y,self.x
		for present_ldir in framed_route:
			future_gdir = self.get_next_dir(past_gdir,present_ldir)
			if present_ldir == "forward":
				change = [0,0]
				if future_gdir   == "left":  change = [0,-1]
				elif future_gdir == "right": change = [0,1]
				elif future_gdir == "up":    change = [-1,0]
				elif future_gdir == "down":  change = [1,0]
				future_y = past_y+change[0]
				future_x = past_x+change[1]
			else:
				pass
			##4 Next LoopInstance:
			past_y,past_x = future_y,future_x
			past_gdir = future_gdir
		return past_y,past_x,past_gdir
	def get_next_dir(self,olddir,newdir):
		olddict = {"up":0,"right":1,"down":2,"left":3}
		newdict = {"forward":0,"right":1,"backward":2,"left":3}
		num =  olddict[olddir]
		num += newdict[newdir]
		num = num%4
		dict = {0:"up",1:"right",2:"down",3:"left"}
		return dict[num]#,num
	def next(self):
		if self.current_frame < len(self.route)-1:
			self.current_frame += 1
		else:
			self.current_frame = 0

if __name__ == "__main__":
	route = Route("TRAIN_ID",3,4,1)#y,x,right
	route.add("forward")
	route.add("right")
	route.add("forward")
	route.add("forward")
	route.add("left")
	route.add("forward")
	route.add("right")
	route.add("right")
	route.add("forward")
	for i in range(len(route.route)):
		pass#log(route.get(i),2)