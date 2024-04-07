import sys
import import_helper


def clear_file():
    with open("coordinates.txt", 'w') as file:
        file.write('')

def robot_start():
    clear_file()
    try:
        obstacles = import_helper.dynamic_import('maze.obstacles')
        obstacles.save_obstacle_coordinates(
                obstacles.create_random_obstacles(10))
    except ImportError:
        print(f"Error: Could not import module maze obstacles")
    
    try:
        game_text = import_helper.dynamic_import(
            'world.text.start_game')
        game_text.robot_start()
    except ImportError:
        print(f"Error: Could not import text game")

def robot_start_argv():
    if (sys.argv[1] == "text" or sys.argv[1] == "turtle" or sys.argv[1] == ""):
        if sys.argv[1] == "text" or sys.argv[1] == "":
            try:
                game_text = import_helper.dynamic_import(
                    'world.text.start_game')
                game_text.robot_start()
            except ImportError:
                print(f"Error: Could not import text game")

        if sys.argv[1] == "turtle":
            try:
                game_graphical = import_helper.dynamic_import(
                    'world.text.start_game')
                game_graphical.robot_start()
            except ImportError:
                print(f"Error: Could not import default graphical game")


def import_controls():
    if len(sys.argv) == 2 and (sys.argv[1] == "text" or sys.argv[1] == "turtle"):
        try:
            obstacles = import_helper.dynamic_import('maze.obstacles')
            obstacles.save_obstacle_coordinates(
                obstacles.create_random_obstacles(20))
            print("loaded default")
        except ImportError:
            print(f"Error: Could not import module maze obstacles")

    elif len(sys.argv) == 3 and sys.argv[2] == "simple_maze":
        try:
            obstacles = import_helper.dynamic_import('maze.simple_maze')
            obstacles.create_maze()

        except ImportError:
            print(f"Error: Could not import module simple_maze")


if __name__ == "__main__":
    clear_file()
    import_controls()
    robot_start_argv()
