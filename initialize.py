import nnfs
import numpy as np

from threevalues import a

nnfs.init()

n_inputs = 2
n_neurons = 4

weights = 0.01 * np.random.randint(n_inputs, n_neurons)
print(a)

print(a.isalpha())

M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
col2 = [row[0] + 4 for row in M]

mielonka = 'mielonka'

letter = [letter * 2 for letter in mielonka]

hello = 'hello'
helloLetter = (le + ' ' for le in hello)

print(list(map(sum, M)))
