# constants.py

import pygame

pygame.init()

bills = [20000, 10000, 5000, 2000, 1000, 500, 200]
bill_labels = ["R$200,00", "R$100,00", "R$50,00", "R$20,00", "R$10,00", "R$5,00", "R$2,00"]
bill_colors = [
    (0, 128, 128),
    (0, 100, 0),
    (139, 69, 19),
    (255, 140, 0),
    (0, 0, 205),
    (255, 0, 0),
    (128, 0, 128)
]

coins = [100, 50, 25, 10, 5, 1]
coin_labels = ["R$1,00", "R$0,50", "R$0,25", "R$0,10", "R$0,05", "R$0,01"]
coin_colors = [
    (255, 215, 0),
    (192, 192, 192),
    (205, 127, 50),
    (135, 206, 250),
    (255, 182, 193),
    (211, 211, 211)
]

all_values = bills + coins
all_labels = bill_labels + coin_labels
all_colors = bill_colors + coin_colors
initial_bill_stock = [10] * len(bills)
initial_coin_stock = [10] * len(coins)
initial_stock = initial_bill_stock + initial_coin_stock

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
