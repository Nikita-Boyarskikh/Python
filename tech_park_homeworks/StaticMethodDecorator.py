class StaticMethod:
	
	def __get__(self, obj, obj_type):
		def foo1(*args, **kwargs):
			return self.func(*args, **kwargs)
		return foo1

	def __init__(self, func):
		self.func = func
		
class Class:
	@StaticMethod
	def foo(message):
		print(message)
		
obj = Class()

obj.foo("Hello")
obj.foo = lambda(x): print(x + 'a')
obj.foo()
obj.foo()
