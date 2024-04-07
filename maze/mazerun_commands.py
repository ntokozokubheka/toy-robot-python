from maze import maze_run


def run_to_top(robot_name):

    environment = maze_run.ExampleEnvironment(
        width=52, height=52, destination_x=0, destination_y=52)
    random_mouse = maze_run.RandomMouse(environment)
    random_mouse.run()
    print(f"{robot_name}: I am at the top edge.")


def run_to_bottom(robot_name):

    environment = maze_run.ExampleEnvironment(
        width=52, height=52, destination_x=0, destination_y=-52)
    random_mouse = maze_run.RandomMouse(environment)
    random_mouse.run()
    print(f"{robot_name}: I am at the bottom edge.")


def run_to_left(robot_name):

    environment = maze_run.ExampleEnvironment(
        width=52, height=52, destination_x=-52, destination_y=0)
    random_mouse = maze_run.RandomMouse(environment)
    random_mouse.run()
    print(f"{robot_name}: I am at the left edge.")


def run_to_right(robot_name):

    environment = maze_run.ExampleEnvironment(
        width=52, height=52, destination_x=50, destination_y=0)
    random_mouse = maze_run.RandomMouse(environment)
    random_mouse.run()
    print(f"{robot_name}: I am at the right edge.")


def processes_command(robot_name, command):
    if command == "" or command == "top":
        run_to_top(robot_name)
    if command == "bottom":
        run_to_bottom(robot_name)
    if command == "left":
        run_to_left(robot_name)
    if command == "right":
        run_to_right(robot_name)
