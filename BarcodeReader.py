import math
import string
from time import sleep
import array
import fcntl
from ev3dev2.sensor.lego import LightSensor
import os
import sys
import time
from ev3dev2.sensor import INPUT_1,  INPUT_2
sensor1 = LightSensor(INPUT_1)
sensor2 = LightSensor(INPUT_2)
goLoop = True
while goLoop:
    command = input("Type Exit to quit")
    if(command=="Exit"):
        goLoop = False
    #type one all white 
    if(sensor1.reflected_light_intensity<10 and sensor2.reflected_light_intensity<10):
        print("box type 1 ")
    #Type 2 all Ambigous 
    elif(sensor1.reflected_light_intensity>10 and sensor1.reflected_light_intensity<50 and sensor2.reflected_light_intensity>10 and sensor2.reflected_light_intensity<50):
        print("box type 2 ")
    #Type 3 all Ambigous 
    elif(sensor1.reflected_light_intensity<10 and sensor2.reflected_light_intensity>50):
        print("box type 3 ")
    #Type 4 all Ambigous 
    else:
        print("box type 4 ")

