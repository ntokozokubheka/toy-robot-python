from world.text import display_utils
from helpers.validation_utils import is_int
from world.text import robot_movements as move_robot
from world.text import world as robot_world
from world.text import replay_commands as replay
from maze import mazerun_commands

# commands history
history = []

valid_commands = ['off', 'help', 'replay', 'forward',
                  'back', 'right', 'left', 'sprint', 'mazerun']
move_commands = valid_commands[3:]


def get_robot_name():
    name = input("What do you want to name your robot? ")
    while len(name) == 0:
        name = input("What do you want to name your robot? ")
    return name


def get_command(robot_name):
    """
    Asks the user for a command, and validate it as well
    Only return a valid command
    """

    prompt = ''+robot_name+': What must I do next? '
    command = input(prompt)
    while len(command) == 0 or not valid_command(command):
        display_utils.output(
            robot_name, "Sorry, I did not understand '"+command+"'.")
        command = input(prompt)

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

    elif command_name.lower() == 'mazerun':
        if len(arg1.strip()) == 0:
            return True
        if arg1.lower().find('top') > -1 or arg1.lower().find('bottom') > -1 or arg1.lower().find('left') > -1 or arg1.lower().find('right') > -1:
            return True

    else:
        return command_name.lower() in valid_commands and (len(arg1) == 0 or is_int(arg1))


def call_command(command_name, command_arg, robot_name):
    if command_name == 'help':
        return display_utils.do_help()
    elif command_name == 'mazerun':
        mazerun_commands.processes_command(robot_name, command_arg)
        
    elif command_name == 'forward':
        return move_robot.do_forward(robot_name, int(command_arg))
    elif command_name == 'back':
        return move_robot.do_back(robot_name, int(command_arg))
    elif command_name == 'right':
        return move_robot.do_right_turn(robot_name)
    elif command_name == 'left':
        return move_robot.do_left_turn(robot_name)
    elif command_name == 'sprint':
        return move_robot.do_sprint(robot_name, int(command_arg))
    elif command_name == 'replay':
        return replay.do_replay(robot_name, command_arg)
    return False, None


def handle_command(robot_name, command):
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
        (do_next, command_output) = call_command(command_name, arg, robot_name)

    print(command_output)
    robot_world.show_position(robot_name)
    add_to_history(command)

    return do_next


def add_to_history(command):
    """
    Adds the command to the history list of commands
    :param command:
    :return:
    """
    history.append(command)
