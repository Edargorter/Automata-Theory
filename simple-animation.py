#!/usr/bin/env python 

# Based on https://blog.gitnux.com/code/python-animation/

import pygame
import sys

# Initialize pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the window
pygame.display.set_caption("Finite State Machine")

# Load and set up state (your image file)
state_image = "state.png"  # Replace this with the path to your image
state = pygame.image.load(state_image)
state_rect = state.get_rect()
speed = 2  # Select the speed of the state movement

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill((255, 255, 255))  # White background

    # Move the state's position
    '''
    if state_rect.right < screen_width:
        state_rect.x += speed
    else:
        state_rect.x = 0
        '''

    pygame.draw.line(screen, BLACK, (state_rect.right, state_rect.height/2), 
                    (state_rect.right*2, state_rect.height/2),
                    width = 1)

    # Draw the state
    screen.blit(state, state_rect)

    # Update the display
    pygame.display.update()

    # Control the frame rate (60 FPS)
    pygame.time.delay(int(1000 / 60))
