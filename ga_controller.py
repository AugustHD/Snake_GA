# This Python code defines a class GAController that inherits from GameController. 
# It is used to control a game, possibly with a graphical display. 
# The update method is used to update the game state and return the next move. 
# The block method returns a tuple representing the position and size of a block.

from typing import Protocol
from vector import Vector
import pygame
from game_controller import GameController

# GAController is a class that inherits from GameController
class GAController(GameController):
    # The constructor initializes the game, display, and other properties
    def __init__(self, game, display=False, model=None):
        self.display = display
        self.game = game
        self.game.controller = self
        self.model = model
        if self.display:
            pygame.init()
            self.screen = pygame.display.set_mode((game.grid.x * game.scale, game.grid.y * game.scale))
            self.clock = pygame.time.Clock()
            self.color_snake_head = (0, 255, 0)
            self.color_food = (255, 0, 0)
            self.action_space = (Vector(0, -1), Vector(0, 1), Vector(1, 0), Vector(-1, 0))

    # Destructor to quit pygame when the object is deleted
    def __del__(self):
        if self.display:
            pygame.quit()

    # update method to update the game state and return the next move
    def update(self) -> Vector:
        # observation space

        # delta north, east, south, west
        dn = self.game.snake.p.y
        de = self.game.grid.x - self.game.snake.p.x
        ds = self.game.grid.y - self.game.snake.p.y
        dw = self.game.snake.p.x

        # delta food x and y
        dfx = self.game.snake.p.x - self.game.food.p.x
        dfy = self.game.snake.p.y - self.game.food.p.y

        # score
        s = self.game.snake.score

        obs = (dn, de, ds, dw, dfx, dfy, s)

        # action space
        next_move = self.action_space[self.model.action(obs)]

        # display
        if self.display:
            self.screen.fill('black')
            for i, p in enumerate(self.game.snake.body):
                pygame.draw.rect(self.screen, (0, max(128, 255 - i * 12), 0), self.block(p))
            pygame.draw.rect(self.screen, self.color_food, self.block(self.game.food.p))
            pygame.display.flip()
            self.clock.tick(10)
        return next_move

    # block method to return a tuple representing the position and size of a block
    def block(self, obj):
        return (obj.x * self.game.scale,
                obj.y * self.game.scale,
                self.game.scale,
                self.game.scale)
