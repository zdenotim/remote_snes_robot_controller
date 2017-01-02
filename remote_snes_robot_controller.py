#!/usr/bin/env python

#
# Script by zdenotim (1/2017) inspired by @PiBorg
# pigpiod daemon must running on remotely controlled device
# For more info how to enable remote control on your RaspberryPi check @ben_nutall blog and github
# Note: Script is working only on OS with GUI due to pygame library
#

from gpiozero.pins.pigpiod import PiGPIOPin
from gpiozero import Robot
import pygame


# IP address of remote Robot (In my case RaspberryPi Zero with CamJam)
# Set IP of your RaspberryPi
remote_pi = "192.168.0.16"

# Set remote GPIO pins for robot motor control
robot = Robot(left=(PiGPIOPin(8, host=remote_pi), PiGPIOPin(7, host=remote_pi)),
              right=(PiGPIOPin(9, host=remote_pi), PiGPIOPin(10, host=remote_pi)))

# Setup SNES gamepad buttons
global hadEvent
global x
global y
global a
global b

hadEvent = False
x = False  # UP
y = False  # LEFT
a = False  # RIGHT
b = False  # DOWN

# Initialize pygame and SNES gamepad(joystick)
pygame.init()
pygame.joystick.init()

j = pygame.joystick.Joystick(0)
j.init()


# Define function to handle pygame events
def game_controller(events):
    global hadEvent
    global x
    global y
    global a
    global b
    # Define action when gamepad button is pressed
    for event in events:
        if event.type == pygame.JOYBUTTONDOWN:
            hadEvent = True
            x = j.get_button(0)  # UP
            y = j.get_button(3)  # LEFT
            a = j.get_button(1)  # RIGHT
            b = j.get_button(2)  # DOWN

            if x == 1:
                x = True
            elif y == 1:
                y = True
            elif a == 1:
                a = True
            elif b == 1:
                b = True
        # Define action when gamepad button is released
        elif event.type == pygame.JOYBUTTONUP:
            hadEvent = True
            x = j.get_button(0)  # UP
            y = j.get_button(3)  # LEFT
            a = j.get_button(1)  # RIGHT
            b = j.get_button(2)  # DOWN

            if x == 0:
                x = False
            elif y == 1:
                y = False
            elif a == 1:
                a = False
            elif b == 1:
                b = False

# Loop indefinitely
while True:
    # Get the currently pressed buttons gamepad
    game_controller(pygame.event.get())
    if hadEvent:
        # Move robot forward
        if x:
            robot.forward(speed=0.4)
        # Move robot to the left
        elif y:
            robot.left(speed=0.4)
        # Move robot to the right
        elif a:
            robot.right(speed=0.4)
        # Move robot backward
        elif b:
            robot.backward(speed=0.4)
        # Robot will stop
        else:
            robot.stop()
