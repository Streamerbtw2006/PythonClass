#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import time

# Write your program here
while not Button.LEFT : 

    if Button.DOWN in brick.buttons():
        print("Down Button")
        brick.light(Color.GREEN)
    if Button.UP in brick.buttons():
        print("Up Button")
        brick.light(Color.GREEN)
    if Button.RIGHT in brick.buttons():
        print("Right Button")
        brick.light(Color.RED)

brick.sound.beep(1, 1000, 5)
time.sleep(1)

brick.display.clear()
brick.display.text("Hello There", (35,40))
time.sleep(3)
brick.display.clear()
brick.display.text("General Kenobi", (35,40))
time.sleep(3)

