import utils.driving_logic as driving_logic
import time

stop_flag = False

def action():
    robot = driving_logic.Robot()
    robot.execute_instructions('instructions.json')
    while True:
        if stop_flag:
            print("Stopping robot")
            robot.cleanup()
            break
        time.sleep(0.1)
