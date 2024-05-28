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
    population_size = 200
    generations = 1000
    population = []

    # Create a population of SimpleModel instances
    for i in range(population_size):
        population.append(SimpleModel(dims=(7, 10, 4)))
    
    # Run the genetic algorithm for a number of generations
    for generation in range(generations):
        fitness_scores = []
        generation_count = generation + 1

        # Run the game for each individual in the population, while keeping track of which agent it is
        for individual_count, individual in enumerate(population, start=1):

            game = SnakeGame()
            controller = GAController(game, display=False, model=individual)
            steps, score = game.run()
            fitness = individual.fitness(steps, score)
            fitness_scores.append((fitness, individual))
            print(f"Generation {generation + 1}, Individual nr. {individual_count}: Steps = {steps}, Score = {score}, Fitness = {fitness}")

        max_fitness = max(fitness_scores, key=lambda x: x[0])[0]
        print(f"Max fitness in generation {generation_count}: {max_fitness}")

        # The selection process below is a variation of the roulette wheel selection method.
        # It is likely not the optimal way to do selection.

        # Calculate the total fitness of the population
        total_fitness = sum(fitness for fitness, individual in fitness_scores)

        # Calculate the relative fitness of each individual
        relative_fitness = [(fitness / total_fitness, individual) for fitness, individual in fitness_scores]

        # Sort the relative fitness scores in ascending order
        relative_fitness.sort(key=lambda x: x[0])

        # Generate cumulative probabilities
        cumulative_probs = [sum(fitness for fitness, individual in relative_fitness[:i+1]) for i in range(len(relative_fitness))]

        # Select individuals
        population_half = population_size // 2
        new_population = []
        for _ in range(population_half):
            rand = random.random()
            for i, individual in enumerate(relative_fitness):
                if rand <= cumulative_probs[i]:
                    new_population.append(individual[1])
                    break

        population = new_population

        # Create children by crossing over two random individuals
        children = []
        for individual in population:
            partner = random.choice(population)
            child = individual.__add__(partner)
            children.append(child)

        # Add the children to the population
        population.extend(children)
        # print(f"Population size after crossover: {len(population)}")
        
        # Mutate the population
        for individual in population:
            individual.mutate(0.1)
    
