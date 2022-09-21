# Score statistics and rendering for image printing module, scoreboard py
import pygame.ftfont
from pygame.sprite import Group
from ship import Ship


class Scoreboard:
    """Class that displays score information"""

    def __init__(self, ai_settings, screen, stats):
        """Initialize the attributes involved in displaying scores"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Font setting for displaying score information
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare to display the image of the current score and the highest score
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Render scores as images"""
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        # Displays the score in the upper right corner
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Converts the highest score to a rendered image"""
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format((high_score))
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)

        # Place the highest score in the center of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = 20

    def prep_level(self):
        """Convert levels to images"""
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.ai_settings.bg_color)

        # Put the grade below the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """Show how many ships are left"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)



    def show_score(self):
        """Show score"""
        self.screen.blit(self.score_image, self.score_rect) # Displays the current score
        self.screen.blit(self.high_score_image, self.high_score_rect)   # Show highest score
        self.screen.blit(self.level_image, self.level_rect)
        # Drawing spacecraft
        self.ships.draw(self.screen)