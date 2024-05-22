# This Python code defines a SimpleModel class for a genetic algorithm. 
# The class includes methods for updating the model based on an observation, 
# determining the action based on an observation, mutating the DNA based on a mutation rate, 
# defining the addition operation for two models, and returning the DNA of the model.

import random
from typing import Protocol, Tuple, List, Sequence
import numpy as np
from ga_models.ga_protocol import GAModel
from ga_models.activation import sigmoid, tanh, softmax

# Define a simple model for a genetic algorithm
class SimpleModel(GAModel):
    # Initialize the model with a tuple of dimensions
    def __init__(self, *, dims: Tuple[int, ...]): # Describes the NUMBER of dimensions of our neural network (input, hidden, output)
        assert len(dims) >= 2, 'Error: dims must be two or higher.'
        self.dims = dims
        self.DNA = []
        # Initialize the DNA with random values
        for i, dim in enumerate(dims):
            if i < len(dims) - 1:
                self.DNA.append(np.random.rand(dim, dims[i+1])) # Appends a randomly weighted neural network to our snake-agent.

    # Update the model based on the observation
    def update(self, obs: Sequence) -> Tuple[int, ...]:
        x = obs
        for i, layer in enumerate(self.DNA):
            if not i == 0:
                x = tanh(x)
            x = x @ layer
        return softmax(x)

    # Determine the action based on the observation
    def action(self, obs: Sequence):
        return self.update(obs).argmax()

    # Mutate the DNA based on the mutation rate
    def mutate(self, mutation_rate) -> None:
        if random.random() < mutation_rate:
            random_layer = random.randint(0, len(self.DNA) - 1)
            row = random.randint(0, self.DNA[random_layer].shape[0] - 1)
            col = random.randint(0, self.DNA[random_layer].shape[1] - 1)
            self.DNA[random_layer][row][col] = random.uniform(-1, 1)

    # Define the addition operation for two models
    def __add__(self, other):
        baby_DNA = []
        for mom, dad in zip(self.DNA, other.DNA):
            if random.random() > 0.5:
                baby_DNA.append(mom)
            else:
                baby_DNA.append(dad)
        baby = type(self)(dims=self.dims)
        baby.DNA = baby_DNA
        return baby
    
    def fitness(self):
        return (self.score * self.score) / (self.steps + 1)

    # Return the DNA of the model
    def DNA(self):
        return self.DNA