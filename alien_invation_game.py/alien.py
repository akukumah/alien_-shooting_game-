import pygame
from pygame.sprite import  Sprite

class Alien( Sprite):
    """a class to represent a single alien in the fleet"""

    def __init__(self, ai_game):
        """initialise the alien and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #load the alien image and set its rect attributes 
        self.image = pygame.image.load('C:/Users/emma/Desktop/python_work/alien_invation_game.py/images/alien.bmp') 
        self.rect = self.image.get_rect()

        #start each alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height 

        #store the alien's excat horizontal position 
        self.x= float(self.rect.x)

    def check_edges(self):
        """return True if alien is at egde of the screen""" 
        screen_rect = self.screen.get_rect()
        return(self.rect.right >= screen_rect.right) or (self.rect.left <= 0)   

    def update (self):
        """Move the alien to the right"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction 
        self.rect.x = self.x     

