import pygame as py
import os

# Constants size display
WIDTH, HEIGHT = 900, 500
VEL = 5
BULLET_VEL = 16
MAX_BULLET = 6
SHIP_WIDTH, SHIP_HEIGHT = 55, 40

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BORDER = py.Rect(WIDTH / 2 - 5, 0, 10, HEIGHT)

# Special Event
RED_HIT = py.USEREVENT + 1
YELLOW_HIT = py.USEREVENT + 2

# Load image and sound
YELLOW_SHIP = py.image.load(os.path.join('assets', 'spaceship_yellow.png'))
RED_SHIP = py.image.load(os.path.join('assets', 'spaceship_red.png'))
BACKGROUND = py.image.load(os.path.join('assets', 'background.png'))
BULLET = py.image.load(os.path.join('assets', 'spaceship_red.png'))
BACKSOUND = py.mixer.Sound(os.path.join('assets', 'sound.mp3'))
BULLET_SOUND = py.mixer.Sound(os.path.join('assets', 'bullet.mp3'))

# Transform image
YELLOW_SHIP = py.transform.rotate(py.transform.scale(YELLOW_SHIP, (SHIP_WIDTH, SHIP_HEIGHT)), 90)
RED_SHIP = py.transform.rotate(py.transform.scale(RED_SHIP, (SHIP_WIDTH, SHIP_HEIGHT)), -90)
BACKGROUND = py.transform.scale(BACKGROUND, (WIDTH, HEIGHT))
YELLOW_BULLET = py.transform.rotate(py.transform.scale(BULLET, (80, 80)), 0)
RED_BULLET = py.transform.rotate(py.transform.scale(BULLET, (80, 80)), -180)

# Font
HEAL_FONT = py.font.SysFont('comicsans', 35)
