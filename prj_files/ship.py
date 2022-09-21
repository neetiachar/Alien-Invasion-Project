# Initialize the relevant class of the spacecraft, ship py
import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        """Initialize the spacecraft and set its initial position"""
        super(Ship, self).__init__()
        self.screen = screen
        self.moving_right = False  # Can I move the sign to the right
        self.moving_left = False  # Can I move the sign to the left
        self.ai_settings = ai_settings

        # Load the ship image and obtain its circumscribed rectangle
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()  # Get the size attribute of the image and save it
        self.screen_rect = screen.get_rect()  # Get the size attribute of the screen and save it

        # Put each new ship in the center of the bottom
        self.rect.centerx = self.screen_rect.centerx  # Obtain the midpoint data of the x-axis of the screen and assign it to rect
        self.rect.bottom = self.screen_rect.bottom  # Get the bottom position data of the screen and assign it to rect

        # Store decimals in the attribute center of the spacecraft
        self.center = float(self.rect.centerx)  # A new decimal storage property

    def blitme(self):
        """Draw the spaceship at the specified location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Check the status of the flag, if the flag is True Just move the ship"""

        # Update the center value of the spacecraft instead of the rect value
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed

        # According to self The value of center updates self Value of centerx
        self.rect.centerx = self.center

    def center_ship(self):
        """Center the ship on the screen"""
        self.center = self.screen_rect.centerx