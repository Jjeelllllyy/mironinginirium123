import pygame

class Circle:
    def __init__(self, color, x, y, rad):
        self.color = color
        self.x = x
        self.y = y
        self.rad = rad
        self.is_jump = False
        self.jump_counter =15



    def draw(self):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.rad)

    def move_by_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= 3

        if keys[pygame.K_RIGHT]:
            self.x += 3

        if keys[pygame.K_UP]:
            self.y -= 3

        if keys[pygame.K_DOWN]:
            self.y += 3


    def jump(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.is_jump = True
        if self.if_jump:
            if self.jump_counter >= -15:
                self.y -= self.jump_counter
                self.jump_counter -= 2
            else:
                self.jump_counter = 15
                self.is_jump = False






pygame.init()
width = 500
height = 500
win = pygame.display.set_mode((width, height))

x = 0
y = 0

circle = Circle((255, 255, 0), 0, 0, 30)

FPS = 60
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    win.fill((255, 255, 255))

    circle.draw()
    circle.move_by_keys()
    circle.jump()
    pygame.display.update()
    clock.tick(FPS)
    pygame.time.delay(10)