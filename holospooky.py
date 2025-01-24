# HOLOSPOOKY - cool stuff to do with your old Cozmo!! :3

import pycozmo
import pygame
import cv2
import sys

# TODO: #4 update wiki

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
        sys.exit()
    print("Robot code deployed...") 

def connect_joystick():
    # stabilizes connection from controller to pygame
    pygame.init()
    pygame.joystick.init()
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    if joystick.get_init():
        print("Controller connected!")
    else:
        print("Controller not connected. Try checking Bluetooth connection, wired connection, battery life, or controller functionality.")

# TODO: #1 fix controls for arm and head movement
def joystick():
    # PYGAME CODE - For using a controller to control Cozmo
    while True:
        for event in pygame.event.get():
            if event.type == pygame.JOYAXISMOTION:
                if event.axis == 1:
                    if event.value > 0:
                        cli.set_head_angle(angle=1000, accel=1000, duration=0)
                    if event.value < 0:
                        cli.set_head_angle(angle=-1000, accel=1000, duration=0)
                # Axis 1 (AKA left joystick) controlls head movement. Up and down move the head angle to their respective directions.
                # Attempting to use Axis 0 (moving the left joystick left and right) will not do anything

                if event.axis == 3:
                    if event.value > 0:
                        cli.set_lift_height(height=1000, accel=1000, duration=0.1)
                    if event.value < 0:
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
                # CONSOLEArrow buttons control direction of cozmo. Forward and backward move the cozmo to their respective directions,
                # but left and right only rotate the cozmo. There is no net movement in any direction when rotating.

            if event.type == pygame.JOYBUTTONUP:
                if event.button <= 14 and event.button >= 11:
                    cli.drive_wheels(lwheel_speed=0, rwheel_speed=0)
                    # releasing any of the arrow controls will pause all rotation/direction movement

# TODO: #2 find cozmo camera module
def webcam():
    # WIP - Accessing cozmo's camera and displaying it on computer
    cap = cv2.VideoCapture(0)
    print("Webcam connected (but not rly this is a placeholder for cozmo's webcam) PRESS \"q\" to disconnect")
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow("Webcam Feed", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        # press "q" key to close camera
    cap.release()
    cv2.destroyAllWindows()

def test_joystick():
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

# TODO: #3 finalize keyboard controls
def keyboard():
    # for using your keyboard to control Cozmo
    if keypress == "up" or event.button == "w":
        cli.drive_wheels(lwheel_speed=1000, rwheel_speed=1000)
    if keypress == "down" or event.button == "s":
        cli.drive_wheels(lwheel_speed=-1000, rwheel_speed=-1000)
    if keypress == "right" or event.button == "a":
        cli.drive_wheels(lwheel_speed=-1000, rwheel_speed=1000)
    if keypress == "left" or event.button == "d":
        cli.drive_wheels(lwheel_speed=1000, rwheel_speed=-1000)
        # KEYBOARD: WASD and arrow controls both move the Cozmo. Forward and backward move the cozmo to their respective directions,
        # but left and right only rotate the cozmo. There is no net movement in any direction when rotating.
