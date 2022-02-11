#!/usr/bin/env python3
from ev3dev2.sound import Sound
from time import sleep
sound = Sound()
#please download the sounds folder to your ev3 browser
#testing sound of a dog bark
sound.beep()
sound.play('/home/robot/python-ev3dev2/sounds/cake.wav',100,0)
sound.play_song((
    ('D4', 'e3'),
    ('D4', 'e3'),
    ('D4', 'e3'),
    ('G4', 'h'),
    ('D5', 'h')
))
#sleep(10)
#testing sound of another file 
sound.beep()