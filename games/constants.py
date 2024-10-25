import pygame as py
import os

py.init()
py.mixer.init()

# Konstanta
WIDTH, HEIGHT = 900, 500
VEL = 5
BULLET_VEL = 16
MAX_BULLET = 6
SHIP_WIDTH, SHIP_HEIGHT = 55, 40

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BORDER = py.Rect(WIDTH / 2 - 5, 0, 10, HEIGHT)

# Event khusus untuk penembakan
RED_HIT = py.USEREVENT + 1
YELLOW_HIT = py.USEREVENT + 2

# Load gambar dan suara
YELLOW_SHIP_IMAGE = py.image.load(os.path.join('assets', 'spaceship_yellow.png'))
RED_SHIP_IMAGE = py.image.load(os.path.join('assets', 'spaceship_red.png'))
SPACE = py.image.load(os.path.join('assets', 'background.png'))
BULLET_IMAGE = py.image.load(os.path.join('assets', 'peluru.png'))
SOUND = py.mixer.Sound(os.path.join('assets', 'sound.mp3'))
BULLET_SOUND = py.mixer.Sound(os.path.join('assets', 'bullet.mp3'))

# Transformasi gambar (resize dan rotasi)
ROTATE_SHIP_YELLOW = py.transform.rotate(py.transform.scale(YELLOW_SHIP_IMAGE, (SHIP_WIDTH, SHIP_HEIGHT)), 90)
ROTATE_SHIP_RED = py.transform.rotate(py.transform.scale(RED_SHIP_IMAGE, (SHIP_WIDTH, SHIP_HEIGHT)), -90)
SCALE_SPACE = py.transform.scale(SPACE, (WIDTH, HEIGHT))
YELLOW_BULLET = py.transform.rotate(py.transform.scale(BULLET_IMAGE, (80, 80)), 0)
RED_BULLET = py.transform.rotate(py.transform.scale(BULLET_IMAGE, (80, 80)), -180)

# Font untuk teks
HEAL_FONT = py.font.SysFont('comicsans', 35)
WINNER_FONT = py.font.SysFont('comicsans', 35)
MENU_FONT = py.font.SysFont('comicsans', 50)