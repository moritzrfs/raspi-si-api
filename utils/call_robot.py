import utils.driving_logic as driving_logic
import time

stop_flag = False

def action():
    robot = driving_logic.Robot()
    print("Robot started.")
    robot.execute_instructions('tmp/driving_instructions/instructions.json')
    print("Robot stopped.")
