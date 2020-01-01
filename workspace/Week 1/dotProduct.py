import numpy as np

a = np.array([2,2])
b = np.array([2,-2])

s = 0;
for i in range( len (a)):

	product = a[i]*b[i]
	s = s + product
	print("i = ", i, "product = ", product, "S = ", s)
print(s)


