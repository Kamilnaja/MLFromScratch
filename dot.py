import numpy as np

first = [1, 2, 3]
second = [4, 5, 6]


def dot_product(first, second):
    return np.dot(first, second)


res = dot_product(first, second)

print(res)
