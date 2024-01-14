import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))
x = 10
y = 10
w = 100
h = 100

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    color = (255, 255, 255)

    pygame.draw.rect(win, (255, 0, 0), (100, 50, 50, 50))
    pygame.display.update()
