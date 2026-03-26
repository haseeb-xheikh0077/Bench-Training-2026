Command:
python3 neuron.py

Output:
══════════════════════════════════════════════════
  Tiny Neural Network — Forward Pass
══════════════════════════════════════════════════

  Input              : [0.5, -0.3, 0.8]

  After Layer 1 (ReLU)    :
    Neuron 1: 1.080000
    Neuron 2: 0.000000
    Neuron 3: 1.040000
    Neuron 4: 0.000000

  After Layer 2 (Sigmoid) :
    Output 1: 0.698465
    Output 2: 0.303222

What is forward propagation :

Forward propagation is just the data moving forward through the network, one layer at a time. You start with your input numbers. Each neuron in the first layer takes all those numbers, multiplies each one by its own weight (how much it cares about that input), adds them all up, adds a bias (a nudge up or down), and then squashes the result through an activation function. That gives you a new set of numbers. Those new numbers become the input to the next layer, which does the exact same thing. You keep going forward until you reach the output layer. The final numbers are the network's answer.

What does each weight represent:
A weight is how strongly a neuron reacts to one specific input. A high positive weight means that input pushes the neuron strongly toward firing. A negative weight means that input suppresses the neuron. A weight near zero means that neuron mostly ignores that input.

What does the bias do:
The bias lets a neuron fire even when all inputs are zero or very small. Without it a neuron that gets weak inputs could never produce a meaningful output. It gives each neuron an independent baseline.

ReLU vs Sigmoid:
ReLU just returns 0 for anything negative and passes positive values through unchanged. This keeps the math simple and fast and it is good in hidden layers because it does not squash large values. Sigmoid squashes everything between 0 and 1 which makes it useful in the output layer when you want the answer to look like a probability. The problem with sigmoid in hidden layers is that for very large or very small inputs its output barely changes at all which makes learning slow. That is called the vanishing gradient problem.

What is missing for the network to actually learn:

Right now the weights are set manually. For the network to learn on its own it needs two things it currently does not have:

1. A loss function. Something that measures how wrong the output is compared to the correct answer. Right now there is no correct answer and no way to know if the output is good or bad.

2. Backpropagation. Once you know how wrong the output is you need to work backwards through the network to figure out how much each weight contributed to that error. Then you adjust each weight slightly in the direction that would have made the error smaller. That process repeated thousands of times on training data is how a network learns. Without it the weights just sit there doing nothing.
