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

mainenginesound = pygame.mixer.Sound("/Sounds/main_engines.mp3")



class Rocket:
    def __init__(self,fuel=100, health=100, acceleration=0, speed=0, heading=0):
        self.fuel = fuel
        self.health = health
        self.acceleration = acceleration
        self.speed = speed
        self.heading = heading


while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEWHEEL:
            mainenginesound.play(-1)

