import os
import pygame

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((1366,768))
screen.fill((70, 44,133))
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
bg_speed = 3

player_speed = 5
player_x = 150

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
        screen.blit(walk_left[player_anim_count],(player_x,550))
    else: 
        screen.blit(walk_right[player_anim_count],(player_x,550))
    
    if keys[pygame.K_d] and player_x <=1250:
        player_x += player_speed
    elif keys[pygame.K_a] and player_x >= 20:
        player_x -= player_speed
    
    
    
    if player_anim_count == 3:
        player_anim_count = 0 
    elif loops%7 ==0:
        player_anim_count +=1
    
    bg_x -= bg_speed
    bg_x1 -= bg_speed
    
    if bg_x <= -1366:
        bg_x = 0
    if bg_x1 <= 0:
        bg_x1 = 1366
    
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    
if __name__ == "__main__":
    pass