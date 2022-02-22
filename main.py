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
motorSpeed = 100
motorTarget = 0
line_sensor = ColorSensor(Port.S1)
block_sensor = UltrasonicSensor(Port.S2)
leftMotor = Motor(Port.B)
rightMotor = Motor(Port.C)
Ev3 = DriveBase(leftMotor, rightMotor, wheel_diameter=55.5, axle_track=104)
GREY = 11
WHITE = 23
threshold = (GREY + WHITE) / 2
PROPORTIONAL_GAIN = 2.1


# Execute
while True:
    while block_sensor.distance() > 100:
        if line_sensor.reflection() >= threshold:
            Ev3.straight(20)
        else:
            Ev3.turn(-30)
    #Ev3.stop()
    #Ev3.straight(100)
