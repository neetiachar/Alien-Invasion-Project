# Initialize the module of the bullet py
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class used to manage the firing of bullets from a spacecraft"""

    def __init__(self, ai_settings, screen, ship):
        """Add a bullet object to the position of the ship"""
        super(Bullet, self).__init__()
        self.screen = screen

        # Create a rectangle representing the bullet at (0, 0) and set the correct position.
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx  # Set the centerx of the bullet to the centerx of the ship
        self.rect.top = ship.rect.top  # Set the top of the bullet to the top of the ship

        # Store bullet position in decimal
        self.y = float(self.rect.y)  # Store the y coordinate of the bullet in decimal places

        self.color = ai_settings.bullet_color  # Sets the color of the bullet
        self.speed = ai_settings.bullet_speed  # Set the speed of the bullet

    def update(self):
        """Move the bullet up"""
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw bullets on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)