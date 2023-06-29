import os
import pygame

pygame.init()
screen = pygame.display.set_mode((1024,768))
screen.fill((70, 44,133))
pygame.display.set_caption("First_pygame_project")
icon = pygame.image.load("img\\2992645_chess_computer_strategy_tactic_technology_icon.png")
pygame.display.set_icon(icon)

square = pygame.Surface(size=(100,100))
square.fill("black")

red_hat_font = pygame.font.Font("fonts\\RedHatMono-VariableFont_wght.ttf", 30)
text_surface = red_hat_font.render("Hello World", True, "Black")

running = True
while running:
    
    
    pygame.display.update()
    screen.blit(source=square, dest=(0,0))
    pygame.draw.circle(surface=screen, color="Red", center=(0,0), radius=20)
    screen.blit(text_surface, (300,100))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                screen.fill((70,44,133))  

if __name__ == "__main__":
    pass