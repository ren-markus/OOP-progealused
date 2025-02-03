import sys
import pygame

def check_events():
    """Check keyboard events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.moving_right = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player.moving_right = False
                
            
def update_screen(game_settings, screen, player):
    """Update image on screen and draw new screen"""
    # add screen backgroud
    screen.fill(game_settings.bg_color)
    # add player to screen
    player.blit_me()
    # display the last screen
    pygame.display.flip()
    