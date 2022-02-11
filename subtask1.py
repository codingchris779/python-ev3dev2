#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds

leftDrive = LargeMotor(OUTPUT_A) 
rightDrive = LargeMotor(OUTPUT_B)   #defining a large motor
leftDrive.COMMAND_RUN_TIMED(20)
leftDrive.COMMAND_RUN_TIMED(20)