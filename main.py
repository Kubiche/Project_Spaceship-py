#import serial
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

# Get count of joysticks
joystick_count = pygame.joystick.get_count()

#joystick = pygame.joystick.Joystick(0)
#joystick.init()


# Sound instances
mainenginesound = pygame.mixer.Sound("C:\\Users\\jalvarez\\My Drive\\CODE\\Project_Spacecraft_py\\Project_Spaceship_Rpi\\Sounds\\main_engines.mp3")

pygame.display.set_mode((800, 600))



r1 = Rocket()


# ser = serial.Serial("/dev/ttyAMA0", 115200)
# serialFromArduino.flush()

on = True

while on:    
    for event in pygame.event.get():        
        if event.type == pygame.KEYDOWN:
            print("Key press detected")
            if event.key == pygame.K_ESCAPE:
                print("Escape key pressed")
                on = False
            if event.key == pygame.K_k:
                print("k key pressed")
                mainenginesound.play(-1)

    
    
    r1.update  # Updates the rocket properties like velocity, altitude etc.
    clock.tick(30)


pygame.quit()