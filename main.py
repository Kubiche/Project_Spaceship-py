# This is still under construction =(
# Created by: JC 
import os
import serial
import pygame
from rocket import Rocket


WIDTH,HEIGTH = 1920, 1080
WIN = pygame.display.set_mode((WIDTH, HEIGTH), pygame.HWSURFACE | pygame.DOUBLEBUF)
SPACE_GREY = (101,115,126)
FPS = 60
pygame.display.set_caption("CURIOSITY SPACE PROGRAM")
global craft





# Images
CRAFT_WIDTH, CRAFT_HEIGTH = 400, 200
CRAFT_IMAGE = pygame.image.load(os.path.join('Assets', 'Images', 'craft.png'))
CRAFT_OPEN_DOOR_IMAGE = pygame.image.load(os.path.join('Assets', 'Images', 'craft_open_door.png'))
CRAFT_ENGINE_ON_IMAGE = pygame.image.load(os.path.join('Assets', 'Images', 'craft_engine_on.png'))


class Game:
    def __init__(self,running = True):
        self.running = running
        


def get_events():
    global craft
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            session.running = False
        if event.type == pygame.JOYDEVICEADDED:
            Panel1 = pygame.joystick.Joystick(0)
            panel1_instance_id = Panel1.get_instance_id()
            print("Joystick Added")
            print(panel1_instance_id)
            ser = serial.Serial("/dev/serial/by-id/usb-SparkFun_Panel_HIDBF-if00", 115200)
            ser.flush()                       
        if event.type == pygame.JOYBUTTONDOWN:
            print("Joystick Button Pressed")
            r1.angle = 90
            r1.acceleration = 15
            r1.altitude += 10                
            #global craft
            craft = pygame.transform.rotate(pygame.transform.scale(CRAFT_ENGINE_ON_IMAGE, (CRAFT_WIDTH, CRAFT_HEIGTH)), r1.angle)
            MAIN_ENGINE_SOUND.play(-1)
            r1.engine_on = True
            send_panel_command(2,1,True) # send a LED 1 ON command
        if event.type == pygame.JOYBUTTONUP:
            print("Joystick Button Depressed")
            craft = pygame.transform.rotate(pygame.transform.scale(CRAFT_IMAGE, (CRAFT_WIDTH, CRAFT_HEIGTH)), r1.angle)
            MAIN_ENGINE_SOUND.stop()
            r1.engine_on = False
            r1.acceleration = -10
            send_panel_command(2,1,False) # send a "LED 1 OFF" command     
        if event.type == pygame.KEYDOWN:
            print("Key press detected")
            if event.key == pygame.K_ESCAPE:
                print("Escape key pressed")
                session.running = False
            if event.key == pygame.K_k:  # Engine ON
                print("k key pressed")
                r1.angle = 90
                r1.acceleration = 15
                r1.altitude += 10                
                #global craft
                craft = pygame.transform.rotate(pygame.transform.scale(CRAFT_ENGINE_ON_IMAGE, (CRAFT_WIDTH, CRAFT_HEIGTH)), r1.angle)
                MAIN_ENGINE_SOUND.play(-1)
                r1.engine_on = True
                send_panel_command(2,1,True) # send a LED 1 ON command
            if event.key == pygame.K_l:  # Engine OFF
                print("l key pressed")
                craft = pygame.transform.rotate(pygame.transform.scale(CRAFT_IMAGE, (CRAFT_WIDTH, CRAFT_HEIGTH)), r1.angle)
                MAIN_ENGINE_SOUND.stop()
                r1.engine_on = False
                r1.acceleration = -10
                send_panel_command(2,1,False) # send a "LED 1 OFF" command  
            if event.key == pygame.K_LEFT:
                if r1.engine_on == True:
                    r1.angle += 1
                    craft = pygame.transform.rotate(pygame.transform.scale(CRAFT_ENGINE_ON_IMAGE, (CRAFT_WIDTH, CRAFT_HEIGTH)), r1.angle)
            if event.key == pygame.K_RIGHT:
                if r1.engine_on == True:
                    r1.angle -= 1
                    craft = pygame.transform.rotate(pygame.transform.scale(CRAFT_ENGINE_ON_IMAGE, (CRAFT_WIDTH, CRAFT_HEIGTH)), r1.angle)



def draw_window():
    
    WIN.fill(SPACE_GREY)
    WIN.blit(craft, (((WIDTH-CRAFT_WIDTH)*0.5),((HEIGTH-CRAFT_HEIGTH)*0.5)))
    pygame.display.update()

def send_panel_command(command_type, command, value): # command types are 0-lamp test 1-show in led-bar 2-control led | device number: bar or led number | value: 0-10 for bar or on\off for led
    command_string = "{:1.0f},{:1.0f},{:1.0f}\n".format(command_type,command,value)    
    ser.write(command_string.encode())
    

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
#joystick_count = pygame.joystick.get_count()

# Sound instances
MAIN_ENGINE_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Sounds', 'main_engines.mp3'))

r1 = Rocket()
session = Game()

craft = pygame.transform.rotate(pygame.transform.scale(CRAFT_IMAGE, (CRAFT_WIDTH, CRAFT_HEIGTH)), r1.angle)

while session.running:
    clock.tick(FPS)    
    get_events()     
    r1.update()  # Updates the rocket properties like velocity, altitude etc.
    draw_window()
    #print(r1.velocity)


pygame.quit()