# Basic paint program made with pygame that outputs a 280x280 png
# Emmet Geoghegan

import pygame  # Import pygame

canvas = pygame.display.set_mode((280, 280))     # Define our screen region
pygame.display.set_caption("Number Identifier")  # Title window
white = [255, 255, 255]                          # Define white
draw_on = False                                  # Disable continious draw
pencolor = (0, 0, 0)                             # Define pen color ie black
radius = 10                                      # Brush size
last_pos = (0, 0, 0)                             # Placeholder


def whiteout():                                 # Func to clear canvas
    canvas.fill(white)                          # Set background color
    pygame.display.update()                     # Fill


def smoothener(srf, color, start, end, radius=1):                                     # Creates smooth lines
    dx = end[0]-start[0]                                                              # Gets change in x and y pos
    dy = end[1]-start[1]
    distance = max(abs(dx), abs(dy))                                                  # gets distance and for every unit draws a circle
    for i in range(distance):
        x = int(start[0]+float(i)/distance*dx)                                        # along the line connecting the initial and final co-ords
        y = int(start[1]+float(i)/distance*dy)
        pygame.display.update(pygame.draw.circle(srf, pencolor, (x, y), radius))      # draw tje circle


def Capture(display, name, pos, size):
    image = pygame.Surface(size)                                                       # Create image surface
    image.blit(display, (0, 0), (pos, size))                                           # screencap the image
    pygame.image.save(image, name)                                                     # Save the image to the disk


whiteout()
drawing = True
while drawing is True:
    e = pygame.event.wait()                                                             # Waits til something happens
    if e.type == pygame.MOUSEBUTTONDOWN:                                                # If mouse is pressed
        pygame.draw.circle(canvas, pencolor, e.pos, radius)                             # Draw a circle at the events position
        draw_on = True                                                                  # Allow us to draw more
    if e.type == pygame.MOUSEBUTTONUP:
        draw_on = False                                                                 # Stop drawing when mouse button is released
    if e.type == pygame.MOUSEMOTION:
        if draw_on:                                                                     # If mouse is moving and the button is presed
            pygame.display.update(pygame.draw.circle(canvas, pencolor, e.pos, radius))  # Draw lots of circles
            smoothener(canvas, pencolor, e.pos, last_pos,  radius)                      # If the mouse moves to fast we see individual circles so we have to smooth out
        last_pos = e.pos
    if e.type == pygame.KEYDOWN:                                                        # If q is pressed screencap the drawing area
        if e.key == pygame.K_q:                                                         # and stop the program
            Capture(canvas, "usersublarge.png", (0, 0), (280, 280))
            drawing = False
    if e.type == pygame.KEYDOWN:                                                        # If w is preseed whiteout the screen again
        if e.key == pygame.K_w:
            whiteout()

pygame.quit()                                                                           # exit pygame
