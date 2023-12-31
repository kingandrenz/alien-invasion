import pygame


class Ship:
    """ A class to manage the ship"""

    def __init__(self, ai_game):
        """ Intialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings= ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #Load the ship Image and get its rect.
        """self.image = pygame.image.load('images/ship1.bmp')
        self.rect = self.image.get_rect()
        """
        self.image = pygame.image.load('images/ship1.bmp')
        self.image = pygame.transform.scale(self.image, (self.settings.ship_width, self.settings.ship_height))
        self.rect = self.image.get_rect()

        #start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal positio
        self.x = float(self.rect.x)

        #movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Updates the ships's position based on the movement flag."""
        #update the ship x value not the rect

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        if self.moving_left and self.rect.left > 0 :
            self.x -= self.settings.ship_speed

        #update rect object from self.x.
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at the current location"""
        self.screen.blit(self.image, self.rect)
