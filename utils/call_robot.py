import utils.driving_logic as driving_logic
import time

stop_flag = False

def action():
    robot = driving_logic.Robot()
    while not stop_flag:
        robot.execute_instructions('instructions.json')
    
    robot.cleanup()