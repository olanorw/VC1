version = "ALPHA-0.5.0-SNAPSHOT"
import pygame
import os

pygame.init()

SCREEN_WIDTH = 850
SCREEN_HEIGHT = 900

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('VC1')
icon_image = pygame.image.load('vc1.ico')
pygame.display.set_icon(icon_image)

font = pygame.font.SysFont("Tw Cen MT Condensed Extra Bold", 40)
release = pygame.font.SysFont("consolas", 10)

TEXT_COL = (255, 255, 255)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))
    
run = True
while run:
        
        screen.fill((52, 78, 91))
        
        draw_text(version, release, TEXT_COL, 0, 0)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        pygame.display.update()