# input layer
# neuron
inputs = [1, 2, 3, 2.5]

weights1 = [0.2, 0.8, -0.5, 1.0]
weights2 = [0.5, -0.91, 0.26, -0.5]
weights3 = [-0.26, -0.27, 0.17, 0.87]

weights = [weights1, weights2, weights3]

biases = [2, 3, 0.5]


def calculate_layer():
    layer_outputs = []  # output of current layer
    for neuron_weights, neuron_bias in zip(weights, biases):
        neuron_output = 0  # output of given neuron
        for n_input, weight in zip(inputs, neuron_weights):
            neuron_output += n_input * weight
        neuron_output += neuron_bias
        layer_outputs.append(neuron_output)
    return layer_outputs


layers = calculate_layer()

print(layers)
