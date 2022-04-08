#!/usr/bin/env python3
from distutils.file_util import write_file
import math
import string
from time import sleep
import array
import fcntl
from timeit import timeit
from weakref import WeakMethod
from ev3dev2.motor import Motor, LargeMotor, OUTPUT_A, OUTPUT_C, SpeedPercent, MoveTank,MoveDifferential
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from threading import Thread
from ev3dev2.led import Leds
from ev3dev2.sound import Sound
from ev3dev2.wheel import Wheel
from time import sleep
from  ev3dev2.display import Display
import ev3dev2.fonts as fonts
import os
import sys
import time
#!/usr/bin/env python

import array
import fcntl
import sys
from ev3dev2.button import Button
from ev3dev2.wheel import EV3Tire
from ev3dev2.sensor.lego import GyroSensor
def playChuckIntro():
    spkr = Sound()
    print("run first")
    spkr.play_file("cake.wav")
#t=Thread(target=playChuckIntro)
#t.start()
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
odoDrive = MoveDifferential(OUTPUT_A,OUTPUT_C,EV3Tire, 140)
odoDrive.wheel = Wheel(43.2,22)
gyro = GyroSensor()
gyro.reset()
gyro.calibrate()
#odoDrive.gyro= gyro
fileTime = int(time.perf_counter())
#This is a quick and dirty way to generate semi unique file names
#File names will be unique to each session but will not be unique across sessions
#Because of this the files should be moved into a new dir at the end of each testing session to avoid accidental data loss
writeFile = open("logs2/"+str(int(fileTime/1))+".txt",'w')
odoDrive.odometry_start()
startTime=time.perf_counter()
odoDrive.on(30,30)
lastTime = startTime
dt=time.perf_counter()-startTime
finalPos = 12*25.4
while(odoDrive.y_pos_mm<finalPos):
    dt=time.perf_counter()-lastTime
    leftPos = left.position
    rightPos = right.position
    theta = gyro.value()
    writeFile.write("{0:.10f}\t{1}\t{2}\t{3}\t{4}\n".format(dt,leftPos,rightPos,theta,math.degrees(odoDrive.theta)))
    
    # if  abs(theta)<1:
    #     odoDrive.on(30,30)
    # elif theta<0:
    #     odoDrive.on(30,33)
    # else :
    #     odoDrive.on(33,30)
    

    print(str(odoDrive.y_pos_mm))
    lastTime=time.perf_counter()
time.sleep(.5)
dt=time.perf_counter()-lastTime
writeFile.write("{0:.10f}\t{1}\t{2}\t{3}\t{4}\n".format(dt,leftPos,rightPos,theta,math.degrees(odoDrive.theta)))
writeFile.close()
print(str(odoDrive.y_pos_mm))
odoDrive.stop()