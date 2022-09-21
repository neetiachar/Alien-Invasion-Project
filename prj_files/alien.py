# Initialize alien related modules, alien py
import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting position"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien image and set its rect property
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # Let each alien appear near the upper left corner of the screen
        self.rect.x = self.rect.width  # Left margin set to alien width
        self.rect.y = self.rect.height  # The top margin is set to alien height

        # Store the exact location of aliens
        self.x = float(self.rect.x)  # It is mainly used for back calculation

    def blitme(self):
        """Draw aliens at the specified location"""
        self.screen.blit(self.image, self.rect)

    def check_edge(self):
        """If the alien is on the edge of the screen, return True"""
        screen_rect = self.screen.get_rect()
        # If the edge of the alien is greater than or equal to the right edge of the screen
        if self.rect.right >= screen_rect.right:
            return True
        # If the edge of the alien is less than or equal to the left edge of the screen, i.e. coordinate 0
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move aliens to the right"""
        self.x += (self.ai_settings.alien_speed *
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x