import pycozmo
import pygame
import cv2
import sys

def deploy():
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
    pygame.init()
    pygame.joystick.init()
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    if joystick.get_init():
        print("Controller connected!")
    else:
        print("Controller not connected. Try checking Bluetooth connection, wired connection, battery life, or controller functionality.")

def joystick():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.JOYAXISMOTION:
                if event.axis == 1:
                    if event.value > 0:
                        cli.set_head_angle(angle=1000, accel=1000, duration=0)
                    if event.value < 0:
                        cli.set_head_angle(angle=-1000, accel=1000, duration=0)

                if event.axis == 3:
                    if event.value > 0:
                        cli.set_lift_height(height=1000, accel=1000, duration=0.1)
                    if event.value < 0:
                        cli.set_lift_height(height=-1000, accel=1000, duration=0.1)

            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 11:
                    cli.drive_wheels(lwheel_speed=1000, rwheel_speed=1000)
                if event.button == 12:
                    cli.drive_wheels(lwheel_speed=-1000, rwheel_speed=-1000)
                if event.button == 13:
                    cli.drive_wheels(lwheel_speed=-1000, rwheel_speed=1000)
                if event.button == 14:
                    cli.drive_wheels(lwheel_speed=1000, rwheel_speed=-1000)

            if event.type == pygame.JOYBUTTONUP:
                if event.button <= 14 and event.button >= 11:
                    cli.drive_wheels(lwheel_speed=0, rwheel_speed=0)

def webcam():
    cap = cv2.VideoCapture(0)
    print("Webcam connected (but not rly this is a placeholder for cozmo's webcam) PRESS \"q\" to disconnect")
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow("Webcam Feed", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

def test_joystick():
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
    if keypress == "up" or event.button == "w":
        cli.drive_wheels(lwheel_speed=1000, rwheel_speed=1000)
    if keypress == "down" or event.button == "s":
        cli.drive_wheels(lwheel_speed=-1000, rwheel_speed=-1000)
    if keypress == "right" or event.button == "a":
        cli.drive_wheels(lwheel_speed=-1000, rwheel_speed=1000)
    if keypress == "left" or event.button == "d":
        cli.drive_wheels(lwheel_speed=1000, rwheel_speed=-1000)
