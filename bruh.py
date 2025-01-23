import pygame 



pygame.init() 



# Set screen dimensions

screen_width = 800

screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height)) 



# Game loop

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False



    # Fill the screen with white

    screen.fill((255, 255, 255)) 



    # Update the display

    pygame.display.flip() 



pygame.quit() 
