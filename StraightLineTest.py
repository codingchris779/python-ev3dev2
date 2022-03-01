#!/usr/bin/env python3
import math
import string
from time import sleep
import array
import fcntl
from timeit import timeit
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
odoDrive = MoveDifferential(OUTPUT_A,OUTPUT_C,EV3Tire, 154.5)
gyro = GyroSensor()
gyro.reset()
#odoDrive.gyro= gyro
odoDrive.wheel = Wheel(56,27)
odoDrive.odometry_start()
odoDrive.on_to_coordinates(30,0,84*25.4)
