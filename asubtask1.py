#!/usr/bin/env python3
from time import sleep
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound
from time import sleep
sound = Sound()
sound.beep()
#comment
#comment2
# leftDrive = LargeMotor(OUTPUT_A) 
# rightDrive = LargeMotor(OUTPUT_B) 
# print("test")  #defining a large motor
# leftDrive.on_for_seconds(speed=SpeedRPS(-2), seconds=3)
# rightDrive.on_for_seconds(speed=SpeedRPS(2), seconds=3)
# print("test")
# sleep(100)