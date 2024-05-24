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

if __name__ == '__main__':
    population_size = 100
    generations = 100
    population = []

    # Create a population of SimpleModel instances
    for i in range(population_size):
        population.append(SimpleModel(dims=(7, 10, 4)))
    
    # Run the genetic algorithm for a number of generations
    for generation in range(generations):
        fitness_scores = []

        # Run the game for each individual in the population
        for individual in population:
            game = SnakeGame()
            controller = GAController(game, display=False, model=individual)
            steps, score = game.run()
            if hasattr(individual, 'fitness'):
                fitness = individual.fitness(steps, score)
            else:
                print(f"Individual of type {type(individual)} does not have a fitness method")
            fitness_scores.append((fitness, individual))
            print(f"Generation {generation + 1}, Individual: Steps = {steps}, Score = {score}, Fitness = {fitness}")

        max_fitness = max(fitness_scores, key=lambda x: x[0])[0]
        print(f"Max fitness over {generations} generations: {max_fitness}")

        # Sort the fitness_scores list in descending order based on the fitness score
        fitness_scores.sort(key=lambda x: x[0], reverse=True)

        # Calculate the number of individuals to keep
        num_to_keep = len(fitness_scores) // 2

        # Keep the first half of the list
        fitness_scores = fitness_scores[:num_to_keep]

        # Extract the individuals from the fitness_scores list
        population = [individual for fitness, individual in fitness_scores]
        print(f"Population size: {len(population)}")

        # Create new individuals by crossing over the existing ones
        for individual in population:
            partner = random.choice(population)
            child = individual.__add__(partner)
            population.append(child)
        print(f"Population size after crossover: {len(population)}")
        
        # Mutate the population
        for individual in population:
            individual.mutate(0.1)
    
