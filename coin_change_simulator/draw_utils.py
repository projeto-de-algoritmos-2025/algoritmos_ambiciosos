# draw_utils.py

import pygame
from constants import *


def draw_text(screen, text, pos, color=BLACK, font_obj=None):
    if font_obj is None:
        font_obj = fonts["font"]
    text_surface = font_obj.render(text, True, color)
    screen.blit(text_surface, pos)


def draw_gradient_background(screen):
    for y in range(window_size[1]):
        color = (
            int(BG_COLOR[0] + (HIGHLIGHT[0] - BG_COLOR[0]) * y / window_size[1]),
            int(BG_COLOR[1] + (HIGHLIGHT[1] - BG_COLOR[1]) * y / window_size[1]),
            int(BG_COLOR[2] + (HIGHLIGHT[2] - BG_COLOR[2]) * y / window_size[1]),
        )
        pygame.draw.line(screen, color, (0, y), (window_size[0], y))


def draw_panel(screen):
    panel_rect = pygame.Rect(40, 20, 670, 1050)  # altura aumentada
    pygame.draw.rect(screen, (255, 255, 255, 230), panel_rect, border_radius=18)
    pygame.draw.rect(screen, BORDER_COLOR, panel_rect, 3, border_radius=18)


def draw_coin_icon(screen, x, y, color):
    pygame.draw.circle(screen, color, (x, y), 16)
    pygame.draw.circle(screen, (200, 200, 200), (x, y), 16, 2)


def draw_input_box(screen, box, active=False):
    pygame.draw.rect(screen, (245, 250, 255), box["rect"], border_radius=8)
    pygame.draw.rect(
        screen,
        HIGHLIGHT if active else BORDER_COLOR,
        box["rect"],
        3 if active else 2,
        border_radius=8,
    )
    draw_text(screen, box["text"], (box["rect"].x + 10, box["rect"].y + 7))
