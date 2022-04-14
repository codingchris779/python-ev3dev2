#!/usr/bin/env python3
from ev3dev2.wheel import EV3Tire, Wheel
from ev3dev2.motor import LargeMotor, MediumMotor, MoveTank, MoveDifferential, OUTPUT_A, OUTPUT_D
from ev3dev2.sensor.lego import GyroSensor, UltrasonicSensor, ColorSensor
from ev3dev2.sensor import INPUT_2, INPUT_3
from ev3dev2.sound import Sound
from threading import Thread
import random
import time
left = LargeMotor(OUTPUT_A)
right = LargeMotor(OUTPUT_D)
myWheel = Wheel(diameter_mm=43.2, width_mm=22)
drive = MoveTank(OUTPUT_A, OUTPUT_D)
odoDrive = MoveDifferential(OUTPUT_A, OUTPUT_D, EV3Tire, 156)
odoDrive.wheel = myWheel
odoDrive.odometry_start()
def playChuckIntro():
    spkr = Sound()
    print("run first")
    spkr.play_file("mo.wav")
t=Thread(target=playChuckIntro)
t.start()
while True:
    t = random.randint(1,4)
    theta = random.randint(-90,90)
    odoDrive.on_for_seconds(-100,-100,t)
    odoDrive.turn_degrees(100, theta)
    
