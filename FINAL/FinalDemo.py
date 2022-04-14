#!/usr/bin/env python3
import math
from ev3dev2.button import Button
#from ClassStructure.Location import Location
from ev3dev2.wheel import EV3Tire, Wheel
from ev3dev2.motor import LargeMotor, MoveTank,MoveDifferential,OUTPUT_A,OUTPUT_D
from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.display import Display
import time
print("starting")
left = LargeMotor(OUTPUT_A)
screen = Display()
right = LargeMotor(OUTPUT_D)
button = Button()
right.on_for_rotations
myWheel = Wheel(diameter_mm=43.2, width_mm=  22)
drive = MoveTank(OUTPUT_A,OUTPUT_D)
odoDrive = MoveDifferential(OUTPUT_A,OUTPUT_D,EV3Tire, 156)
odoDrive.wheel=myWheel
gyro = GyroSensor()
centerBoxDist = 3
gyro.reset()
gyro.calibrate()
gyro.reset()
odoDrive.gyro=gyro
odoDrive.set_polarity(LargeMotor.POLARITY_INVERSED)
kP = 2
kI = 1.5
errorSum = 0
count = 0
odoDrive.odometry_start()
odoDrive.theta = math.radians(90)
odoDrive.x_pos_mm = 6*25.4
odoDrive.y_pos_mm = -6*25.4
#INPUTS
#barcode
barcode = 3
#isle is the isle up down 1-4
isle = 1 
#box 
box = 3

print("x - {0:.2f} y - {1:.2f} rotODO - {2:.2f} rotGyro {3}".format(odoDrive.x_pos_mm,odoDrive.y_pos_mm, math.degrees(odoDrive.theta),gyro.value()))
odoDrive.on_to_coordinates(30,6*25.4,(6+(24*isle))*25.4)
print("x - {0:.2f} y - {1:.2f} rotODO - {2:.2f} rotGyro {3}".format(odoDrive.x_pos_mm,odoDrive.y_pos_mm, math.degrees(odoDrive.theta),gyro.value()))
odoDrive.on_to_coordinates(30,6*25.4,(6+(24*isle))*25.4)
