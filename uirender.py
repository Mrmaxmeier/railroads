#!/usr/local/bin/python3



#tested with font "Curier"
train = """
/‾‾‾‾‾‾‾\\
|  -TR  P
o‾o‾‾‾o‾o"""[1:]
station = """
/‾‾‾‾‾‾‾\\
|  -ST  |
‾‾‾‾‾‾‾‾‾"""[1:]



side = """
_________
---------
‾‾‾‾‾‾‾‾‾"""[1:]

up = """
   |¦|   
   |¦|   
   |¦|   """[1:]

left_down = """
_____    
-----|   
‾‾‾|¦|   """[1:]

down_right = """
    _____
   |-----
   |¦|‾‾‾"""[1:]
left_up = """
___|¦|   
-----|   
‾‾‾‾‾    """[1:]
up_right = """
   |¦|___
   |-----
    ‾‾‾‾‾"""[1:]




def combine_strings(strings):
	result = ""
	resultdict = {}
	xlength = len(strings)
	ylength = len(strings[0].split("\n"))
	dictcoords = (-1,-1)
	#print("X,Y",xlength,ylength)
	for string in strings:
		dictcoords = (dictcoords[0]+1,-1)
		#print("Aussen",dictcoords)
		#print("Hudshauidha:",string.split("\n"))
		for line in string.split("\n"):
			dictcoords = (dictcoords[0],dictcoords[1]+1)
			#print("innen",dictcoords)
			resultdict[dictcoords] = (line)
	#print(resultdict)
	for y in range(ylength):
		for x in range(xlength):
			result += resultdict[(x,y)]
		if not y == ylength-1:
			result += "\n"
	return result






if __name__ == "__main__":
	testmatrix =   [[down_right,side,side,side,left_down],
					[station,left_down,down_right,left_down,up],
					[up,up,station,up,up],
					[up,up_right,train,left_up,up],
					[up_right,side,side,side,left_up]]
	print()
	for i in testmatrix:
		print(combine_strings(i))










class UI:
	def __init__(self,matrix):
		self.matrix = matrix








class Renderer(UI):
	pass