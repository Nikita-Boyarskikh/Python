def ignore_exceptions (*args):
    def decorated(out):
        l = args
        def func(*args, **kwargs):
            if(len(l) == 0):
                try:
                    result = out(*args, **kwargs)
                except:
                    result = None
            else:
                try:
                    result = out(*args, **kwargs)
                except l:
                    result = None
            return result
        return func
    return decorated

@ignore_exceptions(ZeroDivisionError)
def zeroDiv(x):
    return x/0

@ignore_exceptions(TypeError)
def twoDiv(x):
    return x/2

@ignore_exceptions()
def div(x, y):
    return x/y

@ignore_exceptions(TypeError)
def typeErrZeroDiv(x):
    return x/0

print(twoDiv('sdg;kjhflka'))
print(zeroDiv(1))
print(div('dgfkfs', 0))
print(typeErrZeroDiv('a'))
print(div(1,2))
print(typeErrZeroDiv(1))


#import time
#import random

#class timer:
#	def __init__(self):
#		pass
#
#	def elapsed(self):
#		return time.time() - self.t_start
#
#	def __enter__(self):
#		self.t_start = time.time()
#		return self
#		
#	def __exit__(self, *args):
#		self.t_end = time.time()
#		print("Time: " + str(self.t_end - self.t_start))
#		
#with timer() as t:
#	for _ in range(10):
#		time.sleep(random.random())
#		print("elapsed - " + str(t.elapsed()))
