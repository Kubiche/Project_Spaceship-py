import math
import time
import serial
import pygame
from rocket import Rocket

# Initialize the mixer
pygame.mixer.pre_init(48000, -16, 1, 1024)  #was 1024
pygame.mixer.init()

# DON'T PUT PYGAME.INIT BEFORE MIXER.INIT!
pygame.init()
pygame.mixer.set_num_channels(14)

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Initialize the joysticks
pygame.joystick.init()


# Sound instances
mainenginesound = pygame.mixer.Sound("/Sounds/main_engines.mp3")



r1 = Rocket()

ser = serial.serial()

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEWHEEL:
            mainenginesound.play(-1)
    
    
    r1.update  # Updates the rocket properties like velocity, altitude etc.
