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

# print(list(map(sum, M)))
# print({sum(row) for row in M})
# print({i: sum(M[i]) for i in range(3)})
D = {}
D['imie'] = 'Kamil'
D['zawod'] = 'programista'
D['wiek'] = 25

bob1 = dict(imie='Robert', zawod='programista', wiek=25)
rec = {'dane osobowe': {'imie': 'Robert', 'zawod': [
    'programista', 'inźynier'], 'wiek': 25}}
rec['dane osobowe']['zawod'].append('leśnik')
# print(rec['dane osobowe']['zawod'])
L = []
print(type(L))

print(7.0 / 3.0)
print(7.0 // 3.0)

# calculate 7 modulo 3
print(7 % 3)
