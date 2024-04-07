from world.text import display_utils
from world.text import validation_command as handle_commands
from world.text import world
from maze import obstacles
from maze import mazerun_commands
import random

print("HAL: Loaded simple_maze.")


def create_random_obstacles():
    obstacle_coordinates = []
    not_allowed = [0, 1, 2, 3, 4, -1, -2, -3, -4,]
    num_obstacles = random.randint(200, 1000)
    for i in range(num_obstacles):
        position_x = random.randint(-48, 48)
        position_y = random.randint(-48, 48)
        if position_x in not_allowed or position_y in not_allowed or obstacles.is_position_blocked(position_x, position_y):
            position_x = random.randint(-48, 48)
            position_y = random.randint(-48, 48)
        obstacle_coordinates.append((position_x, position_y))

    return obstacle_coordinates


def clear_file(filename):
    with open(filename, 'w') as file:
        file.truncate(0)


def create_perimeter():
    obstacle_coordinates = []
    # __
    for i in range(4, 53, 4):
        position_x = i
        position_y = -52
        obstacle_coordinates.append((position_x, position_y))

    # ___
    for i in range(-4, -53, -4):
        position_x = i
        position_y = -52
        obstacle_coordinates.append((position_x, position_y))

    # |__
    for i in range(-53, -4, 4):
        position_x = -52
        position_y = i
        obstacle_coordinates.append((position_x, position_y))

    # third  quadrant perimeter |__
    for i in range(4, 53, 4):
        position_x = -52
        position_y = i
        obstacle_coordinates.append((position_x, position_y))

      # fourth quadrant perimeter  __
    for i in range(-53, -4, 4):
        position_x = i
        position_y = 52
        obstacle_coordinates.append((position_x, position_y))

    # third quadrant perimeter __|
    for i in range(4, 53, 4):
        position_x = i
        position_y = 52
        obstacle_coordinates.append((position_x, position_y))

    # third  quadrant perimeter |_
    for i in range(53, 4, -4):
        position_x = 52
        position_y = i
        obstacle_coordinates.append((position_x, position_y))

    # third  quadrant perimeter |_
    for i in range(-4, -53, -4):
        position_x = 52
        position_y = i
        obstacle_coordinates.append((position_x, position_y))

    return obstacle_coordinates


def add_edges():
    obstacles.save_obstacle_coordinates(create_perimeter())


def create_maze():

    add_edges()
    obstacles.save_obstacle_coordinates(create_random_obstacles())
