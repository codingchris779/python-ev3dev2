#!/usr/bin/env python3
from ev3dev2.wheel import EV3Tire, Wheel
from ev3dev2.motor import LargeMotor, MediumMotor, MoveTank, MoveDifferential, OUTPUT_A, OUTPUT_D
from ev3dev2.lego.sensor import GyroSensor, UltrasonicSensor, ColorSensor
from ev3dev2.sensor import INPUT_2, INPUT_3

import time

MkUltra = UltrasonicSensor()
sensor1 = ColorSensor(INPUT_2)
sensor2 = ColorSensor(INPUT_3)
mid = MediumMotor()
left = LargeMotor(OUTPUT_A)
right = LargeMotor(OUTPUT_D)
myWheel = Wheel(diameter_mm=44.2, width_mm=22)
drive = MoveTank(OUTPUT_A, OUTPUT_D)
odoDrive = MoveDifferential(OUTPUT_A, OUTPUT_D, EV3Tire, 150)
odoDrive.wheel = myWheel
gyro = GyroSensor()
centerBoxDist = 3
gyro.reset()
gyro.calibrate()
gyro.reset()
odoDrive.gyro = gyro
mid.on_to_position(80, 6000)

# MkUltra.MODE_US_DIST_CM()
odoDrive.odometry_start()
odoDrive.turn_degrees(30, 95)
mid.on_to_position(80, 1000)


while MkUltra.value() > 35 and MkUltra.value()<2000:
    print(MkUltra.value())
    odoDrive.on(-5,-5)
    time.sleep(.25)
odoDrive.off()
odoDrive.on_for_distance(-15,20)
print(str(sensor1.reflected_light_intensity))
print(str(sensor2.reflected_light_intensity))
odoDrive.off()
mid.on_to_position(80,20000)
odoDrive.on_for_distance(30,160)
odoDrive.turn_degrees(-30,95)
odoDrive.on_for_distance(-30,650)

mid.on_to_position(80,1000)
odoDrive.on_for_distance(30,150)


# odoDrive.turn_to_angle(30,180,use_gyro=True,error_margin=1)

# odoDrive.on_for_distance(-30,(12+centerBoxDist)*25.4)
# time.sleep(3)

# odoDrive.turn_degrees(-30,90)
# print(str(gyro.value()))


# odoDrive.on_for_distance(-30,(108-(12+centerBoxDist))*25.4)

# odoDrive.turn_degrees(-30,90)
# odoDrive.on_for_distance(-30,39*25.4)
