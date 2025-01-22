# Run this program while connected to your controller to test controls

import pygame
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