import math
import time
import serial
import pygame


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



class Rocket:
    def __init__(self,fuel=100, health=100, acceleration=0, velocity=0, angle=90, altitude = 0):
        self.fuel = fuel
        self.health = health
        self.acceleration = acceleration
        self.velocity = velocity
        self.angle = angle  # Referenced from the positive side of X in a 2D representation.
        self.altitude = altitude
        self.last_update = time.time()
    
    def update(self):        
        time_elapsed = time.time() - self.last_update
        self.velocity = self.acceleration / time_elapsed
        self.altitude = self.altitude + ((self.velocity*math.sin(math.radians(self.angle))) * time_elapsed)

        self.last_update = time.time()  # Update last to record the time the update was finished


while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEWHEEL:
            mainenginesound.play(-1)

