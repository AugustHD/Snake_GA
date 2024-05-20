# This Python code defines a protocol GameController 
# and a class HumanController that implements this protocol. 
# The HumanController class is used to control a game with human input. 
# The update method is used to update the game state based on user input and 
# return the next move. The block method returns a tuple representing the 
# position and size of a block.

from typing import Protocol
from vector import Vector
import pygame

# Define a protocol for game controllers
class GameController(Protocol):
    # All game controllers must implement an update method that returns a Vector
    def update(self) -> Vector:
        pass

# Define a class for human-controlled games
class HumanController(GameController):
    # Initialize the game controller with a game instance
    def __init__(self, game):
        self.game = game
        self.game.controller = self
        pygame.init()
        # Set up the game display
        self.screen = pygame.display.set_mode((game.grid.x * game.scale, game.grid.y * game.scale))
        self.clock = pygame.time.Clock()
        # Define colors for the snake head and food
        self.color_snake_head = (0, 255, 0)
        self.color_food = (255, 0, 0)

    # Clean up when the controller is deleted
    def __del__(self):
        pygame.quit()

    # Update the game state based on user input
    def update(self) -> Vector:
        next_move = None
        # Process all events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                # Update the next move based on the key pressed
                if event.key == pygame.K_LEFT:
                    next_move = Vector(-1, 0)
                if event.key == pygame.K_RIGHT:
                    next_move = Vector(1, 0)
                if event.key == pygame.K_UP:
                    next_move = Vector(0, -1)
                if event.key == pygame.K_DOWN:
                    next_move = Vector(0, 1)
        # Update the display
        self.screen.fill('black')
        for i, p in enumerate(self.game.snake.body):
            pygame.draw.rect(self.screen, (0, max(128, 255 - i * 12), 0), self.block(p))
        pygame.draw.rect(self.screen, self.color_food, self.block(self.game.food.p))
        pygame.display.flip()
        self.clock.tick(10)
        return next_move

    # Define a method to calculate the position and size of a block
    def block(self, obj):
        return (obj.x * self.game.scale,
                obj.y * self.game.scale,
                self.game.scale,
                self.game.scale)