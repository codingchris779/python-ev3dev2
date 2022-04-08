#!/usr/bin/env python3
import math
import string
from time import sleep
import array
import fcntl
from timeit import timeit
from ev3dev2.motor import Motor, LargeMotor, OUTPUT_A, OUTPUT_C, SpeedPercent, MoveTank,MoveDifferential,MediumMotor
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
def findRotError(gyroAngle, targetAngle):
   # print(math.fmod(gyroAngle,360))
    correctedGyroAngle=360-math.fmod(gyroAngle,360)
    return targetAngle-gyroAngle

def playChuckIntro():
    spkr = Sound()
    print("run first")
    spkr.play_file("cake.wav")
light = MediumMotor()
light.run_forever()
t=Thread(target=playChuckIntro)
t.start()
btn = Button()
disp = Display()
left = LargeMotor(OUTPUT_A)
right = LargeMotor(OUTPUT_C)
myWheel = Wheel(diameter_mm=68.88, width_mm=  45)
countsPerRotLM =360
wheelDiameterMM=68.88
wheelCir = wheelDiameterMM*math.pi
#dont foget its in cm
Length = 120
Laps = 3
drive = MoveTank(OUTPUT_A,OUTPUT_C)
#156.3
#154.3
odoDrive = MoveDifferential(OUTPUT_A,OUTPUT_C,EV3Tire, 154.5)
gyro = GyroSensor()
#odoDrive.gyro= gyro
odoDrive.wheel = Wheel(56,27)
message = "Laps: "+str(Laps)+"Length of track: "+ str(Length)+"Press center button to reset and go"
disp.draw.text((10,10), message,font=fonts.load('luBS14'))
disp.update()
# while(not btn.enter):
#     print(Length)
disp.clear()
disp.update()
left.reset()
right.reset()
odoDrive.odometry_start()
gyro.calibrate()
gyro.reset()
odoDrive.gyro=gyro
#.turn_degrees(20,360*10)
# time.sleep(1)
startingVal = gyro.value()
# while True:
#     print(findRotError(gyro.value(),0))
# for k in range(Laps):
#     odoDrive.on_for_distance(speed = 40,distance_mm = Length*10)
#     print(str(gyro.value()%360))

#     odoDrive.turn_degrees(-10,findRotError(gyro.value(),180))


#     odoDrive.turn_degrees(-10,findRotError(gyro.value(),180))
#     print(str(gyro.value()%360))

#     odoDrive.on_for_distance(speed = 40,distance_mm = Length*10)
#     print(str(gyro.value()%360))

#     odoDrive.turn_degrees(-10,findRotError(gyro.value(),0))
#     odoDrive.turn_degrees(-10,findRotError(gyro.value(),0))

#     print(str(gyro.value()%360))

    #odoDrive.turn_degrees(-10,(gyro.value()%360)-startingVal)





"This is old code that im trying to change"
for k in range(Laps):
    odoDrive.on_to_coordinates(speed=35,x_target_mm=0,y_target_mm=Length*10)
    sleep(1)

    odoDrive.turn_to_angle(10,270,error_margin=1)
    print(str(odoDrive.x_pos_mm)+" "+str(odoDrive.y_pos_mm)+" "+str(math.degrees(odoDrive.theta))+" ")

    odoDrive.on_to_coordinates(speed=35,x_target_mm=0,y_target_mm=0)
    sleep(1)

    odoDrive.turn_to_angle(10,90,error_margin=1)
    print(str(odoDrive.x_pos_mm)+" "+str(odoDrive.y_pos_mm)+" "+str(math.degrees(odoDrive.theta))+" ")

    print(k)
odoDrive.turn_to_angle(10,90)
# for k in range(Laps):
#     while(odoDrive.y_pos_mm<Length*10):
#         odoDrive.follow_gyro_angle(  
#         kp=11.3, ki=0.05, kd=3.2,
#         speed=SpeedPercent(30),
#         target_angle=0,follow_for=)
#         print(odoDrive.y_pos_mm)
#     odoDrive.stop()
#     sleep(1)
#     odoDrive.turn_degrees(-10,findRotError(gyro.value(),180),error_margin=1)
#     print(str(odoDrive.x_pos_mm)+" "+str(odoDrive.y_pos_mm)+" "+str(math.degrees(odoDrive.theta))+" ")

#     while(odoDrive.y_pos_mm>0):
#         odoDrive.follow_gyro_angle(  
#         kp=11.3, ki=0.05, kd=3.2,
#         speed=SpeedPercent(30),
#         target_angle=180)
#     odoDrive.stop()
    
#     sleep(1)
#     sleep(1)

#     odoDrive.turn_degrees(-10,findRotError(gyro.value(),0),error_margin=1)
#     odoDrive.turn_degrees(-10,findRotError(gyro.value(),0),error_margin=1)
#     print(str(odoDrive.x_pos_mm)+" "+str(odoDrive.y_pos_mm)+" "+str(math.degrees(odoDrive.theta))+" ")

#     print(k)
# odoDrive.turn_to_angle(10,90)

#odoDrive.turn_to_angle(20,90)
    # odoDrive.on_for_distance(speed = 20,distance_mm = Length*10)
    # odoDrive.turn_degrees(speed= 10, degrees = 180)
    # odoDrive.on_for_distance(speed = 20,distance_mm = Length*10)
    # odoDrive.turn_degrees(speed= 10, degrees = 180)


    # odoDrive.reset()
    # odoDrive.odometry_stop()
    # odoDrive.odometry_start()
    # time.sleep(.3)
odoDrive.odometry_stop()