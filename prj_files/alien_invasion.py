# Main module, alien_invasion.py
import pygame  # It contains the functions required for game development
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    """Initialize the game and create a screen object"""
    pygame.init()  # Initialize and check whether the toolkit is complete
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))  # Create a window with a size of 800 * 600
    pygame.display.set_caption("Alien invasion")  # Set screen name
    play_button = Button(ai_settings, screen, "Play")
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    ship = Ship(ai_settings, screen)  # Create a spaceship
    bullets = Group()  # Create a group to store bullets
    aliens = Group()  # Create an alien group
    gf.create_fleet(ai_settings, screen, ship, aliens)  # Create alien groups
    # Start the main cycle of the game
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, sb,screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()  # Run program