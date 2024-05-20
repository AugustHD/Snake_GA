# This Python script is used to run a snake game. 
# It first imports the necessary classes, then creates instances of the 
# SnakeGame and GAController classes. The game is then started with the run method.

#!/usr/bin/env python

# Import the SnakeGame class from the snake module
from snake import SnakeGame
# Import the GAController class from the ga_controller module
from ga_controller import GAController

# This condition checks if this script is being run directly and not imported as a module
if __name__ == '__main__':
    # Create an instance of SnakeGame
    game = SnakeGame()
    # Create an instance of GAController with the game instance as an argument
    controller = GAController(game)
    # Start running the game
    game.run()