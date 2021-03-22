class Settings():
    def __init__(self):
        # Init game settings
        # Screen params
        self.screen_width = 1400
        self.screen_height = 830
        self.bg_color = (80, 38, 56)

        # Bullet params
        self.bullet_speed_factor = 1
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5