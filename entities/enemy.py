import pygame
import random
from config import SCREEN_WIDTH, SCREEN_HEIGHT
from utils.constants import ENEMY_WIDTH, ENEMY_HEIGHT, ENEMY_SPEED

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        
        self.image = pygame.Surface((ENEMY_WIDTH + 6, ENEMY_HEIGHT + 6), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = ENEMY_SPEED
        self.direction = random.choice([-1, 1])  
        
        
        self.target_y = random.randint(100, 240)

    def update(self):
        
        if self.rect.y < self.target_y:
            self.rect.y += 2
        else:
            
            self.rect.x += self.speed * self.direction
            
            
            if self.rect.left <= 15 or self.rect.right >= SCREEN_WIDTH - 15:
                self.direction *= -1
                
                self.rect.y += random.choice([-8, 8])
                self.rect.y = max(80, min(self.rect.y, 280))

    def draw_alien(self):
        pass


class EnemyTypeA(Enemy):
    """Enemigo 1: Tipo Abejita Roja"""
    def __init__(self, x, y):
        super().__init__(x, y)
        self.draw_alien()

    def draw_alien(self):
        self.image.fill((0, 0, 0, 0))
        w, h = self.rect.width, self.rect.height
        
        pygame.draw.ellipse(self.image, (230, 50, 50), (4, 4, w - 8, h - 8))
        
        pygame.draw.circle(self.image, (255, 230, 0), (w // 3, h // 3 + 2), 4)
        pygame.draw.circle(self.image, (255, 230, 0), (2 * w // 3, h // 3 + 2), 4)
        pygame.draw.circle(self.image, (0, 0, 0), (w // 3, h // 3 + 2), 2)
        pygame.draw.circle(self.image, (0, 0, 0), (2 * w // 3, h // 3 + 2), 2)


class EnemyTypeB(Enemy):
    """Enemigo 2: Tipo Platillo Verde"""
    def __init__(self, x, y):
        super().__init__(x, y)
        self.speed = ENEMY_SPEED * 1.2  
        self.draw_alien()

    def draw_alien(self):
        self.image.fill((0, 0, 0, 0))
        w, h = self.rect.width, self.rect.height
        
        pygame.draw.ellipse(self.image, (50, 230, 100), (2, h // 3, w - 4, h // 2))
        
        pygame.draw.circle(self.image, (0, 150, 255), (w // 2, h // 3), 6)


class EnemyTypeC(Enemy):
    """Enemigo 3: Tipo Tanque Morado"""
    def __init__(self, x, y):
        super().__init__(x, y)
        self.speed = ENEMY_SPEED * 0.7  
        self.draw_alien()

    def draw_alien(self):
        self.image.fill((0, 0, 0, 0))
        w, h = self.rect.width, self.rect.height
        
        pygame.draw.rect(self.image, (180, 50, 220), (4, 4, w - 8, h - 8), border_radius=4)
        
        pygame.draw.line(self.image, (255, 255, 255), (6, 10), (w - 6, 10), 3)
        