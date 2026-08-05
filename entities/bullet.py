import pygame
from config import screen_width, screen_height
from utils.constants import bullet_width, bullet_height, bullet_speed

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, speed_x=0):
        super().__init__()
        self.image = pygame.Surface((bullet_width, bullet_height), pygame.srcalpha)
        
        self.image.fill((255, 255, 0))
        pygame.draw.rect(self.image, (0, 255, 230), (1, 1, bullet_width -2, bullet_height - 2) )
        
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speed_y = bullet_speed * direction
        self.speed_x = speed_x
        
    def update(self):
        self.rect.y -= self.speed_y
        self.rect.x += self.speed_x
        
        if (self.rect.bottom < 0 or self.rect.top > screen_height or self.rect.right < 0 or self.rect.left > screen_width):
            self.kill()
            
        