import pygame
import random
from config import screen_width, screen_height
from utils.constants import enemy_width, enemy_height, enemy_speed

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        
        self.image = pygame.Surface((enemy_width +6, enemy_height +6), pygame.srcalpha)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = enemy_speed
        self.direction = random.choice([-1, 1])
        
        self.target_y = random.randint(100, 240)
        
    def update(self):
        if self.rect.y < self.target_y:
            self.retc.y += 2
        else:
            self.rect.x += self.speed * self.direction
            
            if self.rect.left <= 15 or self.rect.right >= screen_width - 15:
                self.direction *= -1
                
                self.rect.y += random.choince([-8, 8,])
                self.rect.y = max(80, min(self.rect.y, 280))
                
    def draw_alien(self):
        pass
    
    class AlienTypeA(Enemy):
        """ENEMY 1: ABEJA ROJA"""
        def __init__(self,x ,y):
            super().__init__(x, y)
            self.draw_alien()
        
        def draw_alien(self):
            self.image.fill((0, 0, 0, 0))
            w, h = self.rect.width, self.rect.height
            
            pygame.draw.ellipse(self.image, (230, 50, 50), (4, 4, w-8, h-8))
            pygame.draw.circle(self.image, (255, 230, 0), (w // 3, h//3 +2), 4)
            pygame.draw.circle(self.image, (255, 230, 0), (2 * w //3, h//3 + 2), 4)
            pygame.draw.circle(self.image, (0, 0, 0), (w // 3, h//3 +2), 2)
            pygame.draw.circle(self.image, (0, 0, 0), (2 * w //3, h//3 + 2), 2)
            
    class AlienTypeB(Enemy):
        """ENEMY 2: PLATILLO VERDE"""
        def __init__(self, x, y):
            super().__init__(x, y)
            self.speed = enemy_speed * 1.2
            self.draw_alien()
            
        def draw_alien(self):
            self.image,fill((0, 0, 0, 0))
            w, h = self.rect.width, self.rect.height
            
            pygame.draw.ellipse(self.image, (50, 230, 100), (2, h // 3, w - 4, h // 2))
            pygame.draw.circle(self.image, (0, 150, 255), (w // 2, h // 3), 6)
            
    class AlienTypeC(Enemy):
        """ENEMY 3: TANQUE MORADO"""
        def __init__(self, x, y):
            super().__init__(x, y)
            self.speed = enemy_speed * 0.7
            self.draw_alien()
            
        def draw_alien(self):
            self.image.fill((0, 0, 0, 0))
            w, h = self.rect.width, self.rect.height
            
            pygame.draw.rect(self.image, (180, 50, 220), (4, 4, w - 8, h - 8)), border_radius=4)
            pygame.draw.line(self.image, (255, 255, 255), (6, 10), (w - 6, 10), 3)
            
            