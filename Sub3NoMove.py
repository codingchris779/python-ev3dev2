#!/usr/bin/env python3

from itertools import count
from ev3dev2.wheel import EV3Tire, Wheel
from ev3dev2.motor import LargeMotor, MediumMotor, MoveTank, MoveDifferential, OUTPUT_A, OUTPUT_D
from ev3dev2.sensor.lego import GyroSensor, UltrasonicSensor, ColorSensor
from ev3dev2.sensor import INPUT_2, INPUT_3
from ev3dev2.sound import Sound
import time
def processBarcodeData(sensor1, sensor2):
    colorsOfSense1 = []
    colorsOfSense2 = []
    whtLengths = []
    blkLengths = []

    BcCount = 1
    bcLength = 0 
    lastNum = -1
    barcodeChkSum = 0
    for j in sensor1:
        if (j<10):
            colorsOfSense1.append(0)
        elif j>60:
            colorsOfSense1.append(1)
        else:
            colorsOfSense1.append(-1)
    print("sense1")
    for j in sensor2:
        if (j<10):
            colorsOfSense2.append(0)
        elif j>40:
            colorsOfSense2.append(1)
        else:
            colorsOfSense2.append(-1)
    for n in colorsOfSense2:
       # print("{0} {1}".format(n,lastNum))
        if n == 0 and lastNum==1:
            print(" wht {0}".format(bcLength))
            whtLengths.append(bcLength)
            bcLength = 0
            BcCount = BcCount+1
        elif n ==0:
            bcLength+=1
        if n == 1 and lastNum == 0: 
            print("blk {0}".format(bcLength))
            blkLengths.append(bcLength)
            bcLength = 0
            BcCount = BcCount+1
        elif n==1:
            bcLength+=1
        if not n == -1:
         lastNum = n
    if lastNum == 1:
        whtLengths.append(bcLength)
    else:
        blkLengths.append(bcLength)
    for n in blkLengths:
        print(n)
    for n in whtLengths:
        print(n)

    #assume almost no black 
    if(blkLengths[0]>100):
        return 11
    if(len(whtLengths))==1 and whtLengths[0]>180:
        return 111
    if(blkLengths[0]>80):
        return 11
    if len(whtLengths) == 1:
        return 110
    return 101

print("Start")
left = LargeMotor(OUTPUT_A)
right = LargeMotor(OUTPUT_D)
myWheel = Wheel(diameter_mm=43.2, width_mm=22)
drive = MoveTank(OUTPUT_A, OUTPUT_D)
odoDrive = MoveDifferential(OUTPUT_A, OUTPUT_D, EV3Tire, 156)
odoDrive.wheel = myWheel
mid = MediumMotor()
MkUltra = UltrasonicSensor()
sense1Val = [0]
sense2Val = [0]
sensor1 = ColorSensor(INPUT_2)
sensor2 = ColorSensor(INPUT_3)
odoDrive.odometry_start()
mid.on_to_position(80, 2000)



while mid.position<22000:
    sense1Val.append(sensor1.reflected_light_intensity)
    sense2Val.append(sensor2.reflected_light_intensity)
    #print("sense1 {0} Sense 2 {1}".format(sensor1.reflected_light_intensity,sensor2.reflected_light_intensity))
    mid.on(85)
mid.off()
print(processBarcodeData(sense1Val,sense2Val))
mid.on_to_position(100,2000)

