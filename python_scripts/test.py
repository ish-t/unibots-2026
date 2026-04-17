from gpiozero import Motor
from time import sleep


""" Change GPIO according to wiring. Standard values are given below for reference."""

# Motor A, Left wheel - IN1: 17, IN2: 27, ENA (Speed): 18
motor_left = Motor(forward=17, backward=27, enable=18)

# Motor B, Right wheel - IN3: 22, IN4: 23, ENB (Speed): 24
motor_right = Motor(forward=22, backward=23, enable=24)

def move_forward(speed=0.7):
    print(f"Moving forward at {speed * 100}% speed")
    motor_left.forward(speed)
    motor_right.forward(speed)

def turn_left(speed=0.6):
    print("Turning left")
    motor_left.backward(speed)
    motor_right.forward(speed)

def turn_right(speed=0.6):
    print("Turning right")
    motor_left.forward(speed)
    motor_right.backward(speed)

def stop_robot():
    print("Stopping")
    motor_left.stop()
    motor_right.stop()

if __name__ == "__main__":
    try:
        """ Test sequence: Move forward, turn left, then stop. Adjust timings as needed. """
        move_forward(speed=0.7)
        sleep(1)
        
        turn_left(speed=0.6)
        sleep(0.5)
        
        stop_robot()
        
    # Stop the robot by pressing Ctrl+C
    except KeyboardInterrupt:
        stop_robot()