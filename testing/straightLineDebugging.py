#!/usr/bin/env python3
import math
from ev3dev2 import LargeMotor, OUTPUT_A, OUTPUT_C, MoveTank,MoveDifferential
from ev3dev2 import Wheel
from ev3dev2 import Display

from ev3dev2 import Button
from ev3dev2 import EV3Tire
from ev3dev2 import GyroSensor
btn = Button()
disp = Display()
left = LargeMotor(OUTPUT_A)
right = LargeMotor(OUTPUT_C)
myWheel = Wheel(diameter_mm=68.88, width_mm=  45)
countsPerRotLM =360
wheelDiameterMM=68.88
wheelCir = wheelDiameterMM*math.pi
#dont foget its in cm
Length = 90
Laps = 4
drive = MoveTank(OUTPUT_A,OUTPUT_C)
odoDrive = MoveDifferential(OUTPUT_A,OUTPUT_C,EV3Tire, 154.5)
gyro = GyroSensor()
gyro.reset()
#odoDrive.gyro= gyro
odoDrive.wheel = Wheel(56,27)
odoDrive.odometry_start()
odoDrive.gyro=gyro
odoDrive.on_to_coordinates(30,0,150*25.4)
print(str(odoDrive.x_pos_mm)+" "+str(odoDrive.y_pos_mm)+" "+str(math.degrees(odoDrive.theta))+" \n")
odoDrive.on_to_coordinates(30,0,150*25.4)
odoDrive.turn_to_angle(30,90)
