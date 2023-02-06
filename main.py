from pygame import mixer


pygame.mixer.pre_init(48000, -16, 2, 1024) #was 1024
pygame.mixer.init()

mainenginesound = pygame.mixer.Sound("/Sounds/main_engines.mp3")

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEWHEEL:
            mainenginesound.play(-1)

