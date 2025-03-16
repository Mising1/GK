import pygame

pygame.init()

WIDTH, HEIGHT = 600,600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("pygame")

BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

screen.fill(WHITE)

pygame.draw.circle(screen, BLACK, (100, 100), 50)
pygame.draw.rect(screen, YELLOW, (75, 75, 50, 50))

pygame.draw.polygon(screen, GREEN, [(250, 50), (350, 50), (350, 100), (300, 75), (250, 100)])

pygame.draw.polygon(screen, BLUE, [(100, 250), (125, 200), (75, 200)])
pygame.draw.rect(screen, BLUE, (60, 250, 80, 50))
pygame.draw.polygon(screen, BLUE, [(100, 300), (125, 345), (75, 345)])

pygame.draw.line(screen, RED, (250, 200), (350, 200), 5)
pygame.draw.line(screen, RED, (350, 200), (250, 300), 5)
pygame.draw.line(screen, RED, (250, 300), (350, 300), 5)

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
