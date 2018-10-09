#neuro.py - a basic set of neural network functions
#these are almost entirely based on the functions
#provided in the textbook (Data Science from Scratch)
#This is not an efficient nor robust implementation.
#For educational purposes only.

from __future__ import division
#import numpy as np
import math as math
import random
from linear_algebra import dot
import pickle

weights=[]

def writeNetworkToFile(fn, neural_network):
    with open(fn, 'wb') as f:
        try:
            pickle.dump(neural_network, f, protocol=2, fix_imports=True)
        except:
            pickle.dump(neural_network, f)

def readNetworkFromFile(fn):
    with open(fn, 'rb') as f:
        network = pickle.load(f)
    return network
    
def sigmoid(t):
    #t=np.clip(t, -700, 700)
    if t<-700:
        t=-700
    elif t>700:
        t=700
        
    return 1 / (1 + math.exp(-t))

def neuron_output(weights, inputs):
    return sigmoid(dot(weights, inputs))

def predict(neural_network, input_vector):
    return feed_forward(neural_network, input_vector)[-1][0]

def feed_forward(neural_network, input_vector):
    """takes in a neural network
    (represented as a list of lists of lists of weights)
    and returns the output from forward-propagating the input"""
    outputs = []
    # process one layer at a time
    for layer in neural_network:
        input_with_bias = input_vector + [1] # add a bias input
        output = [neuron_output(neuron, input_with_bias) # compute the output
                  for neuron in layer] # for each neuron
        outputs.append(output) # and remember it
        # then the input to the next layer is the output of this one
        input_vector = output

    return outputs

def backpropagate(network, input_vector, targets):
    output_layer=network[-1]
    hidden_outputs, outputs = feed_forward(network, input_vector)
    # the output * (1 - output) is from the derivative of sigmoid
    output_deltas = [output * (1 - output) * (output - target)
                     for output, target in zip(outputs, targets)]
    # adjust weights for output layer, one neuron at a time
    for i, output_neuron in enumerate(network[-1]):
        # focus on the ith output layer neuron
        for j, hidden_output in enumerate(hidden_outputs + [1]):
            # adjust the jth weight based on both
            # this neuron's delta and its jth input
            output_neuron[j] -= output_deltas[i] * hidden_output
    # back-propagate errors to hidden layer
    hidden_deltas = [hidden_output * (1 - hidden_output) *
                     dot(output_deltas, [n[i] for n in output_layer])
                     for i, hidden_output in enumerate(hidden_outputs)]
    # adjust weights for hidden layer, one neuron at a time
    for i, hidden_neuron in enumerate(network[0]):
        for j, input in enumerate(input_vector + [1]):
            hidden_neuron[j] -= hidden_deltas[i] * input


def train(network, input_vector, targets, reps):
    for __ in range(reps):
        for input, target in zip(input_vector,targets):
            backpropagate(network, input, target)

        

def setup_network(inputs):
    random.seed(0)
    input_size = len(inputs[0])
    num_hidden = 5
    output_size = 1

    hidden_layer = [[random.randrange(-1, 1)*random.random() for __ in range(input_size + 1)]
                    for __ in range(num_hidden)]
    # each output neuron has one weight per hidden neuron, plus a bias weight                 
    output_layer = [[random.randrange(-1,1)*random.random() for __ in range(num_hidden + 1)]
                    for __ in range(output_size)]
    # the network starts out with random weights                                              
    network = [hidden_layer, output_layer]
    
    return network
