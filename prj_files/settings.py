# Store game related setting information, settings py
class Settings:
    """Store all classes related to alien invasion"""

    def __init__(self):
        """Initialize game static settings"""
        # screen setting
        self.screen_width = 1200  # Set window width
        self.screen_height = 600  # Set window height
        self.bg_color = (230, 230, 230)  # Set background color

        # Spacecraft setup
        self.ship_limit = 3  # Set the maximum number of ships for players

        # Bullet setting
        self.bullet_width = 3  # The width of the bullet
        self.bullet_height = 15  # Bullet height
        self.bullet_color = (60, 60, 60)  # Bullet color
        self.bullets_allowed = 3  # Limit the number of bullets that do not disappear to 3

        # Alien settings
        self.fleet_drop_speed = 10  # The speed at which aliens move down

        self.speed_up = 1.1  # What kind of speed to accelerate the pace of the game

        self.score_scale = 1.5  # Speed up scores

        self.initialize_dynamic_speed()

    def initialize_dynamic_speed(self):
        """The amount of dynamic change as the game progresses"""
        self.ship_speed = 1.5  # Set the initial value of spacecraft speed
        self.bullet_speed = 3  # Bullet speed
        self.alien_speed = 0.5  # Aliens move at a speed of 0.5
        self.alien_point = 50  # Points per alien defeated

        # fleet_ When direction is 1, it means to move right, and when direction is - 1, it means to move left
        self.fleet_direction = 1

    def increase_speed(self):
        """Speed up"""
        self.ship_speed *= self.speed_up
        self.bullet_speed *= self.speed_up
        self.alien_speed *= self.speed_up
        self.alien_point = int(self.alien_point * self.score_scale)
        # print(self.alien_point)   # Print and display the score of the current alien