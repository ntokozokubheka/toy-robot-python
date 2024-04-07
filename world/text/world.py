from maze.obstacles import is_position_blocked, is_path_blocked

if 'position_x' not in globals():
    position_x = 0

if 'position_y' not in globals():
    position_y = 0


directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0

# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100


def get_x():
    return position_x

def get_y():
    return position_y

def update_x(x):
    global position_x
    position_x = x

def update_x(y):
    global position_y
    position_y = y


def update_index(i):
    global current_direction_index

    current_direction_index = i


def show_position(robot_name):
    print(' > '+robot_name+' now at position (' +
          str(position_x)+','+str(position_y)+').')


def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """

    return min_x <= new_x <= max_x and min_y <= new_y <= max_y


def update_position(steps):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    """

    global position_x, position_y
    new_x = position_x
    new_y = position_y

    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
    elif directions[current_direction_index] == 'right':
        new_x = new_x + steps
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
    elif directions[current_direction_index] == 'left':
        new_x = new_x - steps

   # if is_position_blocked(new_x, new_y) or is_path_blocked(position_x, position_y, new_x, new_y):
    #    print("obstacle found")
     #   return False
    if is_position_allowed(new_x, new_y):

        position_x = new_x
        position_y = new_y
        return True
    return False
