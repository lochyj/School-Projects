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
col = False
lowered = False
distanceDriven = 0
motorSpeed = 100
block_sensor = UltrasonicSensor(Port.S4)
armMotor = Motor(Port.A)
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
    # split the string into a list of strings
    directions = directions.split()
    # for each string in the list
    for direction in directions:
        # split the string into a list of strings
        direction = direction.split("(")
        # remove the remaining brackets
        direction[1] = direction[1].replace(")", "")
        # check for block_sensor.distance() > 70 and col == False
        if block_sensor.distance() > 70 and col == False
            # if the first string in the list is "left"
            if direction[0] == "left":
                # turn left
                # Ev3.turn(-int(direction[1]))
                print(int(direction[1]))
            # if the first string in the list is "right"
            elif direction[0] == "right":
                # turn right
                # Ev3.turn(int(direction[1]))
                print(int(direction[1]))
            # if the first string in the list is "straight"
            elif direction[0] == "straight":
                # drive straight
                print(int(direction[1]))
                # Ev3.straight(int(direction[1]))
                distanceDriven += int(direction[1])
            

# Execute
while lowered == False:
    while block_sensor.distance() > 70 and col == False:
        execute(directions)
    else:
        col = True
    if col == True:
        Arm(-155)
        lowered = True
        Return()