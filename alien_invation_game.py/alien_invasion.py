import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet    
from alien import Alien
from time import sleep
from game_stats import GameStats 



class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        #creating an instance to store game stats 
        self.stats = GameStats(self)

        #start alien invasion in an inactive state 
        self.game_active = False 

    
        

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self. _check_events()
            
            
            if self.game_active:
                self.bullets.update()
                self._update_aliens()
                self.ship.update()
            
            
            self.clock.tick(60)
            self._check_bullet_alien_collisions()
            self. _update_screen()
            
            
    
    def _check_events(self):
        """Responds to key presses and mouse responds"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                 self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                 self._check_keyup_events(event)     
                    

    def _check_keydown_events(self,event):
            """Responds to keypresses"""
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = True
            #adding a shortcut to exist the game by pressing q    
            elif event.key == pygame.K_q:
                 sys.exit()
            elif event.key == pygame.K_SPACE:
                 self._fire_bullet()         

    def _check_keyup_events(self,event):
            """Responds to key releases"""
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = False  

    def _fire_bullet(self):
         """creates a new bullet and add it to the bullet group.""" 
         if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)  


    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()

        #get ride of bullets that has disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

        if not self.aliens:
             #Destory existing bullets and create new fleet.
             self .bullets.empty()
             self._create_fleet()

        

    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        # Remove any bullets and aliens that have collided.
        collision =pygame.sprite.groupcollide( self.bullets, self.aliens, True, True)

        if not self.aliens:
            # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()
        
                                      

    def _update_screen(self):
        """Updates new images on the screen and flips to the new screen"""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.background)
        for  bullet in self.bullets.sprites():
             bullet.draw_bullets()
        self.ship.blitme()
        self.aliens.draw(self.screen)

        #Draw the play button if the game is inactive 
        self.game_active = True
            

        pygame.display.flip()
  


    def _create_fleet(self):
         """create a fleet of aliens"""
         #make an alien
         #create  an lien and keep addiing aliens until there is no room left 
         #spacing between aliens is one width  and one alien height. 
         alien = Alien(self)
         alien_width , alien_height = alien.rect.size                    

         current_x,current_y = alien_width, alien_height
         while current_y < (self.settings.screen_height - 3 * alien_height):   
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x,current_y)
                current_x += 2*alien_width

            #finish a row:  reset x value, and increment y value. 
            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien( self,x_position, y_position):
         """create an alien and places it in the fleet"""
         new_alien = Alien(self)
         new_alien.x = x_position
         new_alien.rect.x = x_position
         new_alien.rect.y = y_position
         self.aliens.add(new_alien)     

    def _update_aliens(self):
         """check if the fleet is at the egde then update positions"""
         self._check_fleet_edges()
         self.aliens.update()

         #look for alien-ship collisions.
         if pygame.sprite.spritecollideany(self.ship, self.aliens):
              self._ship_hit()

         #look for aliens hitting the buttom of the screen
         self._check_aliens_bottom()    

    def _check_fleet_edges(self):
         """Respond apprioprartely if any aliens have reached an edge"""
         for alien in self.aliens.sprites():
              if alien.check_edges():
                   self._change_fleet_direction()
                   break 

    def _change_fleet_direction(self):
         """drops the antire fleet and chmage their direction"""
         for alien in self.aliens.sprites():
              alien.rect.y += self.settings.fleet_drop_speed
         self.settings.fleet_direction *= -1                     


    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left > 0:
            # Decrement ships_left.
            self.stats.ships_left -= 1

            # Get rid of any remaining bullets and aliens.
            self.bullets.empty()
            self.aliens.empty()

            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()

            # Pause.
            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)


    def _check_aliens_bottom(self):
         """Check if any alien have reached the buttom"""
         for alien in self.aliens.sprites():
              if alien.rect.bottom >= self.settings.screen_height:
                   self._ship_hit()
                   break     

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()