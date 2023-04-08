import driving_logic
import time
def action():
    robot = driving_logic.Robot()
    robot.drive_backwards(2)
    time.sleep(.2)
    robot.turn_left()