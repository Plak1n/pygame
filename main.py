import os
import time
import pygame

from const import BG_SPEED, PLAYER_SPEED, PLAYER_CROUCH_SPEED, PLAYER_HEIGHT_CROUCHING, PLAYER_HEIGHT_STANDING


pygame.init()
screen = pygame.display.set_mode((1366,768))
pygame.display.set_caption("First_pygame_project")
icon = pygame.image.load("img\\chess_icon.png")
pygame.display.set_icon(icon)

background = pygame.image.load("img/background.png")
background = pygame.transform.scale(background,(1366,768))

l1 = pygame.image.load("img/player_left1.png")
l2 = pygame.image.load("img/player_left2.png")
l3 = pygame.image.load("img/player_left3.png")
l4 = pygame.image.load("img/player_left4.png")

r1 = pygame.image.load("img/player_right1.png")
r2 = pygame.image.load("img/player_right2.png")
r3 = pygame.image.load("img/player_right3.png")
r4 = pygame.image.load("img/player_right4.png")

walk_left = [l1, l2, l3, l4]

walk_right = [r1, r2, r3, r4]


for i in range(len(walk_left)):
    walk_left[i] = pygame.transform.scale(walk_left[i],(100,100))
    walk_right[i] = pygame.transform.scale(walk_right[i],(100,100))

loops = 0
player_anim_count = 0
bg_x = 0
bg_x1 = 1366

player_x = 150
player_y = 550
is_jumped = False
jump_high = 15

# Sound
# bg_sound = pygame.mixer.Sound("path to sound")
# bg_sound.play(-1)

running = True
while running:
    loops +=1
    
    screen.blit(background, (bg_x,0))
    screen.blit(background, (bg_x1,0))
    
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a]:
        if keys[pygame.K_s]:
            screen.blit(walk_left[player_anim_count], (player_x, player_y + PLAYER_HEIGHT_STANDING - PLAYER_HEIGHT_CROUCHING))
        else:
            screen.blit(walk_left[player_anim_count],(player_x,player_y))
    else: 
        if keys[pygame.K_s]:
            screen.blit(walk_right[player_anim_count], (player_x, player_y + PLAYER_HEIGHT_STANDING - PLAYER_HEIGHT_CROUCHING))
        else:
            screen.blit(walk_right[player_anim_count],(player_x, player_y))

    
    if keys[pygame.K_d] and player_x <=1250 and not keys[pygame.K_s]:
        player_x += PLAYER_SPEED
    elif keys[pygame.K_a] and player_x >= 20 and not keys[pygame.K_s]:
        player_x -= PLAYER_SPEED

    
    if not is_jumped:
        if keys[pygame.K_SPACE] or keys[pygame.K_w]:
            is_jumped = True
    else:
        if jump_high >= -15:
            if jump_high > 0:
                player_y -=(jump_high ** 2)/3
            else:
                player_y += (jump_high **2 )/3
            jump_high -=1.5
        else:
            is_jumped = False
            jump_high = 15
        
    
    
    if player_anim_count == 3:
        player_anim_count = 0 
    elif loops%7 ==0:
        player_anim_count +=1
    
    bg_x -= BG_SPEED
    bg_x1 -= BG_SPEED
    
    if bg_x <= -1366:
        bg_x = 0
    if bg_x1 <= 0:
        bg_x1 = 1366
    
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                player_y += PLAYER_HEIGHT_STANDING - PLAYER_HEIGHT_CROUCHING
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                player_y -= PLAYER_HEIGHT_STANDING - PLAYER_HEIGHT_CROUCHING
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    
if __name__ == "__main__":
    pass