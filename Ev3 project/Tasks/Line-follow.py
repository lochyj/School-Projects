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

# defining variables
motorSpeed = 100
motorTarget = 0
line_sensor = ColorSensor(Port.S1)
leftMotor = Motor(Port.B)
rightMotor = Motor(Port.C)
Ev3 = DriveBase(leftMotor, rightMotor, wheel_diameter=55.5, axle_track=104)
# defining what is black and white, measures the reflectivity of a surface based on its colour.
BLACK = 9
WHITE = 30
threshold = (BLACK + WHITE) / 2
PROPORTIONAL_GAIN = 2.1


# Execute
while True:
    deviation = line_sensor.reflection() - threshold
    turn_rate = PROPORTIONAL_GAIN * deviation
    Ev3.drive(motorSpeed, turn_rate)
    wait(10)
