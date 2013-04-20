from time import *

class StoppableClock:
	def __init__(self, startTime=0, running=False):
		self.time = startTime
		self.running = False
		if running: self.start()
	
	def start(self):
		self.lastStarted  = time()
		self.running = True
	
	def stop(self):
		self.time = self.getTime()
		self.running = False
	
	def getTime(self):
		if not self.running:
			return self.time
		return self.time + (time() - self.lastStarted)
	
	def __str__(self):
		return "%sUhr (%ds)" % ("gestartete " if self.running else "", self.getTime())
