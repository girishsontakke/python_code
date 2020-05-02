import pygame
import time

pygame.init()

width = 800
height = 600

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)

dis = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake game by Girish')

x1 = width/2
y1 = height/2

x1_change = 0
y1_change = 0

game_over = False
clock = pygame.time.Clock()
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -10
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = 10
                x1_change = 0
    x1+= x1_change
    y1+= y1_change
    dis.fill(black)

    # argument is x,y, width, height
    pygame.draw.rect(dis, blue, [x1, y1, 10, 10])
    pygame.display.update()
    clock.tick(30)
pygame.quit()
quit()
