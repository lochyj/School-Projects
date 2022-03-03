#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Initialize the EV3 brick
ev3 = EV3Brick()

# defining vars
motorSpeed = 100
leftMotor = Motor(Port.B)
rightMotor = Motor(Port.C)
Ev3 = DriveBase(leftMotor, rightMotor, wheel_diameter=55.5, axle_track=104)

def Arm(angle):
    armMotor.run_target(speed=motorSpeed, target_angle= angle)
    
def Return():
    Ev3.straight(-distanceDriven)
    Arm(0)

# directions function that take a string and returns a list of operations to be executed by the robot
def execute(directions):
    distanceDriven = 0
    # split the string into a list of strings
    directions = directions.split()
    # for each string in the list
    for direction in directions:
        # split the string into a list of strings
        direction = direction.split("(")
        # remove the remaining brackets
        direction[1] = direction[1].replace(")", "")
        # if the first string in the list is "left"
        if direction[0] == "left":
            # turn left
            Ev3.turn(-int(direction[1]))
            print(int(direction[1]))
        # if the first string in the list is "right"
        elif direction[0] == "right":
            # turn right
            Ev3.turn(int(direction[1]))
            print(int(direction[1]))
        # if the first string in the list is "straight"
        elif direction[0] == "straight":
            # drive straight
            Ev3.straight(int(direction[1]))
            print(int(direction[1]))
        
    

# directions string

directions = "straight(700) right(20) straight(300) right(90) straight(450) left(120) straight(300)"


# Execute
if True: 
    execute()