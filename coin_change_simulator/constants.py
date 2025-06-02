# constants.py

import pygame

pygame.init()

coins = [100, 50, 25, 10, 5, 1]
coin_labels = ["R$1,00", "R$0,50", "R$0,25", "R$0,10", "R$0,05", "R$0,01"]
initial_coin_stock = [10] * 6

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (220, 220, 220)
DARK_GRAY = (160, 160, 160)
GREEN = (34, 177, 76)
RED = (200, 0, 0)
BG_COLOR = (245, 245, 250)
HIGHLIGHT = (100, 149, 237)
BOX_COLOR = (255, 255, 255)
BORDER_COLOR = (150, 150, 150)

window_size = (750, 550)

fonts = {
    "font": pygame.font.SysFont("arial", 24),
    "large": pygame.font.SysFont("arial", 28, bold=True),
    "small": pygame.font.SysFont("arial", 20),
}

coin_colors = [
    (255, 215, 0),
    (192, 192, 192),
    (205, 127, 50),
    (135, 206, 250),
    (255, 182, 193),
    (211, 211, 211)
]
