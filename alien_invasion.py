import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game asset and behaviour."""

    def __init__(self):
        """Initialize the game, and create game resource."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        # Set the background color directly in __init__
        #self.bg_color = (230, 230, 230)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self._update_screen()


    def _check_events(self):
        # Respond  to keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        #move the ship to the right
                        self.ship.rect.x += 1
                    elif event.key == pygame.K_LEFT:
                        #Move the ship to the left.
                        self.ship.rect.x += 1


    def _update_screen(self):
         #Update image on the screen, and flip to the new screen
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # Make the most recently drawn screen visible
            pygame.display.flip()


if __name__ == "__main__":
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()

