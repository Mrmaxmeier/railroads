import threading,queue

class Event_Catcher(threading.Thread):
	def __init__(self,queue,cursesinstance):
		threading.Thread.__init__(self)
		self.queue = queue
		self.cursesinstance = cursesinstance
	def run(self):
		while 1:
			event = self.cursesinstance.getch()
			self.queue.put(event)