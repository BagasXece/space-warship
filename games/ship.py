import pygame as py
from .constants import MAX_BULLET, VEL, BULLET_VEL, SHIP_WIDTH, SHIP_HEIGHT, BULLET_SOUND, BORDER, WIDTH, HEIGHT

py.init()
py.mixer.init()

class Ship:
    def __init__(self, x, y, image, is_yellow=True):
        self.rect = py.Rect(x, y, SHIP_WIDTH - 15, SHIP_HEIGHT + 15)
        self.image = image
        self.is_yellow = is_yellow
        self.health = 10
        self.bullets = []

    def draw(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def move(self, keys_pressed):
        if self.is_yellow:
            if keys_pressed[py.K_a] and self.rect.x - VEL > 0:
                self.rect.x -= VEL
            if keys_pressed[py.K_d] and self.rect.x + VEL + self.rect.width < BORDER.x:
                self.rect.x += VEL
            if keys_pressed[py.K_w] and self.rect.y - VEL > 0:
                self.rect.y -= VEL
            if keys_pressed[py.K_s] and self.rect.y + VEL + self.rect.height < HEIGHT:
                self.rect.y += VEL
        else:
            if keys_pressed[py.K_LEFT] and self.rect.x - VEL > BORDER.x + 10:
                self.rect.x -= VEL
            if keys_pressed[py.K_RIGHT] and self.rect.x + VEL + self.rect.width < WIDTH:
                self.rect.x += VEL
            if keys_pressed[py.K_UP] and self.rect.y - VEL > 0:
                self.rect.y -= VEL
            if keys_pressed[py.K_DOWN] and self.rect.y + VEL + self.rect.height < HEIGHT:
                self.rect.y += VEL

    def shoot(self, bullet_image, direction):
        if len(self.bullets) < MAX_BULLET:
            if self.is_yellow:
                bullet = py.Rect(self.rect.x + self.rect.width - 15, self.rect.y - 13 + self.rect.height - 16, 10, 5)
            else:
                bullet = py.Rect(self.rect.x + self.rect.width - 65, self.rect.y - 10 + self.rect.height - 16, 10, 5)
            self.bullets.append(bullet)
            BULLET_SOUND.play()

    def handle_bullets(self, enemy, event_hit):
        for bullet in self.bullets[:]:
            bullet.x += BULLET_VEL if self.is_yellow else -BULLET_VEL
            if enemy.rect.colliderect(bullet):
                py.event.post(py.event.Event(event_hit))
                self.bullets.remove(bullet)
            elif bullet.x > WIDTH or bullet.x < 0:
                self.bullets.remove(bullet)
        if py.event.get(py.USEREVENT):  # Check if the timer has expired
            self.bullets = []