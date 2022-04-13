#!/usr/bin/env python3
from ev3dev2.wheel import EV3Tire, Wheel
from ev3dev2.motor import LargeMotor, MediumMotor, MoveTank, MoveDifferential, OUTPUT_A, OUTPUT_D
from ev3dev2.lego.sensor import GyroSensor, UltrasonicSensor, ColorSensor
from ev3dev2.sensor import INPUT_2, INPUT_3
from ev3dev2.sound import Sound
import time
def processBarcodeData(sensor1, sensor2):
    qsize = int(len(sensor1)/4)
    barcode1 = 50<sensor1[int(qsize/2)]
    barcode2 = 50<sensor1[2*int(qsize/2)]
    barcode3 = 50<sensor1[3*int(qsize/2)]
    return 100*barcode1 + 10*barcode2 + 1*barcode3
def readBarcodeData(sensorr1, sensorr2, midMot):
    print("Starting To Read the Barcode")
    time.sleep(.4)
    while not sensorr1.reflected_light_intensity== 32:
        print("sense1 {0} Sense 2 {1}".format(sensorr1.reflected_light_intensity,sensorr2.reflected_light_intensity))
MkUltra = UltrasonicSensor()
def playChuckIntro():
    spkr = Sound()
    print("run first")
    spkr.play_file("testing/cake.wav")
# t=Thread(target=readBarcodeData)
# t.start()
mid = MediumMotor()
left = LargeMotor(OUTPUT_A)
right = LargeMotor(OUTPUT_D)
sensor1 = ColorSensor(INPUT_2)
sensor2 = ColorSensor(INPUT_3)

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
sense1Val = [0]
sense2Val = [0]

#mid.reset()
mid.on_to_position(80, 2000)
BRCDCkSum1 = 111
barcode1Wt = True
barcode2Wt = True
barcode3Wt = False
BarcodeBad = False

# MkUltra.MODE_US_DIST_CM()
odoDrive.odometry_start()
#----------
# 8/9
#--------
# mid.on_to_position(80,10000)
# time.sleep(2)
# print(str(sensor1.reflected_light_intensity))
liftPos = 2000
liftHeight = 22000
spd = 500
# t=Thread(target=readBarcodeData(sensorr1=sensor1,sensorr2=sensor2,midMot=mid))
# t.start()
mid.on_to_position(50,liftHeight)
mid.position
print(str(mid.position))
# while liftPos < liftHeight:
#     liftPos += 1 * spd
#     mid.on_to_position(100,liftPos)
#     sense1Val.append(sensor1.reflected_light_intensity)
#     sense2Val.append(sensor2.reflected_light_intensity)
#     print("sense1 {0} Sense 2 {1}".format(sensor1.reflected_light_intensity,sensor2.reflected_light_intensity))
print(str(processBarcodeData(sense2Val,sense2Val)))
# if  (sensor1.reflected_light_intensity>30 == barcode1Wt):
#     print("bad sector 1")
#     BarcodeBad = True
# mid.on_to_position(80,16000)
# time.sleep(2)
#
# print(str(sensor1.reflected_light_intensity))
# if  (sensor1.reflected_light_intensity>30 == barcode2Wt):
#     print("bad sector 2")
#     BarcodeBad = True
# mid.on_to_position(80,22000)
# time.sleep(2)

# print(str(sensor1.reflected_light_intensity))
# if (sensor1.reflected_light_intensity > 30 == barcode3Wt):
#     print("bad sector 3")
#     BarcodeBad = True
# mid.on_to_position(80,20000)
# odoDrive.on_for_distance(30,160)
# odoDrive.turn_degrees(-30,95)
# odoDrive.on_for_distance(-30,650)

# mid.on_to_position(80,1000)
# odoDrive.on_for_distance(30,150)
