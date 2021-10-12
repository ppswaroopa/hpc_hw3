import numpy as np
x = np.array([[0, 10, 20], [20, 30, 40]])
print("Original array: ")
print(x)
print("Values larger than 10 =", x[x > 10])
print("Indices:", np.nonzero(x > 10))
