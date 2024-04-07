from world.turtle import world as robot_world


def do_forward(robot_name, steps, robot):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    robot.forward(steps)
    if robot_world.update_position(steps):
        return True, ' > '+robot_name+' moved forward by '+str(steps)+' steps.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_back(robot_name, steps, robot):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    robot.back(steps)
    if robot_world.update_position(-steps):

        return True, ' > '+robot_name+' moved back by '+str(steps)+' steps.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_right_turn(robot_name, robot):
    """
    Do a 90 degree turn to the right
    :param robot_name:
    :return: (True, right turn output text)
    """
    robot.right(90)
    robot_world.current_direction_index += 1

    if robot_world.current_direction_index > 3:
        robot_world.current_direction_index = 0

    return True, ' > '+robot_name+' turned right.'


def do_left_turn(robot_name, robot):
    """
    Do a 90 degree turn to the left
    :param robot_name:
    :return: (True, left turn output text)
    """
    robot.left(90)
    robot_world.current_direction_index -= 1
    if robot_world.current_direction_index < 0:
        robot_world.current_direction_index = 3

    return True, ' > '+robot_name+' turned left.'


def do_sprint(robot_name, steps,robot):
    """
    Sprints the robot, i.e. let it go forward steps + (steps-1) + (steps-2) + .. + 1 number of steps, in iterations
    :param robot_name:
    :param steps:
    :return: (True, forward output)
    """

    if steps == 1:
        return do_forward(robot_name, 1)
    else:
        (do_next, command_output) = do_forward(robot_name, steps,robot)
        print(command_output)
        return do_sprint(robot_name, steps - 1,robot)