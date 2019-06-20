import pygame

pygame.init()
screen = pygame.display.set_mode((900,700))

finished = False # 0 < 10 - > True/ 10<10 ->False
x = 0
y = 350
x2 = 890
y2 = 350
#print pygame.K_SPACE

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
    if pressedKeys[pygame.K_SPACE] == 1:
        x += 10
    paddle = pygame.Rect(x, y, 10, 80)
    paddle2 = pygame.Rect(x2, y2, 10, 80)
    color = (255,255,255)
    black =(0,0,0)
    screen.fill(black)
    pygame.draw.rect(screen, color, paddle)
    pygame.draw.rect(screen, color, paddle2)
    pygame.display.flip()
