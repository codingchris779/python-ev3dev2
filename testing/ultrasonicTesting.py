#!/usr/bin/env python3
import math
from ev3dev2 import LargeMotor, OUTPUT_A, OUTPUT_D
from ev3dev2 import INPUT_1
from ev3dev2 import UltrasonicSensor
from ev3dev2 import Wheel
from ev3dev2 import Display
from ev3dev2 import Button

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
