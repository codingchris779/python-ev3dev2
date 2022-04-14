#!/usr/bin/env python3
import math
from ev3dev2.button import Button
from ClassStructure.Location import Location
from ev3dev2.wheel import EV3Tire, Wheel
from ev3dev2.motor import LargeMotor, MoveTank,MoveDifferential,OUTPUT_A,OUTPUT_D
from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.display import Display
import time
robot = Location()
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
odoDrive.set_polarity(LargeMotor.POLARITY_NORMAL)
while not button.check_buttons(buttons=["up"]):
    print("waiting")
gyro = GyroSensor()
centerBoxDist = 3
gyro.reset()
gyro.calibrate()
gyro.reset()
odoDrive.gyro=gyro
kP = 2
kI = 1.5
errorSum = 0
count = 0
odoDrive.odometry_start()
print("GOING TO SHELF")
odoDrive.on_for_distance(-30,38*25.4)
print("x - {0:.2f} y - {1:.2f} rotODO - {2:.2f} rotGyro {3}".format(odoDrive.x_pos_mm,odoDrive.y_pos_mm, math.degrees(odoDrive.theta),gyro.value()))

print("TURNING")
odoDrive.turn_degrees(30,90)
odoDrive.turn_degrees(30,90-gyro.value())
print("x - {0:.2f} y - {1:.2f} rotODO - {2:.2f} rotGyro {3}".format(odoDrive.x_pos_mm,odoDrive.y_pos_mm, math.degrees(odoDrive.theta),gyro.value()))

print("GOING TO BOX")
while odoDrive.x_pos_mm>-(12+centerBoxDist)*25.4:
    count = count+1
    errorSum += 90-gyro.value()
    print("x - {0:.2f} y - {1:.2f} rotODO - {2:.2f} rotGyro {3}".format(odoDrive.x_pos_mm,odoDrive.y_pos_mm, math.degrees(odoDrive.theta),gyro.value()))
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

print("x - {0:.2f} y - {1:.2f} rotODO - {2:.2f} rotGyro {3}".format(odoDrive.x_pos_mm,odoDrive.y_pos_mm, math.degrees(odoDrive.theta),gyro.value()))
odoDrive.off()

errorSum=0
count=0
time.sleep(5)
odoDrive.turn_degrees(30,90-gyro.value())
print("x - {0:.2f} y - {1:.2f} rotODO - {2:.2f} rotGyro {3}".format(odoDrive.x_pos_mm,odoDrive.y_pos_mm, math.degrees(odoDrive.theta),gyro.value()))

print("GOING TO END SHELF")
while odoDrive.x_pos_mm>-(98)*25.4:
    count = count+1
    errorSum += 90-gyro.value()
    print("x - {0:.2f} y - {1:.2f} rotODO - {2:.2f} rotGyro {3}".format(odoDrive.x_pos_mm,odoDrive.y_pos_mm, math.degrees(odoDrive.theta),gyro.value()))
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

errorSum=0
count=0
odoDrive.off()
print("TURNING")
odoDrive.turn_degrees(30,90)
print(str(gyro.value()))
print("x - {0:.2f} y - {1:.2f} rotODO - {2:.2f} rotGyro {3}".format(odoDrive.x_pos_mm,odoDrive.y_pos_mm, math.degrees(odoDrive.theta),gyro.value()))
print("GOING TO ZONE B")
while odoDrive.y_pos_mm<0:
    errorSum+=180-gyro.value()
    count=count+1
    print("x - {0:.2f} y - {1:.2f} rotODO - {2:.2f} rotGyro {3}".format(odoDrive.x_pos_mm,odoDrive.y_pos_mm, math.degrees(odoDrive.theta),gyro.value()))
    leftPow = -30 +(kP*(180-gyro.value())+(errorSum/count)*kI)
    rightPow = -30-(kP*(180-gyro.value())+(errorSum/count)*kI)
    if abs(leftPow)>95:
        if leftPow>rightPow:
            leftPow = 95
            rightPow = -95
        else:
            leftPow= -95
            rightPow = 95
    odoDrive.on(leftPow,rightPow)
odoDrive.off()
errorSum=0
count=0
while not button.check_buttons(buttons=["up"]):
    print("waiting")
# input("press Enter")
time.sleep(5)
while odoDrive.y_pos_mm>-12*25.4:
    errorSum+=180-gyro.value()
    count = count+1
    print("x - {0:.2f} y - {1:.2f} rotODO - {2:.2f} rotGyro {3}".format(odoDrive.x_pos_mm,odoDrive.y_pos_mm, math.degrees(odoDrive.theta),gyro.value()))
    leftPow = 30 +(kP*(180-gyro.value())+(errorSum/count)*kI)
    rightPow = 30-(kP*(180-gyro.value())+(errorSum/count)*kI)
    if abs(leftPow)>95:
        if leftPow>rightPow:
            leftPow = 95
            rightPow = -95
        else:
            leftPow= -95
            rightPow = 95
    odoDrive.on(leftPow,rightPow)
errorSum=0
count=0
odoDrive.turn_degrees(-30,90)
while odoDrive.x_pos_mm<0:
    errorSum+=90-gyro.value()
    count = count+1
    print("x - {0:.2f} y - {1:.2f} rotODO - {2:.2f} rotGyro {3}".format(odoDrive.x_pos_mm,odoDrive.y_pos_mm, math.degrees(odoDrive.theta),gyro.value()))
    leftPow = 30 +(kP*(90-gyro.value())+(errorSum/count)*kI)
    rightPow = 30-(kP*(90-gyro.value())+(errorSum/count)*kI)
    if abs(leftPow)>95:
        if leftPow>rightPow:
            leftPow = 95
            rightPow = -95
        else:
            leftPow= -95
            rightPow = 95
    odoDrive.on(leftPow,rightPow)
odoDrive.off()
odoDrive.turn_degrees(-30,90)
odoDrive.on_for_distance(30,8*25.4)
