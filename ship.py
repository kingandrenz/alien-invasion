import pygame

class Ship:
    """ A class to manage the ship"""

    def __init__(self, ai_game):
        """ Intialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #Load the ship Image and get its rect.
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()

        #start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        #movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Updates the ships's position based on the movement flag."""
        if self.moving_right:
            self.rect.x += 1

        if self.moving_left:
            self.rect.x -= 1

    def blitme(self):
        """Draw the ship at the current location"""
        self.screen.blit(self.image, self.rect)
