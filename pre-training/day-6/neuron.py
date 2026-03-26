import math
import random


# PART 1 — Activation Functions + Single Neuron

def sigmoid(x):
    """Squashes any number into the range (0, 1).
    Used when you want an output that looks like a probability."""
    return 1 / (1 + math.exp(-x))


def relu(x):
    """Returns x if positive, else 0.
    Kills negative signals — fast and simple."""
    return max(0, x)


class Neuron:
    """A single neuron: computes activation(dot(weights, inputs) + bias).

    Each weight controls how much that input matters.
    The bias shifts the result up or down regardless of the inputs.
    """

    def __init__(self, n_inputs, activation="sigmoid"):
        # Random small weights — one per input
        self.weights    = [random.uniform(-1, 1) for _ in range(n_inputs)]
        self.bias       = random.uniform(-1, 1)
        self.activation = sigmoid if activation == "sigmoid" else relu

    def forward(self, inputs):
        # Step 1: weighted sum  →  w1*x1 + w2*x2 + ... + bias
        weighted_sum = sum(w * x for w, x in zip(self.weights, inputs)) + self.bias
        # Step 2: squeeze through activation function
        return self.activation(weighted_sum)


# PART 2 — Dense Layer (a row of neurons)

class DenseLayer:
    """A layer of neurons that all receive the same inputs.

    n_inputs  — how many numbers come in
    n_neurons — how many neurons (= how many numbers go out)
    """

    def __init__(self, n_inputs, n_neurons, activation="sigmoid"):
        self.neurons = [Neuron(n_inputs, activation) for _ in range(n_neurons)]

    def forward(self, inputs):
        # Each neuron processes the same inputs independently
        return [neuron.forward(inputs) for neuron in self.neurons]

    def set_weights(self, weights, biases):
        """Manually override weights and biases (for reproducible demos)."""
        for neuron, w, b in zip(self.neurons, weights, biases):
            neuron.weights = w
            neuron.bias    = b


# PART 3 — Tiny Network: two layers stacked

def build_network():
    """Layer 1: 3 inputs → 4 neurons  (hidden layer)
       Layer 2: 4 inputs → 2 neurons  (output layer)"""

    layer1 = DenseLayer(n_inputs=3, n_neurons=4, activation="relu")
    layer2 = DenseLayer(n_inputs=4, n_neurons=2, activation="sigmoid")

    # Manually set weights so the output is always the same (no random seed needed)
    # Each sub-list = one neuron's weights, one per input
    layer1.set_weights(
        weights=[
            [ 0.5, -0.3,  0.8],   # neuron 1 weights
            [-0.2,  0.6, -0.1],   # neuron 2 weights
            [ 0.9,  0.1,  0.4],   # neuron 3 weights
            [-0.5,  0.7, -0.9],   # neuron 4 weights
        ],
        biases=[0.1, -0.2, 0.3, 0.0],
    )

    layer2.set_weights(
        weights=[
            [ 0.4, -0.5,  0.2, -0.3],   # output neuron 1 weights
            [-0.1,  0.8, -0.6,  0.5],   # output neuron 2 weights
        ],
        biases=[0.2, -0.1],
    )

    return layer1, layer2


def forward_pass(inputs):
    """Run inputs through the full network and return final outputs."""
    layer1, layer2 = build_network()

    hidden_outputs = layer1.forward(inputs)   # 3 numbers → 4 numbers
    final_outputs  = layer2.forward(hidden_outputs)  # 4 numbers → 2 numbers

    return hidden_outputs, final_outputs


# PART 4 — Run it and print everything

def main():
    sample_input = [0.5, -0.3, 0.8]

    print("\n" + "═" * 50)
    print("  Tiny Neural Network — Forward Pass")
    print("═" * 50)

    print(f"\n  Input              : {sample_input}")

    hidden_outputs, final_outputs = forward_pass(sample_input)

    print(f"\n  After Layer 1 (ReLU)    :")
    for i, val in enumerate(hidden_outputs):
        print(f"    Neuron {i+1}: {val:.6f}")

    print(f"\n  After Layer 2 (Sigmoid) :")
    for i, val in enumerate(final_outputs):
        print(f"    Output {i+1}: {val:.6f}")

    print("\n" + "─" * 50)
    print("  What each part does:")
    print("  Weight  → controls how much each input influences a neuron")
    print("  Bias    → shifts the output up/down, independent of inputs")
    print("  ReLU    → kills negatives (output=0), passes positives through")
    print("  Sigmoid → squashes output between 0 and 1 (probability-like)")
    print("─" * 50 + "\n")


if __name__ == "__main__":
    main()
