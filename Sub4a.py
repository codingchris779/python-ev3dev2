#!/usr/bin/env python3
from ev3dev2.wheel import EV3Tire, Wheel
from ev3dev2.motor import LargeMotor, MoveTank,MoveDifferential,OUTPUT_A,OUTPUT_D
from ev3dev2.lego.sensor import GyroSensor,UltrasonicSensor

MkUltra = UltrasonicSensor
left = LargeMotor(OUTPUT_A)
right = LargeMotor(OUTPUT_D)
myWheel = Wheel(diameter_mm=44.2, width_mm=  22)
drive = MoveTank(OUTPUT_A,OUTPUT_D)
odoDrive = MoveDifferential(OUTPUT_A,OUTPUT_D,EV3Tire, 150)
odoDrive.wheel=myWheel
gyro = GyroSensor()
centerBoxDist = 3
gyro.reset()
gyro.calibrate()
gyro.reset()
odoDrive.gyro=gyro
odoDrive.odometry_start()
odoDrive.turn_degrees(-30,90)
# while MkUltra.distance_centimeters > 3:
#     odoDrive.on(-5)
# odoDrive.off()
#odoDrive.turn_to_angle(30,180,use_gyro=True,error_margin=1)

#odoDrive.on_for_distance(-30,(12+centerBoxDist)*25.4)
#time.sleep(3)

#odoDrive.turn_degrees(-30,90)
#print(str(gyro.value()))


#odoDrive.on_for_distance(-30,(108-(12+centerBoxDist))*25.4)

#odoDrive.turn_degrees(-30,90)
#odoDrive.on_for_distance(-30,39*25.4)


