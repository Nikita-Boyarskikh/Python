class Desc:
	def __init__(self, filename):
		self.filename = filename
		self.v = None
	
	def __get__(self, obj, obj_type):
		return self.v
	
	def __set__(self, obj, value):
		with open(self.filename, "a") as f:
			f.write(str(value) + "\n")
		self.v = value
	
	
class Class:
	attr = Desc("log.txt")
	
obj =Class()

obj.attr = 1
obj.attr = 2


