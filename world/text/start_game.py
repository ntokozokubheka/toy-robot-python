from world.text import display_utils
from world.text import validation_command as handle_commands
from world.text import world
from maze import obstacles

def robot_start():
    """This is the entry point for starting my robot"""

    robot_name = handle_commands.get_robot_name()
    display_utils.output(robot_name, "Hello kiddo!")
    display_utils.display_obstacles(obstacles.get_obstacles())
    world.position_x = 0
    world.position_y = 0
    world.current_direction_index = 0
    handle_commands.history = []

    command = handle_commands.get_command(robot_name)
    while handle_commands.handle_command(robot_name, command):
        command = handle_commands.get_command(robot_name)

    display_utils.output(robot_name, "Shutting down..")
