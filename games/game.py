import pygame as py
from pygame.locals import QUIT
import sys
from .constants import *
from .ship import Ship

py.init()
py.mixer.init()
class Game:
    def __init__(self):
        self.yellow_ship = Ship(100, 300, ROTATE_SHIP_YELLOW)
        self.red_ship = Ship(700, 300, ROTATE_SHIP_RED, is_yellow=False)
        self.display = py.display.set_mode((WIDTH, HEIGHT))
        py.display.set_caption("Bagas Sukmanyo")
        self.clock = py.time.Clock()
        self.run_game = True

    def draw_window(self):
        self.display.blit(SCALE_SPACE, (0, 0))
        py.draw.rect(self.display, WHITE, BORDER)

        self.yellow_ship.draw(self.display)
        self.red_ship.draw(self.display)

        for bullet in self.yellow_ship.bullets:
            self.display.blit(YELLOW_BULLET, (bullet.x - 37, bullet.y - 40))
        for bullet in self.red_ship.bullets:
            self.display.blit(RED_BULLET, (bullet.x - 22, bullet.y - 40))

        red_health_text = HEAL_FONT.render(f"Health: {max(self.red_ship.health, 0)}", 1, WHITE)
        yellow_health_text = HEAL_FONT.render(f"Health: {max(self.yellow_ship.health, 0)}", 1, WHITE)
        self.display.blit(red_health_text, (WIDTH - red_health_text.get_width() - 70, 17))
        self.display.blit(yellow_health_text, (WIDTH - yellow_health_text.get_width() - 670, 17))

        py.display.update()

    def splash_game(self):
        self.display.fill(BLACK)
        menu_text = MENU_FONT.render("Click \"R\" for Restart or \"Q\" for Quit", True, WHITE)
        self.display.blit(menu_text, (WIDTH / 2 - menu_text.get_width() / 2, HEIGHT / 2 - menu_text.get_height() / 2))
        py.display.update()

        wait = True
        while wait:
            for event in py.event.get():
                if event.type == QUIT:
                    py.quit()
                    sys.exit()
                if event.type == py.KEYDOWN:
                    if event.key == py.K_r:
                        wait = False
                    if event.key == py.K_q:
                        py.quit()
                        sys.exit()

    def draw_winner(self, text):
        draw_text = WINNER_FONT.render(text, 1, WHITE)
        self.display.blit(draw_text, (WIDTH / 2 - draw_text.get_width() / 2, HEIGHT / 2 - draw_text.get_height() / 2))
        py.display.update()
        py.time.delay(3000)

    def reset_game(self):
        self.yellow_ship.bullets.clear()
        self.red_ship.bullets.clear()
        self.yellow_ship.health = 10
        self.red_ship.health = 10

    def main_game(self):
        self.reset_game()

        while self.run_game:
            self.clock.tick(60)
            keys_pressed = py.key.get_pressed()

            for event in py.event.get():
                if event.type == QUIT:
                    py.quit()
                    sys.exit()
                if event.type == py.KEYDOWN:
                    if event.key == py.K_LCTRL:
                        self.yellow_ship.shoot(YELLOW_BULLET, 1)
                    elif event.key == py.K_RCTRL:
                        self.red_ship.shoot(RED_BULLET, -1)
                if event.type == RED_HIT:
                    self.red_ship.health -= 1
                if event.type == YELLOW_HIT:
                    self.yellow_ship.health -= 1

            self.yellow_ship.move(keys_pressed)
            self.red_ship.move(keys_pressed)

            self.yellow_ship.handle_bullets(self.red_ship, RED_HIT)
            self.red_ship.handle_bullets(self.yellow_ship, YELLOW_HIT)

            # Cek kondisi kesehatan pemain
            if self.red_ship.health <= 0 or self.yellow_ship.health <= 0:
                winner_text = "Yellow Menang!" if self.red_ship.health <= 0 else "Red Menang!"
                SOUND.play()
                self.draw_winner(winner_text)
                self.splash_game()
                self.main_game()

            self.draw_window()