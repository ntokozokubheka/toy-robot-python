import random

def save_obstacle_coordinates(data):
    with open("coordinates.txt", '+a') as file:
        for item in data:
            line = ','.join(map(str, item)) + '\n'
            file.write(line)

def create_random_obstacles(max):
    obstacle_coordinates = []
    num_obstacles = random.randint(1, max)
    for i in range(num_obstacles):
        position_x = random.randint(-100, 100)
        position_y = random.randint(-100, 100)
        if position_x == 0 and position_y == 0 or is_position_blocked(position_x, position_y):
            position_x = random.randint(-100, 100)
            position_y = random.randint(-100, 100)
        obstacle_coordinates.append((position_x, position_y))

    return obstacle_coordinates

def is_position_blocked(robot_x, robot_y):
    obstacle_coordinates = get_obstacles()
    if (obstacle_coordinates == []):
        return False
    robot = (robot_x, robot_y, 2, 2)
    for coordinate in obstacle_coordinates:
        obstacle = (coordinate[0], coordinate[1], 4, 4)
        if check_collision(robot, obstacle):
            return True
    return False


def is_path_blocked(x1, y1, x2, y2):
    obstacle_coordinates = get_obstacles()
    if (obstacle_coordinates == []):
        return False
    dx = 1 if x2 > x1 else -1 if x2 < x1 else 0
    dy = 1 if y2 > y1 else -1 if y2 < y1 else 0

    x, y = x1, y1
    while x != x2 or y != y2:
        if is_position_blocked(x, y):
            return True
        x += dx
        y += dy
    return False


def get_obstacles():
    data = []
    with open("coordinates.txt", 'r') as file:
        for line in file:
            # Assuming the tuples are separated by commas
            items = line.strip().split(',')
            # Convert each item to its appropriate data type
            data.append(tuple(map(eval, items)))
    return data


def check_collision(robot, obstacle):
    return (robot[0] < obstacle[0] + obstacle[2] and
            robot[0] + robot[2] > obstacle[0] and
            robot[1] < obstacle[1] + obstacle[3] and
            robot[1] + robot[3] > obstacle[1])
