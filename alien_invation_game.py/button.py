import pygame.font

class Button:
    """A class to build the buttons in the game """

    def __init__(self,ai_game,msg):
        """Initialize the button attributes"""
        self.screen =  ai_game.self.screen 
        self.screen_rect = self.screen.get_rect()

        #set the dimensions and the button properties 
        self.width, self.height = 200, 50
        self.button_color = (0,135,0)
        self.text_color = (250,250,250)
        

        #build the button's rect object and center it 
        self.rect = pygame.Rect(0,0,self.width,self.height )
        self.rect.center = self.screen_rect.center

        #The button message needs to be prepped only once 
        self._prep_msg(msg) 

    def _prep_msg(self,msg):
        """Turn msg into a rendered image and the center text on the button"""
        self.msg_image = self.font.render (msg,True,self.text_color,
                                           self.button_color)
        
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button (self):
        """Draw blank button and then draw messages"""
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)

