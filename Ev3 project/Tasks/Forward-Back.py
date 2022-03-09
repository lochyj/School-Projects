#!/usr/bin/env pybricks-micropython
# importing the necessary libraries for the code to run
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Initialize the EV3 brick
ev3 = EV3Brick()

# Defining the motor (output) ports
leftMotor = Motor(Port.B)
rightMotor = Motor(Port.C)

Ev3Drive = DriveBase(leftMotor, rightMotor, wheel_diameter=55.5, axle_track=104)


# Execute
# There is a weird bug that makes the robot not respond unless it is in a while or if statement
# Move forward 1000mm (100cm), then move backward 1000mm
if True:
    Ev3Drive.straight(1000)
    Ev3Drive.straight(-1000)
