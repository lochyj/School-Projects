#!/usr/bin/env pybricks-micropython
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
a = 1
motorSpeed = 200
motorTarget = 100
distanceSensor = ''
leftMotor = Motor(Port.B)
rightMotor = Motor(Port.C)
Ev3Drive = DriveBase(leftMotor, rightMotor, wheel_diameter=55.5, axle_track=104)


# Execute
if a == 1:
    Ev3Drive.straight(1000)
    Ev3Drive.straight(-1000)