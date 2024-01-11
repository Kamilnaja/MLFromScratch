import nnfs
import numpy as np

nnfs.init()

n_inputs = 2
n_neurons = 4

weights = 0.01 * np.random.randint(n_inputs, n_neurons)
