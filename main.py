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
motorSpeed = 200
motorTarget = 0
line_sensor = ColorSensor(Port.S1)
leftMotor = Motor(Port.B)
rightMotor = Motor(Port.C)
Ev3 = DriveBase(leftMotor, rightMotor, wheel_diameter=55.5, axle_track=104)
BLACK = 9
WHITE = 30
threshold = (BLACK + WHITE) / 2
PROPORTIONAL_GAIN = 3.4


# Execute
while True:
    deviation = line_sensor.reflection() - threshold
    turn_rate = PROPORTIONAL_GAIN * deviation
    Ev3.drive(motorSpeed, turn_rate)
    wait(5)