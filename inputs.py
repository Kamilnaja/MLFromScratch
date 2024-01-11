import numpy as np

inputs = [[1.0, 2.0, 3.0, 2, 5],
          [2.0, 3.0, 4.0, 5, 6],
          [3.0, 4.0, 5.0, 6, 7]]
weights = [[0.2, 0.8, -0.5, 1, 1],
           [0.5, -0.91, 0.26, 1, 1],
           [-0.26, -0.27, 0.17, 1, 1]]
biases = [2.0, 3.0, 0.5]

weights2 = [[0.1, -0.14, 0.5],
            [-0.5, 0.12, -0.33],
            [-0.44, 0.73, -0.13]]
biases2 = [-1, 2, -0.5]


outputs = np.dot(inputs, np.array(weights).T) + biases

layer1_outputs = np.dot(inputs, np.array(weights).T) + biases
layer2_outputs = np.dot(layer1_outputs, np.array(weights2).T) + biases

print(layer2_outputs)
