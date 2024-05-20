# This Python script is used to run a snake game with human control. 
# It first imports the necessary classes, then creates instances of the SnakeGame 
# and HumanController classes. The game is then started with the run method.

#!/usr/bin/env python

# Import the SnakeGame class from the snake module
from snake import SnakeGame
# Import the HumanController class from the game_controller module
from game_controller import HumanController

# This condition checks if this script is being run directly and not imported as a module
if __name__ == '__main__':
    # Create an instance of SnakeGame
    game = SnakeGame()
    # Create an instance of HumanController with the game instance as an argument
    controller = HumanController(game)
    # Start running the game
    game.run()