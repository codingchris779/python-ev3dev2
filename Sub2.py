#!/usr/bin/env python3
from ev3dev2.wheel import EV3Tire, Wheel
from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.motor import LargeMotor,MediumMotor, MoveTank,MoveDifferential,OUTPUT_A,OUTPUT_D
import time
mid = MediumMotor()
left = LargeMotor(OUTPUT_A)
right = LargeMotor(OUTPUT_D)
myWheel = Wheel(diameter_mm=44.2, width_mm=  22)
drive = MoveTank(OUTPUT_A,OUTPUT_D)
odoDrive = MoveDifferential(OUTPUT_A,OUTPUT_D,EV3Tire, 158.2)
odoDrive.wheel=myWheel
gyro = GyroSensor()
gyro.reset()
gyro.calibrate()
gyro.reset
odoDrive.on_for_distance(30,12*25.4)
odoDrive.turn_degrees(30,90)
odoDrive.turn_degrees(30,90-gyro.value())
print(str(gyro.value()))
odoDrive.on_for_distance(-30,106*25.4)
time.sleep(3)
odoDrive.turn_degrees(30,90)
odoDrive.turn_degrees(30,180-gyro.value())
print(str(gyro.value()))
odoDrive.on_for_distance(30,12*25.4)



