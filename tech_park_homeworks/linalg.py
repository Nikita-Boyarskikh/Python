import numpy.linalg as lg
import numpy as np
a = np.ones((91,91))
for i in range(91):
	a[i][i]=-37
f = open('file', 'w')
print(lg.inv(a))

