##now i will create the bullet class 
import pygame
from pygame.sprite import  Sprite

class Bullet(Sprite):
    """A class to manage the bullets fired from the ship"""

    def __init__(self, ai_game ): 
        """ Creates a bullet object at the ship's current position"""
        super( ). __init__()
        self.screen = ai_game.screen 
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        ##create a bullet rect  at (0,0) and then set coerrect position
        self.rect = pygame.Rect(0,0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #store the bullet's position as a float 
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen""" 
        #update the exact position of the bullet
        self.y -= self.settings.bullet_speed

        #update the rect positon 
        self.rect.y = self.y

    def draw_bullets(self):
        """Draws the bullets to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)       

      
