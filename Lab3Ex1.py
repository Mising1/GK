import pygame
import math


pygame.init()

width = 600
height = 600
r = 150

screen = pygame.display.set_mode([width, height])


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


center_x, center_y = 300, 300
angle = 2 * math.pi / 7

vertices = [
    (center_x + r * math.cos(i * angle), center_y + r * math.sin(i * angle))
    for i in range(7)
]


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    pygame.draw.polygon(screen, BLACK, vertices)

    pygame.display.flip()

pygame.quit()
