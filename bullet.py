import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Bullet for the space ship"""
    def __init__(self, ai_game):
        """intialize the bullet object at the ship current position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #craete a bullet at (0, 0) and the set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # store the bullet's position as decimal
        self.y = float(self.rect.y)
