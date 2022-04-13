#!/usr/bin/env python3
from ev3dev2 import ColorSensor,UltrasonicSensor
from ev3dev2 import MediumMotor, LargeMotor, OUTPUT_A, OUTPUT_D
from ev3dev2 import Button

from ev3dev2 import INPUT_2,INPUT_3
left = LargeMotor(OUTPUT_D)
right = LargeMotor(OUTPUT_A)
butt = Button()
mid = MediumMotor()
sensor1 = ColorSensor(INPUT_2)
sensor2 = ColorSensor(INPUT_3)
MkUltra = UltrasonicSensor()
goLoop = True
pos = 0
mid.reset()
#pos 1 7200
#pox 2 12700
#pos 3 19000
# nominal < 40 is black, most blacks read under 10
while goLoop:
    while not butt.check_buttons( buttons=["up"]):
        if(butt.check_buttons( buttons=["right"])):
            pos+=100
            #mid.on_for_rotations(speed=30,rotations=.1)
        elif((butt.check_buttons( buttons=["left"]))):
            pos-=100
        # mid.on_for_rotations(speed=-30,rotations=.1)
        else:
            mid.on_to_position(30,pos)
            print("endcoder pos = "+ str(pos))

    command = input("Type Exit to quit")
    if(command=="Exit"):
        goLoop = False
    #type one all white
    left.off()
    right.off()
    if(sensor1.reflected_light_intensity<10 and sensor2.reflected_light_intensity<10):
        print("box type 1 ")
        print(str(sensor1.reflected_light_intensity))
        print(str(sensor2.reflected_light_intensity))

    #Type 2 all Ambigous
    elif(sensor1.reflected_light_intensity>10 and sensor1.reflected_light_intensity<30 and sensor2.reflected_light_intensity>10 and sensor2.reflected_light_intensity<30):
        print("box type 2 ")
        print(str(sensor1.reflected_light_intensity))
        print(str(sensor2.reflected_light_intensity))

    #Type 3 all Ambigous
    elif(sensor1.reflected_light_intensity<10 and sensor2.reflected_light_intensity>30):
        print("box type 3 ")
        print(str(sensor1.reflected_light_intensity))
        print(str(sensor2.reflected_light_intensity))

    #Type 4 all Ambigous
    else:
        print("box type 1 ")
        print(str(sensor1.reflected_light_intensity))
        print(str(sensor2.reflected_light_intensity))


