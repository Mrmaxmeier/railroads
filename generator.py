def gen_train(year,name = "Untitled Train"):
	return ["OldieTrain","MyShittyTrain",1642,42]]



import os
from namegen import NameGen


def genname(filename):
	files = os.listdir('./Languages')
	exit = False
	generator = NameGen('Languages/' + filename)
	for i in range(20):
		print generator.gen_word()
	print '\nPress Enter to continue.'
	try:
		raw_input()
	except EOFError:
		pass