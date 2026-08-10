import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT
from utils.constants import PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_SPEED

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.speed = PLAYER_SPEED
        self.lives = 3
        
        
        self.invulnerable = False
        self.invulnerable_timer = 0
        self.invulnerable_duration = 1500  

        
        self.draw_ship()

    def draw_ship(self):
        """Dibuja una nave espacial retro con alas y cabina."""
        self.image.fill((0, 0, 0, 0))  
        
        w, h = PLAYER_WIDTH, PLAYER_HEIGHT
        
        
        points_body = [(w // 2, 0), (0, h), (w, h)]
        pygame.draw.polygon(self.image, (0, 180, 255), points_body)
        
        
        pygame.draw.ellipse(self.image, (255, 255, 0), (w // 2 - 5, h // 3, 10, 15))
        
        
        pygame.draw.rect(self.image, (255, 50, 50), (2, h - 8, 8, 8))
        pygame.draw.rect(self.image, (255, 50, 50), (w - 10, h - 8, 8, 8))

    def update(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.rect.left > 0:
            self.rect.x -= self.speed
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.rect.right < SCREEN_WIDTH:
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
            return True  

        
        self.invulnerable = True
        self.invulnerable_timer = pygame.time.get_ticks()
        return False