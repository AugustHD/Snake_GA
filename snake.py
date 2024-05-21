# This Python code defines a snake game. 
# The SnakeGame class controls the game logic, 
# the Food class represents the food in the game, 
# and the Snake class represents the snake. 
# The game is run until the snake crashes into the wall or hits its own tail. 
# The snake's score increases when it eats food, and its length also increases. 
# The positions of all segments of the snake's body can be printed for debugging.

import random
from collections import deque
from typing import Protocol
import pygame
from vector import Vector
from game_controller import HumanController

# Define a class for the snake game
class SnakeGame:
    # Initialize the game with a grid size and scale
    def __init__(self, xsize: int=30, ysize: int=30, scale: int=15):
        self.grid = Vector(xsize, ysize)
        self.scale = scale
        self.snake = Snake(game=self)
        self.food = Food(game=self)
        self.movements = 0

    # Run the game until the snake crashes or hits its own tail
    def run(self):
        running = True
        while running:
            next_move = self.controller.update()
            if next_move: self.snake.v = next_move
            self.snake.move()
            self.movements += 1 
            if not self.snake.p.within(self.grid):
                running = False
                message = 'Game over! You crashed into the wall!'
            if self.snake.cross_own_tail:
                running = False
                message = 'Game over! You hit your own tail!'
            if self.snake.p == self.food.p:
                self.snake.add_score()
                self.food = Food(game=self)
        print(f'{message} ... Score: {self.snake.score}')

# Define a class for the food in the game
class Food:
    # Initialize the food with a random position within the game grid
    def __init__(self, game: SnakeGame):
        self.game = game
        self.p = Vector.random_within(self.game.grid)

# Define a class for the snake in the game
class Snake:
    # Initialize the snake with a random position within the game grid
    def __init__(self, *, game: SnakeGame):
        self.game = game
        self.score = 0
        self.v = Vector(0, 0)
        self.body = deque()
        self.body.append(Vector.random_within(self.game.grid))

    # Move the snake in the direction of its velocity
    def move(self):
        self.p = self.p + self.v

    # Check if the snake has crossed its own tail
    @property
    def cross_own_tail(self):
        try:
            self.body.index(self.p, 1)
            return True
        except ValueError:
            return False

    # Get the position of the snake's head
    @property
    def p(self):
        return self.body[0]

    # Set the position of the snake's head and remove the last segment of its tail
    @p.setter
    def p(self, value):
        self.body.appendleft(value)
        self.body.pop()

    # Increase the snake's score and length when it eats food
    def add_score(self):
        self.score += 1
        tail = self.body.pop()
        self.body.append(tail)
        self.body.append(tail)

    # Print the positions of all segments of the snake's body for debugging
    def debug(self):
        print('===')
        for i in self.body:
            print(str(i))