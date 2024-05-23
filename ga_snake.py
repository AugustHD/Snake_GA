# This Python script is used to run a snake game. 
# It first imports the necessary classes, then creates instances of the 
# SnakeGame and GAController classes. The game is then started with the run method.

#!/usr/bin/env python

# Import the SnakeGame class from the snake module
import random
from typing import Tuple
from snake import SnakeGame
# Import the GAController class from the ga_controller module
from ga_controller import GAController
from ga_models.ga_simple import SimpleModel

class Population:
    def __init__(self, population_size: int, dims: Tuple[int, ...]):
        self.agents = [SimpleModel(dims=dims) for _ in range(population_size)]
        self.population_size = population_size
        self.dims = dims

    def evolve(self, mutation_rate: float) -> None:
        new_generation = []
        for _ in range(self.population_size):
            parent1, parent2 = self.select_parents()
            if parent1 and parent2:
                child = parent1 + parent2
                child.mutate(mutation_rate)
                new_generation.append(child)
        self.agents = new_generation

    def select_parents(self) -> Tuple[SimpleModel, SimpleModel]:
        return tuple(random.sample(self.agents, 2))

    def evaluate(self, evaluate_function) -> None:
        for agent in self.agents:
            agent.fitness = evaluate_function(agent)

if __name__ == '__main__':
    population_size = 100
    generations = 100

    population = [SimpleModel(dims=(7, 10, 4)) for _ in range(population_size)]

    for generation in range(generations):
        fitness_scores = []

        for individual in population:
            game = SnakeGame()
            controller = GAController(game, display=False, model=individual)
            SimpleModel.mutate(individual, 0.5)
            steps, score = game.run()
            
            fitness = individual.fitness(steps, score)

            fitness_scores.append((fitness, individual))
            print(f"Generation {generation + 1}, Individual: Steps = {steps}, Score = {score}, Fitness = {fitness}")

        
    max_fitness = max(fitness_scores, key=lambda x: x[0])[0]
    print(f"Max fitness over {generations} generations: {max_fitness}")
