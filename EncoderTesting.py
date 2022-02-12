#!/usr/bin/env python3
import string
from time import sleep
from timeit import timeit
from ev3dev2.motor import Motor, LargeMotor, OUTPUT_A, OUTPUT_C, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound
from time import sleep
from  ev3dev2.display import Display
import ev3dev2.fonts as fonts
import os
import sys
import time
disp = Display()
countsPerRotLM =360
wheelDiameterMM=70
Length = 200
Laps = 2
message = "Laps: "+Laps+"Length of track: "+ Length+"Press center button to reset and go"
disp.draw.text((10,10), message,font=fonts.load('luBS14'))
disp.update()
rightM = Motor(OUTPUT_C)

#counts per rot 360
rotprev=0
while(time.time()<(timestart+55555)):
    rot = rightM.position
    rot1 = str(rot)
    if(rot!=rotprev):
        disp.clear()
    disp.draw.text((10,10), rot1,font=fonts.load('luBS14'))
    disp.update()
    rotprev=rot

time.sleep(3)
