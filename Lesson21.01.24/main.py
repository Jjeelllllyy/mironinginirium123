import pygame
pygame.init()
win = pygame.display.set_mode((600, 400))
x = 100
y = 50

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    x = x + 150

    if x > 600:
        x = 0


    win.fill((255, 255, 255))
    pygame.draw.rect(win, (255,255, 0), (x, y, 100, 150))
    pygame.display.update()
    pygame.time.delay(-500)