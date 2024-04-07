import random

from maze.obstacles import get_obstacles
from world.text import robot_movements
from world.text import world


class RandomMouse:
    def __init__(self, environment):
        self.environment = environment
        self.position = (0, 0)

    def move_randomly(self):
        possible_moves = ["forward", "back", "left", "right"]
        return random.choice(possible_moves)

    def is_valid_move(self, move):

        new_position = self.calculate_new_position(move)
        return (
            self.environment.is_within_boundaries(new_position) and
            not self.environment.is_obstacle(new_position)
        )

    def calculate_new_position(self, move):
        x, y = self.position
        if move == "forward":
            display_this = robot_movements.do_forward("HAL", 1)
            print(display_this[1])
            return (world.get_x(), world.get_y())
        elif move == "back":
            display_this = robot_movements.do_forward("HAL", 1)
            print(display_this[1])
            return (world.get_x(), world.get_y())
        elif move == "left":
            display_this = robot_movements.do_left_turn("HAL")
            print(display_this[1])
            return (world.get_x(), world.get_y())
        elif move == "right":
            display_this = robot_movements.do_right_turn("HAL")
            print(display_this[1])
            return (world.get_x(), world.get_y())

    def make_move(self, move):
        if self.is_valid_move(move):
            self.position = self.calculate_new_position(move)

    def run(self):
        print("starting maze run..")
        while not self.environment.is_goal(self.position):
            random_move = self.move_randomly()
            self.make_move(random_move)


class ExampleEnvironment:

    def __init__(self, width, height, destination_x,destination_y):
        self.width = width
        self.height = height
        self.destination_x = destination_x
        self.destination_y= destination_y
        self.obstacles = set(get_obstacles())

    def is_within_boundaries(self, position):
        x, y = position
        return -self.width <= x < self.width and -self.height <= y < self.height

    def is_obstacle(self, position):
        return position in self.obstacles

    def is_goal(self, position):
        return position == (self.destination_x, self.destination_y)