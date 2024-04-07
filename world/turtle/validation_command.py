from world.turtle import display_utils
from helpers.validation_utils import is_int
from world.turtle import robot_movements as move_robot
from world.turtle import world as robot_world
from world.turtle import replay_commands as replay
import turtle


if 'history' not in globals():
    history = []


valid_commands = ['off', 'help', 'replay',
                  'forward', 'back', 'right', 'left', 'sprint']
move_commands = valid_commands[3:]


def get_robot_name():
    name = turtle.textinput(
        "Robot Name", "What do you want to name your robot? ")
    while len(name) == 0:
        name = turtle.textinput(
            "Robot Name", "What do you want to name your robot? ")
    return name


def get_command(robot_name, box):
    """
    Asks the user for a command, and validate it as well
    Only return a valid command
    """
    prompt = ''+robot_name+': What must I do next? '
    command = turtle.textinput("Robot command", prompt)
    while len(command) == 0 or not valid_command(command):
        display_utils.output(
            robot_name, "Sorry, I did not understand '"+command+"'.", box)
        command = turtle.textinput("Robot command", prompt)

    return command.lower()


def split_command_input(command):
    """
    Splits the string at the first space character, to get the actual command, as well as the argument(s) for the command
    :return: (command, argument)
    """
    args = command.split(' ', 1)
    if len(args) > 1:
        return args[0], args[1]
    return args[0], ''


def valid_command(command):
    """
    Returns a boolean indicating if the robot can understand the command or not
    Also checks if there is an argument to the command, and if it a valid int
    """

    (command_name, arg1) = split_command_input(command)

    if command_name.lower() == 'replay':
        if len(arg1.strip()) == 0:
            return True
        elif (arg1.lower().find('silent') > -1 or arg1.lower().find('reversed') > -1) and len(arg1.lower().replace('silent', '').replace('reversed', '').strip()) == 0:
            return True
        else:
            range_args = arg1.replace('silent', '').replace('reversed', '')
            if is_int(range_args):
                return True
            else:
                range_args = range_args.split('-')
                return is_int(range_args[0]) and is_int(range_args[1]) and len(range_args) == 2
    else:
        return command_name.lower() in valid_commands and (len(arg1) == 0 or is_int(arg1))


def call_command(command_name, command_arg, robot_name, robot):
    if command_name == 'help':
        return display_utils.do_help()
    elif command_name == 'forward':
        return move_robot.do_forward(robot_name, int(command_arg), robot)
    elif command_name == 'back':
        return move_robot.do_back(robot_name, int(command_arg), robot)
    elif command_name == 'right':
        return move_robot.do_right_turn(robot_name, robot)
    elif command_name == 'left':
        return move_robot.do_left_turn(robot_name, robot)
    elif command_name == 'sprint':
        return move_robot.do_sprint(robot_name, int(command_arg), robot)
    elif command_name == 'replay':
        return replay.do_replay(robot_name, command_arg, robot)
    return False, None


def handle_command(robot_name, command, box, robot):
    """
    Handles a command by asking different functions to handle each command.
    :param robot_name: the name given to robot
    :param command: the command entered by user
    :return: `True` if the robot must continue after the command, or else `False` if robot must shutdown
    """

    (command_name, arg) = split_command_input(command)

    if command_name == 'off':
        return False
    else:
        (do_next, command_output) = call_command(
            command_name, arg, robot_name, robot)

    # print(command_output)
    robot_world.show_position(robot_name, box)
    add_to_history(command)

    return do_next


def add_to_history(command):
    """
    Adds the command to the history list of commands
    :param command:
    :return:
    """
    history.append(command)
    
    