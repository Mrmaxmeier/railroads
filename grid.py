UP = "up"
DOWN = "down"
LEFT = "left"
RIGHT = "right"

dirs = [UP, DOWN, LEFT, RIGHT]
opposites = {UP:DOWN, DOWN:UP, LEFT:RIGHT, RIGHT:LEFT}

class RailOutOfBoundsException:
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

class Grid:
	def __init__(self, xsize, ysize):
		self.dict = {}
		for x in range(xsize):
			for y in range(ysize):
				self.dict[y, x] = Field((y,x))
				if y < 0:
					self.dict[y, x].connectTo(UP, self.dict[y-1, x])
				if x < 0:
					self.dict[y, x].connectTo(LEFT, self.dict[y, x-1])

#print Grid(2, 3).dict
