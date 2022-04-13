#!/usr/bin/env python3
from ev3dev2.wheel import EV3Tire, Wheel
from ev3dev2.motor import LargeMotor, MoveTank,MoveDifferential,OUTPUT_A,OUTPUT_D
from ev3dev2.sensor.lego import GyroSensor
import time
left = LargeMotor(OUTPUT_A)
right = LargeMotor(OUTPUT_D)
right.on_for_rotations
myWheel = Wheel(diameter_mm=44.2, width_mm=  22)
drive = MoveTank(OUTPUT_A,OUTPUT_D)
odoDrive = MoveDifferential(OUTPUT_A,OUTPUT_D,EV3Tire, 158)
odoDrive.wheel=myWheel
gyro = GyroSensor()
centerBoxDist = 3
gyro.reset()
gyro.calibrate()
gyro.reset()
odoDrive.gyro=gyro
odoDrive.on_for_distance(-30,106*25.4)
while True:
    print(str(gyro.value()))