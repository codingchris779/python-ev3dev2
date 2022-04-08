#!/usr/bin/env python3

from ev3dev2.motor import MediumMotor
lighgg= MediumMotor()
lighgg.on_for_seconds(
    100,50)