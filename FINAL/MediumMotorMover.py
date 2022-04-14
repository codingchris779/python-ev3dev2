#!/usr/bin/env python3
from ev3dev2.motor import MediumMotor
from ev3dev2.button import Button

KEY_LEFT = 105
KEY_RIGHT = 106
mid = MediumMotor()
KEY_MAX = 0x2ff
butt = Button()
def EVIOCGKEY(length):
    return 2 << (14+8+8) | length << (8+8) | ord('E') << 8 | 0x18

# end of stuff from linux/input.h

BUF_LEN = (KEY_MAX + 7) / 8

def test_bit(bit, bytes):
    # bit in bytes is 1 when released and 0 when pressed
    return bool(bytes[bit / 8] & (1 << (bit % 8)))
while not butt.check_buttons( buttons=["backspace"]):
    if(butt.check_buttons( buttons=["right"])):
        mid.on(80)
        #mid.on_for_rotations(speed=30,rotations=.1)
    elif((butt.check_buttons( buttons=["left"]))):
        mid.on(-80)
    elif((butt.check_buttons( buttons=["up"]))):
        mid.reset()
       # mid.on_for_rotations(speed=-30,rotations=.1)
    else:
        mid.off()
        print(mid.position)
