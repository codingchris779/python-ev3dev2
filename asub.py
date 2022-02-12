#!/usr/bin/env python3
from concurrent.futures import thread
from threading import Thread
import time
#from turtle import speed
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_C, SpeedPercent, MoveTank,SpeedRPS
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
from time import sleep
from ev3dev2.sound import Sound
def playChuckIntro():
    spkr = Sound()
    print("run first")
    spkr.play_file("cake.wav")
t=Thread(target=playChuckIntro)
laps =1
lenth = 100
#t.start()
print("Got past sound")
tank_pair= MoveTank(OUTPUT_A, OUTPUT_C, motor_class=LargeMotor)
tank_pair.on(10,10)
sleep(10)
tank_pair.off()