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
# variable that defines whether the robot has reached the block
col = False
# variable that defines whether the arm is lowered or not
lowered = False
distanceDriven = 0
motorSpeed = 200
motorTarget = 0
block_sensor = UltrasonicSensor(Port.S4)
armMotor = Motor(Port.A)
leftMotor = Motor(Port.B)
rightMotor = Motor(Port.C)
Ev3 = DriveBase(leftMotor, rightMotor, wheel_diameter=55.5, axle_track=104)

def Arm(angle):
    armMotor.run_target(speed=motorSpeed, target_angle= angle)
    
def Return():
    Ev3.straight(-distanceDriven / 2)
    Arm(0)
            
# Execute
while lowered == False:
    while block_sensor.distance() > 90 and col == False:
        Ev3.drive(motorSpeed, motorTarget)
        distanceDriven = distanceDriven + 0.5
    else:
        col = True
    if col == True:
        Arm(-155)
        lowered = True
        Return()
