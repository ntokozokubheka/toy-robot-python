def output(name, message):
    print(''+name+": "+message)


def do_help():
    """
    Provides help information to the user
    :return: (True, help text) to indicate robot can continue after this command was handled
    """
    return True, """I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT - turn right by 90 degrees
LEFT - turn left by 90 degrees
SPRINT - sprint forward according to a formula
REPLAY - replays all movement commands from history [FORWARD, BACK, RIGHT, LEFT, SPRINT]
MAZERUN - this command will let the robot figure out what commands to use to get to the top of the screen.
"""

def display_obstacles(obstacles):
    if len(obstacles) > 0:
        print("HAL: Loaded obstacles.")
        print("There are some obstacles:")
        for obstacle in obstacles :
            print(f"- At position {obstacle[0]},{obstacle[1]} (to {obstacle[0]+4},{obstacle[1]+4})")
        
