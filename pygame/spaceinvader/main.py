import pygame
import random
import math
from pygame import mixer



pygame.init()
# create screen
screen = pygame.display.set_mode((800, 600))

#sound
backgroundSound = mixer.Sound("background.wav")
backgroundSound.play(-1)
bulletSound = mixer.Sound("laser.wav")
explosionSound = mixer.Sound("explosion.wav")

#background image
backgroundImg = pygame.image.load("background.png")
backgroundImg = pygame.transform.scale(backgroundImg, (800, 600))

# Title and Icon
image = pygame.image.load('spaceship.png')
pygame.display.set_caption("Space Invader")
pygame.display.set_icon(image)

# player
playerImg = pygame.image.load("spaceship.png")
playerImg = pygame.transform.scale(playerImg, (70, 70))
playerX = 400
playerY = 500
playerX_change = 0

# Enemy
enemyImg = pygame.image.load("enemy.png")
enemyImg = pygame.transform.scale(enemyImg, (60, 60))
enemyX = random.randint(0, 700)
enemyY = random.randint(20, 50)
enemyX_change = 3
enemyY_change = 60
enemyMissSpeed = 1


# bullet
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = playerY
bulletY_change = 10
bulletX_change = 0
bullet_fire = False


# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
scoreX = 10
scoreY = 10

#Game over text
over_text = pygame.font.Font('freesansbold.ttf', 64)

def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def bulletFire(x, y):
    global bullet_fire
    bullet_fire = True
    screen.blit(bulletImg, (x+18, y+20))

def iscollision(x1, y1, x2, y2):
    distance = math.sqrt(math.pow((x1-x2), 2) + math.pow((y1-y2), 2))
    if distance < 27:
        return True
    
    return False

def show_score(x, y):
    score = font.render("score: " + str(score_value), True, (255, 255, 255))
    # text, bool, color
    screen.blit(score, (x, y))

def gameover():
    game_over = over_text.render("GAME OVER", True, (255, 255, 255))
    screen.blit(game_over, (200, 300))


running = True
# game loop
while running:
    # RGB
    screen.fill((0, 0, 0))
    screen.blit(backgroundImg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                playerX_change = -3
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                playerX_change = 3
            if event.key == pygame.K_SPACE:
                if not bullet_fire:
                    bulletX = playerX
                    bulletFire(bulletX, bulletY)
                    bulletSound.play()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_change = 0

    # player movement
    playerX += playerX_change
    if playerX > 740:
        playerX = 740
    elif playerX < 0:
        playerX = 0

    # enemy movement
    enemyX += enemyX_change
    if enemyX > 740:
        enemyY += enemyY_change
        enemyX_change *= -1

    elif enemyX < 0:
        enemyY += enemyY_change
        enemyX_change *= -1

    if enemyY > 480:
        enemyY = 850
        gameover()

    if bulletY <= 0:
        bullet_fire = False
        bulletY = playerY
        if enemyX_change > 0 and enemyX_change < 6:
            enemyX_change += enemyMissSpeed
        elif enemyX_change < 0 and enemyX_change > -1.5:
            enemyX_change -= enemyMissSpeed

    if bullet_fire:
        bulletY -= bulletY_change
        bulletFire(bulletX, bulletY)
    
    collision = iscollision(enemyX, enemyY, bulletX, bulletY)

    if collision:
        score_value += 1
        enemyX = random.randint(0, 700)
        enemyY = random.randint(20, 50)
        bulletY = playerY
        bullet_fire = False
        explosionSound.play()
        if enemyX_change > 0:
            enemyX_change = 3
        else:
            enemyX_change = -3

    show_score(scoreX, scoreY)
    enemy(enemyX, enemyY)
    player(playerX, playerY)
    pygame.display.update()