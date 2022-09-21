# For information about initializing game buttons, see button py
import pygame.ftfont  # The module can render text to the screen


class Button:

    # message is the text we want to display in the button
    def __init__(self, ai_settings, screen, message):
        """Initialize button properties"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Set the size and other properties of the button
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)  # The button is set to green
        self.text_color = (255, 255, 255)  # The text content is set to white
        self.font = pygame.font.SysFont(None, 48)  # None indicates the default font and 48 indicates the font size

        # Create a rect object for the button and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Create a label for the button
        self.prep_msg(message)

    def prep_msg(self, message):
        """take message Render as an image and center it in the button"""
        self.msg_image = self.font.render(message, True, self.text_color,
                                          self.button_color)    # Convert text to image
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw a button before you draw text"""
        self.screen.fill(self.button_color, self.rect)  # Draw button
        self.screen.blit(self.msg_image, self.msg_image_rect)   # Draw text