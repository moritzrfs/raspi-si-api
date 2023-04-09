import utils.driving_logic as driving_logic
import time
def action():
    robot = driving_logic.Robot()
    robot.execute_instructions('instructions.json')