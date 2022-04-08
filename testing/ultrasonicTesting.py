#!/usr/bin/env python3
from distutils.file_util import write_file
import math
from operator import truediv
import string
from time import sleep
import array
import fcntl
from timeit import timeit
from weakref import WeakMethod
from ev3dev2.motor import Motor, LargeMotor, OUTPUT_A, OUTPUT_C,OUTPUT_D, SpeedPercent, MoveTank,MoveDifferential
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor, UltrasonicSensor
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
import array
import fcntl
import sys
from ev3dev2.button import Button
from ev3dev2.wheel import EV3Tire
from ev3dev2.sensor.lego import GyroSensor
btn = Button()
disp = Display()
left = LargeMotor(OUTPUT_A)
right = LargeMotor(OUTPUT_D)
light = MediumMotor
light.on_for_seconds(50,55555)
myWheel = Wheel(diameter_mm=68.88, width_mm=  45)
countsPerRotLM =360
wheelDiameterMM=68.88
wheelCir = wheelDiameterMM*math.pi
SonicTheHedgeHog = UltrasonicSensor(INPUT_1)
left.on(30)
right.on(30)
while(SonicTheHedgeHog.value()>150):
    print(str(SonicTheHedgeHog.value()))
left.off()
right.off()
