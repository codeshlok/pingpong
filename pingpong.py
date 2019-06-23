import pygame
import time

pygame.init()
screen = pygame.display.set_mode((900,700))

finished = False # 0 < 10 - > True/ 10<10 ->False
x = 0
y = 350
x2 = 815
y2 = 350
#print pygame.K_SPACE
playerImage = pygame.image.load("images/Player1.png")
playerImage = pygame.transform.scale(playerImage, (105,160))
playerImage = playerImage.convert_alpha()

playerImage2 = pygame.image.load("images/Player1.png")
playerImage2 = pygame.transform.scale(playerImage2, (105,160))
playerImage2 = playerImage2.convert_alpha()

frame = pygame.time.Clock()

while finished == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    pressedKeys = pygame.key.get_pressed()

    if pressedKeys[pygame.K_UP] == 1:
        y -= 5
    if pressedKeys[pygame.K_DOWN] == 1:
        y += 5
    if pressedKeys[pygame.K_w] == 1:
        y2 -= 5
    if pressedKeys[pygame.K_s] == 1:
        y2 += 5
    if pressedKeys[pygame.K_RIGHT] == 1:
        x += 5
    if pressedKeys[pygame.K_LEFT] == 1:
        x -= 5
    if pressedKeys[pygame.K_d] == 1:
        x2 += 5
    if pressedKeys[pygame.K_a] == 1:
        x2 -= 5
    dividor = pygame.Rect(450, 0, 20, 900)
    color = (255,255,255)
    black =(0,0,0)
    screen.fill(black)
    screen.blit(playerImage,(x,y))
    screen.blit(playerImage2,(x2, y2))
    pygame.draw.rect(screen, color, dividor)
    pygame.display.flip()
    frame.tick(90) #FPS Limit
    if x + 65 >= 450:
        x = x - 400
    if x2 <= 450:
        x2 = x2 + 400
    if x <= -35:
        x = x + 200
    if x2 >= 845:
        x2 = x2 - 200
    if y >= 590:
        y = y - 295
    if y2 >= 590:
        y2 = y2 - 295
    if y <= -45:
        y = y + 295
    if y2 <= -45:
        y2 = y2 + 295