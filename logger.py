import os

file = open("./log.txt","a")

file.write("""
Starting new Log....

""")

def log(*string,level = 0):
	file.write(str(string)+", in Level "+str(level)+".\n")