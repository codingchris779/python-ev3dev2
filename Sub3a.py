#!/usr/bin/env python3
from ev3dev2.wheel import EV3Tire, Wheel
from ev3dev2.motor import LargeMotor, MediumMotor, MoveTank, MoveDifferential, OUTPUT_A, OUTPUT_D
from ev3dev2.sensor.lego import GyroSensor, UltrasonicSensor, ColorSensor
from ev3dev2.sensor import INPUT_2, INPUT_3
from ev3dev2.sound import Sound
mid = MediumMotor()
def processBarcodeData(sensor1, sensor2):
    qsize = int(len(sensor1)/4)
    print(sensor2[3*int(qsize/2)])
    barcode1 = 20<sensor2[int(3*int(qsize/2))]
    print(sensor2[3*int(qsize/2)])
    barcode2 = 20<sensor1[int(4*int(qsize/2))]
    print(sensor2[4*int(qsize/2)])
    barcode3 = 20<sensor1[int(4.5*int(qsize/2))]
    return barcode1*100+barcode2*10+barcode3*1
sense1Val = [0]
sense2Val = [0]
sensor1 = ColorSensor(INPUT_2)
sensor2 = ColorSensor(INPUT_3)
mid.on_to_position(100,2000)
while mid.position<19000:
    sense1Val.append(sensor1.reflected_light_intensity)
    sense2Val.append(sensor2.reflected_light_intensity)
    print("sense1 {0} Sense 2 {1}".format(sensor1.reflected_light_intensity,sensor2.reflected_light_intensity))
    mid.on(50)
mid.off()
print(processBarcodeData(sense1Val,sense2Val))

