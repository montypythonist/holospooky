# HOLOSPOOKY - cool stuff to do with your old Cozmo!! :3

import pycozmo
import pygame
from pygame.locals import *
from sys import exit


def deploy():
    # Establish connection to Cozmo
    global cli
    cli = pycozmo.Client()
    cli.start()
    cli.connect()
    try:
        cli.wait_for_robot()
    except:
        print("Failed to connect to Cozmo. Check if you are successfully connected to the robot WiFi")
        exit()
    print("Robot code deployed...") 


def joystick():
    # PYGAME CODE - For using a controller to control Cozmo
    pygame.init()
    pygame.joystick.init()
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    if joystick.get_init():
        print("Controller connected!")
    else:
        print("Controller not connected. Try checking Bluetooth connection, wired connection, battery life, or controller functionality.")
        exit()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.JOYAXISMOTION:
                if event.axis == 1:
                    if event.value < 0.5:
                        cli.set_head_angle(angle=1000, accel=1000)
                    if event.value > -0.5:
                        cli.set_head_angle(angle=-1000, accel=1000)
                # Axis 1 (AKA left joystick) controlls head movement. Up and down move the head angle to their respective directions.
                # Attempting to use Axis 0 (moving the left joystick left and right) will not do anything

                if event.axis == 3:
                    if event.value < 0:
                        cli.set_lift_height(height=1000, accel=1000, duration=0.1)
                    if event.value > 0:
                        cli.set_lift_height(height=-1000, accel=1000, duration=0.1)
                # Axis 3 (AKA right joystick) controlls arm movement. Up and down move the arm to their respective directions.
                # Attempting to use Axis 2 (moving the right joystick left and right) will not do anything

            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 11:
                    cli.drive_wheels(lwheel_speed=1000, rwheel_speed=1000)
                if event.button == 12:
                    cli.drive_wheels(lwheel_speed=-1000, rwheel_speed=-1000)
                if event.button == 13:
                    cli.drive_wheels(lwheel_speed=-1000, rwheel_speed=1000)
                if event.button == 14:
                    cli.drive_wheels(lwheel_speed=1000, rwheel_speed=-1000)
                # Arrow buttons control direction of cozmo. Forward and backward move the cozmo to their respective directions,
                # but left and right only rotate the cozmo. There is no net movement in any direction when rotating.

            if event.type == pygame.JOYBUTTONUP:
                if event.button <= 14 and event.button >= 11:
                    cli.drive_wheels(lwheel_speed=0, rwheel_speed=0)
                    # releasing any of the arrow controls will pause all rotation/direction movement

def joystick_test():
    # Run this program while connected to your controller to test controls
    pygame.init()
    pygame.joystick.init()
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    if joystick.get_init():
        print("Controller connected! [TEST MODE] Begin testing")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.JOYAXISMOTION:
                print("Axis:", event.axis, "Value:", event.value)
            elif event.type == pygame.JOYBUTTONDOWN:
                print("Button:", event.button, "pressed")
            elif event.type == pygame.JOYBUTTONUP:
                print("Button:", event.button, "released")

def keyboard():
    # for using your keyboard to control Cozmo
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Keyboard Input (Must be active here for keyboard usage)")
    screen.fill((0, 0, 0))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_w or event.key == K_UP:
                    cli.drive_wheels(lwheel_speed=1000, rwheel_speed=1000)
                elif event.key == K_a or event.key == K_LEFT:
                    cli.drive_wheels(lwheel_speed=-1000, rwheel_speed=1000)
                elif event.key == K_s or event.key == K_DOWN:
                    cli.drive_wheels(lwheel_speed=-1000, rwheel_speed=-1000)
                elif event.key == K_d or event.key == K_RIGHT:
                    cli.drive_wheels(lwheel_speed=1000, rwheel_speed=-1000)
                    # KEYBOARD: WASD and arrow controls both move the Cozmo. Forward and backward move the cozmo to their respective directions,
                    # but left and right only rotate the cozmo. There is no net movement in any direction when rotating.
            if event.type == KEYUP:
                if event.key == K_w or event.key == K_a or event.key == K_s or event.key == K_d or event.key == K_UP or event.key == K_DOWN or event.key == K_RIGHT or event.key == K_LEFT:
                    cli.drive_wheels(lwheel_speed=0, rwheel_speed=0)

def keyboard_test():
    # Run this program while connected to your controller to test controls
    pygame.init()
    print("Keyboard input enabled!")
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_w or event.key == K_UP:
                    print("Up/W Key")
                elif event.key == K_a or event.key == K_LEFT:
                    print("Left/A Key")
                elif event.key == K_s or event.key == K_DOWN:
                    print("Down/S Key")
                elif event.key == K_d or event.key == K_RIGHT:
                    print("Right/D Key")

            if event.type == KEYUP:
                if event.key == K_w or event.key == K_a or event.key == K_s or event.key == K_d or event.key == K_UP or event.key == K_DOWN or event.key == K_RIGHT or event.key == K_LEFT:
                    print("Key release!")




                    