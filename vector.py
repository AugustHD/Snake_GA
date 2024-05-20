# This Python code defines a Vector class for 2D vectors. 
# It includes methods for vector addition, checking if a vector is within a certain scope, 
# checking if two vectors are equal, and generating a random vector within a certain scope.

import random

# Define a class for 2D vectors
class Vector:
    # Initialize the vector with x and y coordinates
    def __init__(self, x: int=0, y: int=0):
        self.x = x
        self.y = y

    # Define a string representation for the vector
    def __str__(self):
        return f'Vector({self.x}, {self.y})'

    # Define vector addition
    def __add__(self, other: 'Vector') -> 'Vector':
        return Vector(self.x + other.x, self.y + other.y)

    # Check if the vector is within a certain scope
    def within(self, scope: 'Vector') -> 'Vector':
        return self.x <= scope.x and self.x >= 0 and self.y <= scope.y and self.y >= 0

    # Check if two vectors are equal
    def __eq__(self, other: 'Vector') -> bool:
        return self.x == other.x and self.y == other.y

    # Generate a random vector within a certain scope
    @classmethod
    def random_within(cls, scope: 'Vector') -> 'Vector':
        return Vector(random.randint(0, scope.x - 1), random.randint(0, scope.y - 1))import random


class Vector:
    def __init__(self, x: int=0, y: int=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Vector({self.x}, {self.y})'

    def __add__(self, other: 'Vector') -> 'Vector':
        return Vector(self.x + other.x, self.y + other.y)

    def within(self, scope: 'Vector') -> 'Vector':
        return self.x <= scope.x and self.x >= 0 and self.y <= scope.y and self.y >= 0

    def __eq__(self, other: 'Vector') -> bool:
        return self.x == other.x and self.y == other.y

    @classmethod
    def random_within(cls, scope: 'Vector') -> 'Vector':
        return Vector(random.randint(0, scope.x - 1), random.randint(0, scope.y - 1))
