import pygame
from config import screen_width, screen_height
from utils.constants import player_width, player_height, player_speed


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((player_width, player_height), pygame.srcalpha)
        self.image.fill((0, 0, 0, 0))
        pygame.draw.rect(self.image, (255, 255, 0), (1, 1, player_width - 2, player_height - 2))
        
        self.rect = self.image.get_rect()
        self.rect.centerx = screen_width // 2
        self.rect.bottom = screen_height - 10
        self.speed = player_speed
        self.lives = 3
        
        self.invulnerable = False
        self.invulnerable_timer = 0
        self.invulnerable_duration = 1500
        
        self.draw_ship()
        
    def draw_ship(self):
        """DIBUJA NAVE ESPACIAL DISEÑO"""
        self.image.fill((0, 0, 0, 0))
        w, h = player_width, player_height
        
        points_body = [(w // 2, 0), (0, h), (w, h)]
        pygame.draw.polygon(self.image, (0, 180, 255), points_body)
        
        pygame.draw.ellipse(self.image, (255, 255, 0), (w // 2 - 5, h // 3, 10, 15))
        pygame.draw.rect(self.image, (255, 50, 50), (2, h - 8, 8, 8))
        pygame.draw.rect(self.image, (255, 50, 50), (w - 10, h - 8, 8, 8))
        
    def update(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.rect.left > 0:
            self.rect.x -= self.speed
            
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.rect.right < screen_width:
            self.rect.x += self.speed
            
        if self.invulnerable:
            now = pygame.time.get_ticks()
            if now - self.invulnerable_timer > self.invulnerable_duration:
                self.invulnerable = False
                self.draw_ship()
                
            else:
                if (now // 100) % 2 == 0:
                    self.image.fill((0, 0, 0, 0))
                else:
                    self.draw_ship()
                    
    def shoot(self):
        pass
    
    def take_damage(self):
        if self.invulnerable:
            return False
        
        self.lives -= 1
        if self.lives <= 0:
            return True   ##GAME OVER
        self.invulnerable = True
        self.invulnerable_timer = pygame.time.get_ticks()
        return False
            
          