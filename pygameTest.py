import pygame, time, sys

screen = pygame.display.set_mode((640,480))

expectedDeltaTime = 1/30

prevTime = time.time()

while True:
    deltaTime = time.time() - prevTime
    prevTime = time.time()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()