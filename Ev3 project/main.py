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
distanceDriven = 0
motorSpeed = 900
motorTarget = 0
armMotor = Motor(Port.A)

def Arm():
    armMotor.run_target(speed=motorSpeed, target_angle= 99999)
 
 
while True:
    Arm()