import os
#import serial
import pygame
from rocket import Rocket


WIDTH,HEIGTH = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGTH))
SPACE_GREY = (101,115,126)
FPS = 60
pygame.display.set_caption("CURIOSITY SPACE PROGRAM")


class Game:
    def __init__(self,running = True):
        self.running = running 


def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            session.running = False        
        if event.type == pygame.KEYDOWN:
            print("Key press detected")
            if event.key == pygame.K_ESCAPE:
                print("Escape key pressed")
                session.running = False
            if event.key == pygame.K_k:
                print("k key pressed")
                mainenginesound.play(-1)


def draw_window():
    WIN.fill(SPACE_GREY)
    pygame.display.update()


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

# Get count of joysticks
joystick_count = pygame.joystick.get_count()

#joystick = pygame.joystick.Joystick(0)
#joystick.init()

# Sound instances
mainenginesound = pygame.mixer.Sound(os.path.join('Assets', 'Sounds', 'main_engines.mp3'))





r1 = Rocket()
session = Game()


# ser = serial.Serial("/dev/ttyAMA0", 115200)
# serialFromArduino.flush()



while session.running:
    clock.tick(FPS)    
    check_events()     
    r1.update  # Updates the rocket properties like velocity, altitude etc.
    draw_window()


pygame.quit()