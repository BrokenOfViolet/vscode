import pygame


class Ship:
    def __init__(self, ai_game):
        """__init__函数初始化

        Args:
            ai_game : (->AlienInvasion的一个实例)
        """
        self.screen = ai_game.screen                   
        self.screen_rect = ai_game.screen.get_rect()
        
        self.settings = ai_game.settings
        
        self.image = pygame.image.load('/Users/mac/vscode/Python/Alien_Invasion/images/ship.bmp')
        self.rect = self.image.get_rect()
        
        self.rect.midbottom = self.screen_rect.midbottom   

        self.x = float(self.rect.x)
        
        self.moving_right = False
        self.moving_left = False
        
        self.shoot = False
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)
        
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.rect.x -= self.settings.ship_speed
            
    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)