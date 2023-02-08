import os
#import serial
import pygame
from rocket import Rocket


WIDTH,HEIGTH = 1920, 1080
WIN = pygame.display.set_mode((WIDTH, HEIGTH))
SPACE_GREY = (101,115,126)
FPS = 60
pygame.display.set_caption("CURIOSITY SPACE PROGRAM")





# Images
CRAFT_WIDTH, CRAFT_HEIGTH = 400, 200
CRAFT_IMAGE = pygame.image.load(os.path.join('Assets', 'Images', 'craft.png'))
CRAFT_OPEN_DOOR_IMAGE = pygame.image.load(os.path.join('Assets', 'Images', 'craft_open_door.png'))
CRAFT_ENGINE_ON_IMAGE = pygame.image.load(os.path.join('Assets', 'Images', 'craft_engine_on.png'))


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
            if event.key == pygame.K_k:  # Engine ON
                print("k key pressed")
                r1.angle = 60
                global craft
                craft = pygame.transform.rotate(pygame.transform.scale(CRAFT_ENGINE_ON_IMAGE, (CRAFT_WIDTH, CRAFT_HEIGTH)), r1.angle)
                MAIN_ENGINE_SOUND.play(-1)
            if event.key == pygame.K_l:  # Engine OFF
                print("k key pressed")
                craft = pygame.transform.rotate(pygame.transform.scale(CRAFT_IMAGE, (CRAFT_WIDTH, CRAFT_HEIGTH)), r1.angle)
                MAIN_ENGINE_SOUND.stop()
            if event.key == pygame.K_LEFT
                r1.angle += 1
                craft = pygame.transform.rotate(pygame.transform.scale(CRAFT_IMAGE, (CRAFT_WIDTH, CRAFT_HEIGTH)), r1.angle)



def draw_window():
    
    WIN.fill(SPACE_GREY)
    WIN.blit(craft, (((WIDTH-CRAFT_WIDTH)*0.5),((HEIGTH-CRAFT_HEIGTH)*0.5)))
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
MAIN_ENGINE_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Sounds', 'main_engines.mp3'))



r1 = Rocket()
session = Game()


craft = pygame.transform.rotate(pygame.transform.scale(CRAFT_IMAGE, (CRAFT_WIDTH, CRAFT_HEIGTH)), r1.angle)


# ser = serial.Serial("/dev/ttyAMA0", 115200)
# serialFromArduino.flush()



while session.running:
    clock.tick(FPS)    
    check_events()     
    r1.update  # Updates the rocket properties like velocity, altitude etc.
    draw_window()


pygame.quit()