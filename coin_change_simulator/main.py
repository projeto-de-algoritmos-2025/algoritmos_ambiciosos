# main.py

import pygame
import pygame_gui
import sys
from constants import all_labels, all_colors, initial_stock, window_size, fonts
from coin_logic import greedy_change
from draw_utils import *

pygame.init()
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Simulador de Troco - Algoritmo Guloso")
manager = pygame_gui.UIManager(window_size)
window_size = (750, 800)
input_box_compra = pygame_gui.elements.UITextEntryLine(
    pygame.Rect((120, 50), (200, 36)), manager=manager
)
input_box_recebido = pygame_gui.elements.UITextEntryLine(
    pygame.Rect((430, 50), (200, 36)), manager=manager
)
button = pygame_gui.elements.UIButton(
    pygame.Rect((500, 120), (200, 36)), "Calcular Troco", manager
)
stock_boxes = [
    {
        "rect": pygame.Rect(320, 170 + i * 45, 60, 36),
        "text": str(initial_stock[i]),
        "index": i,
    }
    for i in range(len(initial_stock))
]
coin_stock = initial_stock[:]
active_stock_box = None


def main():
    global active_stock_box, coin_stock
    clock = pygame.time.Clock()
    message = ""
    result = []

    running = True
    while running:
        time_delta = clock.tick(30) / 1000.0
        draw_gradient_background(screen)
        draw_panel(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            manager.process_events(event)

            if event.type == pygame.USEREVENT:
                if (
                    event.user_type == pygame_gui.UI_BUTTON_PRESSED
                    and event.ui_element == button
                ):
                    try:
                        for i, box in enumerate(stock_boxes):
                            coin_stock[i] = int(box["text"])
                        compra = float(input_box_compra.get_text().replace(",", "."))
                        recebido = float(
                            input_box_recebido.get_text().replace(",", ".")
                        )
                        troco = int(round((recebido - compra) * 100))
                        if troco < 0:
                            message = "Valor recebido é menor!"
                            result = []
                        else:
                            temp_stock = coin_stock[:]
                            res = greedy_change(troco, temp_stock)
                            if res:
                                coin_stock[:] = temp_stock
                                for i, box in enumerate(stock_boxes):
                                    box["text"] = str(coin_stock[i])
                                message = f"Troco: R${troco / 100:.2f}"
                                result = res
                            else:
                                message = "Erro: Saldo insuficiente em caixa."
                                result = []
                    except ValueError:
                        message = "Erro nos valores inseridos."
                        result = []

            if event.type == pygame.MOUSEBUTTONDOWN:
                active_stock_box = None
                for box in stock_boxes:
                    if box["rect"].collidepoint(event.pos):
                        active_stock_box = box

            if event.type == pygame.KEYDOWN and active_stock_box:
                if event.key == pygame.K_BACKSPACE:
                    active_stock_box["text"] = active_stock_box["text"][:-1]
                elif event.unicode.isdigit():
                    active_stock_box["text"] += event.unicode

        manager.update(time_delta)

        draw_text(screen, "Valor da Compra:", (120, 25), font_obj=fonts["font"])
        draw_text(screen, "Valor Recebido:", (430, 25), font_obj=fonts["font"])
        draw_text(
            screen, "Estoque de Cédulas e Moedas:", (80, 120), font_obj=fonts["large"]
        )

        for i, label in enumerate(all_labels):
            y = 180 + i * 45
            draw_coin_icon(screen, 100, y + 18, all_colors[i])
            draw_text(screen, f"{label}:", (130, y + 7), font_obj=fonts["font"])
            draw_input_box(screen, stock_boxes[i], active_stock_box == stock_boxes[i])

        resultado_x, resultado_y = 430, 160
        is_erro = any(p in message.lower() for p in ["erro", "não", "menor"])
        draw_text(
            screen,
            message,
            (resultado_x, resultado_y),
            RED if is_erro else GREEN,
            font_obj=fonts["small"] if is_erro else fonts["large"],
        )

        if result:
            for i, (coin, count) in enumerate(result):
                draw_text(
                    screen,
                    f"{count} x {coin}",
                    (resultado_x, resultado_y + 40 + i * 30),
                    font_obj=fonts["font"],
                )

        manager.draw_ui(screen)
        pygame.display.flip()

window_size = (750, 800)
if __name__ == "__main__":
    main()
