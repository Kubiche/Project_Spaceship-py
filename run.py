import os
import serial
import pygame
import constants as const
from rocket import Rocket



WIN = pygame.display.set_mode((WIDTH, HEIGTH))
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
            continue        
        if event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button down")
            r1.angle = 90
            r1.acceleration = 20
            global craft
            craft = pygame.transform.rotate(pygame.transform.scale(CRAFT_ENGINE_ON_IMAGE, (CRAFT_WIDTH, CRAFT_HEIGTH)), r1.angle)
            MAIN_ENGINE_SOUND.play(-1)
            MAIN_ENGINE_SOUND.set_volume(1)
            r1.engine_on = True
            continue
        if event.type == pygame.JOYBUTTONUP:
            print("Joystick button up")
            craft = pygame.transform.rotate(pygame.transform.scale(CRAFT_IMAGE, (CRAFT_WIDTH, CRAFT_HEIGTH)), r1.angle)
            MAIN_ENGINE_SOUND.stop()
            r1.engine_on = False
            r1.acceleration = -0.01
            continue
        if event.type == pygame.KEYDOWN:
            print("Key press detected")
            if event.key == pygame.K_ESCAPE:
                print("Escape key pressed")
                session.running = False
                continue
            if event.key == pygame.K_k or event.type == pygame.JOYBUTTONDOWN:  # Engine ON
                print("k key pressed")
                r1.angle = 90
                r1.acceleration = 20
                # global craft
                craft = pygame.transform.rotate(pygame.transform.scale(CRAFT_ENGINE_ON_IMAGE, (CRAFT_WIDTH, CRAFT_HEIGTH)), r1.angle)
                MAIN_ENGINE_SOUND.play(-1)
                MAIN_ENGINE_SOUND.set_volume(1)
                r1.engine_on = True
                continue
            if event.key == pygame.K_l or event.type == pygame.JOYBUTTONUP:  # Engine OFF
                print("l key pressed")
                craft = pygame.transform.rotate(pygame.transform.scale(CRAFT_IMAGE, (CRAFT_WIDTH, CRAFT_HEIGTH)), r1.angle)
                MAIN_ENGINE_SOUND.stop()
                r1.engine_on = False
                r1.acceleration = -0.01
                continue
            if event.key == pygame.K_LEFT:
                if r1.engine_on == True:
                    r1.angle += 1
                    craft = pygame.transform.rotate(pygame.transform.scale(CRAFT_ENGINE_ON_IMAGE, (CRAFT_WIDTH, CRAFT_HEIGTH)), r1.angle)
                    continue
            if event.key == pygame.K_RIGHT:
                if r1.engine_on == True:
                    r1.angle -= 1
                    craft = pygame.transform.rotate(pygame.transform.scale(CRAFT_ENGINE_ON_IMAGE, (CRAFT_WIDTH, CRAFT_HEIGTH)), r1.angle)
                    continue



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
print("Joystick Count:", joystick_count)

joystick = pygame.joystick.Joystick(0)
joystick.init()
print("Joystick:", joystick.get_name())
# Sound instances
MAIN_ENGINE_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Sounds', 'main_engines.mp3'))



r1 = Rocket()
session = Game()


craft = pygame.transform.rotate(pygame.transform.scale(CRAFT_IMAGE, (CRAFT_WIDTH, CRAFT_HEIGTH)), r1.angle)


# ser = serial.Serial("/dev/ttyAMA0", 115200)
# serialFromArduino.flush()


if __name__ == '__main__':
    while session.running:
        clock.tick(FPS)    
        check_events()     
        r1.update()  # Updates the rocket properties like velocity, altitude etc.
        draw_window()
        print("Velocity:", r1.velocity)

    pygame.quit()
