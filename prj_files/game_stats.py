# Module for storing game statistics, game_stats.py
class GameStats:
    """Track game statistics"""

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False  # The game has just started and is active
        self.high_score = 0  # The highest score should not be reset at any time

    def reset_stats(self):
        """Initialize information that may change during game operation"""

        # Count the number of ships remaining in the game
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0  # Count game scores
        self.level = 1  # Count the level information of the game
