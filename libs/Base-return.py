#!/usr/bin/env pybricks-micropython
# Importing the nessacary libraries
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Initialize the EV3 brick
ev3 = EV3Brick()

# defining vars
# a is here to fix the bug
a = 1
# the speed that the motor spins at (not needed for this scenario but it is good to have)
motorSpeed = 200
# MotorTarget is the target position of the motor in mm
motorTarget = 300
# Defining the motor ports
leftMotor = Motor(Port.B)
rightMotor = Motor(Port.C)
# Ev3Drive is the function that makes the robot drive 
# This also isnt nessacary but it help with the readability of the code
Ev3Drive = DriveBase(leftMotor, rightMotor, wheel_diameter=55.5, axle_track=104)


# Execute
# There is a weird bug that makes the robot not respond unless it is in a while or if statement
if a == 1:
    # Drive straight for 300mm
    Ev3Drive.straight(300)
    # turn 90 degrees
    Ev3Drive.turn(90)
    # Drive straight for 300mm
    Ev3Drive.straight(300)
    # turn 90 degrees
    Ev3Drive.turn(90)
    # Drive straight for 300mm
    Ev3Drive.straight(300)
    # turn 90 degrees
    Ev3Drive.turn(90)
    # Drive straight for 300mm
    Ev3Drive.straight(300)
    # turn 90 degrees
    Ev3Drive.turn(90)
    # Drive straight for 300mm
    Ev3Drive.straight(300)