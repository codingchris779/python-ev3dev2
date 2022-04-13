#!/usr/bin/env python3
import math
from ev3dev2 import LargeMotor, OUTPUT_A, OUTPUT_C, MoveTank,MoveDifferential
from ev3dev2 import Wheel
from ev3dev2 import Display
import time
#!/usr/bin/env python

from ev3dev2 import Button
from ev3dev2 import EV3Tire
from ev3dev2 import GyroSensor
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
odoDrive = MoveDifferential(OUTPUT_A,OUTPUT_C,EV3Tire, 145.1)
gyro = GyroSensor()
gyro.reset()
odoDrive.wheel = Wheel(56,28)
gyro.calibrate()
print(str(gyro.value()))
odoDrive.odometry_start()
odoDrive.gyro=gyro
#odoDrive.on_to_coordinates(30,0,12*25.4)
odoDrive.turn_degrees(20,180,error_margin=0,use_gyro=True)
print(str(left.position))
print(str(right.position))


#odoDrive.on_to_coordinates(30,48*25.4,12*25.4)
print(str(gyro.value()))
time.sleep(1)
print(str(gyro.value()))
odoDrive.odometry_stop()




