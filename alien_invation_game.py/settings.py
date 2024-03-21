import pygame


class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 800
        self.screen_height = 500
        self.background = (230,230,230)
        
        #ship's settings
        self.ship_speed = 5
        self.ship_limit = 3
 
        ##Adding the bullet setting
        self.bullet_speed = 2.5 
        self.bullet_width = 5
        self.bullet_height= 5
        self.bullet_color = (30,30,30)
        self.bullets_allowed =50

        #alien_settings 
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10

        #fleet direction represents right; -1 represents left.
        self.fleet_direction = 1


        from settings import Settings
        