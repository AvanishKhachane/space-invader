import pygame
import random

def collision(x1, x2, y1, y2, d):
    dis = pow(pow(x1 - x2, 2) + pow(y1 - y2, 2), 0.5)
    if dis < d:
        return True
    else:
        return False

def font_render(font_family, font_size, text, tf, rgb):
    font = pygame.font.Font(font_family, font_size)
    font_render = font.render(text, tf, (rgb[0], rgb[1], rgb[2]))
    return font_render


pygame.init()
# head
pygame.display.set_caption("space invader")
pygame.display.set_icon(pygame.image.load('space ship.png'))
# screen
screen = pygame.display.set_mode((800, 600))
# background
background_img = pygame.image.load('cartoon space.png')
# var
score = 0
score_value = font_render("freesansbold.ttf", 40, "Score: " + str(score), True, [255, 255, 255])
# player
player_img = pygame.image.load('spaceship.png')
playerX = 360
playerY = 480
player_change = 0

# ghosts
ghost_img = []
ghostX = []
ghostY = []
ghost_changeX = []
ghost_changeY = []
ghost_speedX = []
ghost_num = 6
for i in range(ghost_num):
    ghost_img.append(pygame.image.load('ghost.png'))
    ghostX.append(random.randint(0, 736))
    ghostY.append(random.randint(50, 150))
    ghost_changeX.append(1)
    ghost_changeY.append(64)
    ghost_speedX.append(1)

# bullet
bullet_img = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bullet_state = "ready"
bullet_fireX = 0
bullet_changeY = 2
bullet_changeX = 0


def blit_obj(obj, x, y, e):
    try:
        if obj == ghost_img:
            screen.blit(obj[e], (x[e], y[e]))
        else:
            screen.blit(obj, (x, y))
        code = "0"
    finally:
        code = "1"
        code = "exit code: " + code
        return code


def fire_bullet(xs, ys):
    global bullet_state
    bullet_state = "fire"
    blit_obj(bullet_img, xs, (ys - 20), 0)


game_over_state = False
run = True
while run:
    #            r  g  b
    screen.fill((40, 0, 40))
    blit_obj(background_img, 0, 0, 0)
    score_value = font_render("freesansbold.ttf", 60, "Score: " + str(score), True, [255, 255, 255])
    # player bounds
    playerX += player_change
    if playerX >= 736:
        playerX = 736
    if playerX <= 0:
        playerX = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            player_change = 0.5*(int(event.key == pygame.K_RIGHT) - int(event.key == pygame.K_LEFT))
            if event.key == pygame.K_SPACE:
                fire_bullet(playerX, bulletY)
                bullet_fireX = playerX

    for j in range(ghost_num):
        for ey in ghostY:
            if ghostY[j] >= 440:
                game_over = font_render("freesansbold.ttf", 40, "GAME OVER", True, [255, 255, 0])
                blit_obj(game_over, 320, 300, 0)
                game_over_state = True
                score = 0
                score_value = font_render("freesansbold.ttf", 60, "Score: " + str(score), True, [255, 255, 255])
                # player
                player_img = pygame.image.load('spaceship.png')
                playerX = 360
                playerY = 480
                player_change = 0

                # ghosts
                ghost_img = []
                ghostX = []
                ghostY = []
                ghost_changeX = []
                ghost_changeY = []
                ghost_num = 6
                for i in range(ghost_num):
                    ghost_img.append(pygame.image.load('ghost.png'))
                    ghostX.append(random.randint(0, 736))
                    ghostY.append(random.randint(50, 150))
                    ghost_changeX.append(1)
                    ghost_changeY.append(64)

                # bullet
                bullet_img = pygame.image.load('bullet.png')
                bulletX = 0
                bulletY = 480
                bullet_state = "ready"
                bullet_fireX = 0
                bullet_changeY = 2
                bullet_changeX = 0
                pass
            else:
                game_over_state = False
        if not(game_over_state):
            # ghost bounds
            ghostX[j] += ghost_changeX[j]
            if ghostX[j] <= 0:
                ghost_changeX[j] = ghost_speedX[j]
                ghostY[j] += ghost_changeY[j]
            elif ghostX[j] >= 736:
                ghost_changeX[j] = -1 * ghost_speedX[j]
                ghostY[j] += ghost_changeY[j]
            col = collision(ghostX[j], bullet_fireX, ghostY[j], bulletY, 46)
            # bullet_fire
            if bullet_state == "fire":
                bulletY -= bullet_changeY
                if col:
                    score += 1
                if bulletY <= 0 or col:
                    bullet_state = "ready"
                    bulletY = 480
                    if col:
                        ghostX[j] = random.randint(0, 736)
                        ghostY[j] = random.randint(50, 150)
                blit_obj(bullet_img, bullet_fireX, bulletY, 0)
            blit_obj(ghost_img[j], ghostX[j], ghostY[j], 0)
            blit_obj(player_img, playerX, playerY, 0)
            blit_obj(score_value, 10, 10, 0)
    pygame.display.update()
