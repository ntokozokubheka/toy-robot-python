from world.turtle import display_utils
from world.turtle import validation_command as handle_commands
from world.turtle.world_elements import set_world_obstacles
from maze import obstacles
import turtle


def draw_obstacle(x, y):
    turtle.penup()
    turtle.goto(x*4, y*4)
    turtle.pendown()
    turtle.begin_fill()

    for _ in range(4):
        turtle.forward(4)
        turtle.right(90)

    turtle.end_fill()


def robot_start():
    """This is the entry point for starting my robot"""
    turtle.speed(0)
    for obstacle in obstacles.get_obstacles():
        draw_obstacle(*obstacle)

    screen = turtle.Turtle()
    box = turtle.Turtle()

    box.penup()
    box.hideturtle()
    box.color("black")
    box.hideturtle()

    screen_width = turtle.window_width()
    screen_height = turtle.window_height()

    box_start_x = screen_width / 2 - 150
    box_start_y = screen_height / 2 - 50

    box.goto(box_start_x, box_start_y)

    box.pendown()
    box.forward(300)
    box.right(90)
    box.forward(100)
    box.right(90)
    box.forward(300)
    box.right(90)
    box.forward(100)

    robot = turtle.Turtle()
    robot.penup()
    robot.clear()
    robot.color("blue")
    robot.left(90)

    robot_name = handle_commands.get_robot_name()
    display_utils.output(robot_name, "Hello kiddo!", box)

    position_x = 0
    position_y = 0
    current_direction_index = 0
    history = []

    command = handle_commands.get_command(robot_name, box)
    while handle_commands.handle_command(robot_name, command, box, robot):
        command = handle_commands.get_command(robot_name, box)

    display_utils.output(robot_name, "Shutting down..", box)
    turtle.done()
