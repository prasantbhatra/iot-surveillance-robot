# IoT Robot Motor Control - Raspberry Pi GPIO
# Author: Prasant Bhatra
import RPi.GPIO as GPIO
import time

# Motor Pins
LEFT_FORWARD = 17
LEFT_BACKWARD = 18
RIGHT_FORWARD = 22
RIGHT_BACKWARD = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup([LEFT_FORWARD, LEFT_BACKWARD, RIGHT_FORWARD, RIGHT_BACKWARD], GPIO.OUT)

def move_forward():
    GPIO.output(LEFT_FORWARD, True)
    GPIO.output(RIGHT_FORWARD, True)
    GPIO.output(LEFT_BACKWARD, False)
    GPIO.output(RIGHT_BACKWARD, False)
    print("Moving Forward")

def move_backward():
    GPIO.output(LEFT_BACKWARD, True)
    GPIO.output(RIGHT_BACKWARD, True)
    GPIO.output(LEFT_FORWARD, False)
    GPIO.output(RIGHT_FORWARD, False)
    print("Moving Backward")

def stop_robot():
    GPIO.output(LEFT_FORWARD, False)
    GPIO.output(LEFT_BACKWARD, False)
    GPIO.output(RIGHT_FORWARD, False)
    GPIO.output(RIGHT_BACKWARD, False)
    print("Robot Stopped")

# Test run
if __name__ == "__main__":
    try:
        move_forward()
        time.sleep(2)
        stop_robot()
    finally:
        GPIO.cleanup()
