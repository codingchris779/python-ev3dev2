#!/usr/bin/env python3
import math
import string
from time import sleep
import array
import fcntl
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
#!/usr/bin/env python

import array
import fcntl
import sys
from ev3dev2.button import Button
btn = Button()
disp = Display()
left = LargeMotor(OUTPUT_A)
right = LargeMotor(OUTPUT_C)
countsPerRotLM =360
wheelDiameterMM=70
TicksToMM = wheelDiameterMM*math.pi
Length = 200
Laps = 2
message = "Laps: "+Laps+"Length of track: "+ Length+"Press center button to reset and go"
disp.draw.text((10,10), message,font=fonts.load('luBS14'))
disp.update()
while(not btn.enter):
    print("waiting")
disp.clear()
disp.update()
left.reset()
right.reset()
left.on_to_position(Length/TicksToMM)
right.on_to_position(Length/TicksToMM)