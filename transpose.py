import numpy as np

a = [1, 2, 3]
b = [2, 3, 4]

a = np.array([a])
b = np.array([b]).T

dot = np.dot(a, b)
print(dot)

expanded = np.expand_dims(a, axis=0)
print(expanded.shape)
print(expanded)
