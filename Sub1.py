#!/usr/bin/env python3
import math
from ClassStructure.Location import Location
from ev3dev2.wheel import EV3Tire, Wheel
from ev3dev2.motor import LargeMotor, MoveTank,MoveDifferential,OUTPUT_A,OUTPUT_D
from ev3dev2.sensor.lego import GyroSensor
import time
robot = Location()
left = LargeMotor(OUTPUT_A)
right = LargeMotor(OUTPUT_D)
right.on_for_rotations
myWheel = Wheel(diameter_mm=44.2, width_mm=  22)
drive = MoveTank(OUTPUT_A,OUTPUT_D)
odoDrive = MoveDifferential(OUTPUT_A,OUTPUT_D,EV3Tire, 158.2)
odoDrive.wheel=myWheel
gyro = GyroSensor()
centerBoxDist = 3
gyro.reset()
gyro.calibrate()
gyro.reset()
odoDrive.gyro=gyro
# odoDrive.on_for_distance(-30,38*25.4)
odoDrive.odometry_start()
odoDrive.on_for_distance(-30,38*25.4)
print(odoDrive.x_pos_mm)
kP = 2
kI = 1.5
errorSum = 0
count = 0
odoDrive.turn_degrees(30,90)
odoDrive.turn_degrees(30,90-gyro.value())

print(str(gyro.value()))

#odoDrive.turn_to_angle(30,180,use_gyro=True,error_margin=1)
while odoDrive.x_pos_mm>-(12+centerBoxDist)*25.4:
    count = count+1
    errorSum += 90-gyro.value()
    print(odoDrive.x_pos_mm)
    leftPow = -30 +(kP*(90-gyro.value())+(errorSum/count)*kI)
    rightPow = -30-(kP*(90-gyro.value())+(errorSum/count)*kI)
    if abs(leftPow)>95:
        if leftPow>rightPow:
            leftPow = 95
            rightPow = -95
        else:
            leftPow= -95
            rightPow = 95
    odoDrive.on(leftPow,rightPow)

print(odoDrive.x_pos_mm)
odoDrive.off()

errorSum=0
count=0
time.sleep(5)
odoDrive.turn_degrees(30,90-gyro.value())
print(str(gyro.value()))

#print(str(gyro.value()))
while odoDrive.x_pos_mm>-(96)*25.4:
    count = count+1
    errorSum += 90-gyro.value()
    print(odoDrive.x_pos_mm)
    leftPow = -30 +(kP*(90-gyro.value())+(errorSum/count)*kI)
    rightPow = -30-(kP*(90-gyro.value())+(errorSum/count)*kI)
    if abs(leftPow)>95:
        if leftPow>rightPow:
            leftPow = 95
            rightPow = -95
        else:
            leftPow= -95
            rightPow = 95
    odoDrive.on(leftPow,rightPow)

#odoDrive.on_for_distance(-30,(108-(12+centerBoxDist))*25.4)
odoDrive.off()
odoDrive.turn_degrees(30,90)
print(str(gyro.value()))
print(odoDrive.y_pos_mm)
while odoDrive.y_pos_mm<0:
    print(odoDrive.y_pos_mm)
    leftPow = -30 +kP*(180-gyro.value())
    rightPow = -30-kP*(180-gyro.value())
    if abs(leftPow)>95:
        if leftPow>rightPow:
            leftPow = 95
            rightPow = -95
        else:
            leftPow= -95
            rightPow = 95
    odoDrive.on(leftPow,rightPow)
odoDrive.off()
