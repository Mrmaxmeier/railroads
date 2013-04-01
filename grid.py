UP = "up"
DOWN = "down"
LEFT = "left"
RIGHT = "right"

dirs = [UP, DOWN, LEFT, RIGHT]
opposites = {UP:DOWN, DOWN:UP, LEFT:RIGHT, RIGHT:LEFT}

class RailOutOfBoundsException(Exception):
	pass

class Field:
	def __init__(self, pos):
		self.pos = pos
		self.neighbors = {}
		for dir in dirs:
			self.neighbors[dir] = (False, None)
		self.hasStation = False
	
	def connectTo(self, dir, other):
		self.neighbors[dir] = (False, other)
		other.neighbors[opposites[dir]] = (False, self)
	
	def disconnect(self, dir):
		other = self.neighbors[dir][1]
		self.neighbors[dir] = (False, None)
		other.neighbors[opposites[dir]] = (False, None)
	
	def buildStation(self):
		self.hasStation = True
	
	def destroyStation(self):
		self.hasStation = False
	
	def toggleStation(self):
		self.hasStation = not self.hasStation
	
	def buildRail(self, dir):
		other = self.neighbors[dir][1]
		if other == None:
			raise RailOutOfBoundsException
		self.neighbors[dir] = (True, other)
		other.neighbors[opposites[dir]] = (True, self)
	
	def destroyRail(self, dir):
		other = self.neighbors[dir][1]
		if other == None:
			raise RailOutOfBoundsException
		self.neighbors[dir] = (False, other)
		other.neighbors[opposites[dir]] = (False, self)
	
	def toggleRail(self, dir):
		if self.neighbors[dir][0]:
			self.destroyRail(dir)
		else:
			self.buildRail(dir)
	def isRail(self,dir):
		return self.neighbors[dir][0]


class Grid:
	def __init__(self, xsize, ysize):
		self.xsize,self.ysize = xsize,ysize
		self.dict = {}
		for x in range(self.xsize):
			for y in range(self.ysize):
				self.dict[y, x] = Field((y,x))
				if y > 0:
					self.dict[y, x].connectTo(UP, self.dict[y-1, x])
				if x > 0:
					self.dict[y, x].connectTo(LEFT, self.dict[y, x-1])
	
	def returnmatrix(self):
		parts = {(1,1,0,0):"left_right",(0,0,1,1):"up_down",(1,0,1,0):"left_up",
			(1,0,0,1):"left_down",(0,1,1,0):"right_up",(1,1,1,1):"left_right_up_down",
			(1,1,1,0):"left_right_up",(0,1,1,1):"right_up_down",(1,0,1,1):"left_up_down",
			(0,0,0,0):"clean",(1,0,0,0):"left",(0,1,0,0):"right",(0,0,1,0):"up",
			(0,0,0,1):"down",(1,1,0,1):"left_right_down",(0,1,0,1):"right_down"}
		matrix = []
		for y in range(self.ysize):
			xmatrix = []
			for x in range(self.xsize):
				cfield_left,cfield_right,cfield_down,cfield_up = False,False,False,False
				if self.dict[y, x].neighbors[LEFT][0]: cfield_left = True
				if self.dict[y, x].neighbors[RIGHT][0]: cfield_right = True
				if self.dict[y, x].neighbors[DOWN][0]: cfield_down = True
				if self.dict[y, x].neighbors[UP][0]: cfield_up = True
				xmatrix.append(parts[(cfield_left,cfield_right,cfield_up,cfield_down)])
			matrix.append(xmatrix)
		return matrix
				
#grid = Grid(2,3)
#print(grid.dict[0,0].neighbors)
#print Grid(2, 3).dict
