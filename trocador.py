import pygame
import pygame_gui
import sys

pygame.init()
window_size = (750, 550)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Simulador de Troco - Algoritmo Guloso")
manager = pygame_gui.UIManager(window_size)

font = pygame.font.SysFont("arial", 24)
large_font = pygame.font.SysFont("arial", 28, bold=True)

# Moedas disponíveis no Brasil
coins = [100, 50, 25, 10, 5, 1]
coin_labels = ["R$1,00", "R$0,50", "R$0,25", "R$0,10", "R$0,05", "R$0,01"]
coin_stock = [10, 10, 10, 10, 10, 10]

# Cores
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

# Inputs usando pygame_gui
input_box_compra = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect((60, 40), (200, 36)), manager=manager
)
input_box_compra.set_text('')

input_box_recebido = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect((300, 40), (200, 36)), manager=manager
)
input_box_recebido.set_text('')

button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((540, 40), (160, 36)),
    text='Calcular Troco',
    manager=manager
)

# Estoque
stock_boxes = []
for i, label in enumerate(coin_labels):
    stock_boxes.append({
        "rect": pygame.Rect(280, 130 + i * 35, 60, 30),
        "text": str(coin_stock[i]),
        "index": i
    })
active_stock_box = None

def draw_text(text, pos, color=BLACK, font_obj=font):
    text_surface = font_obj.render(text, True, color)
    screen.blit(text_surface, pos)

def greedy_change(value, stock):
    result = []
    for i, coin in enumerate(coins):
        count = 0
        while coin <= value and stock[i] > 0:
            value -= coin
            stock[i] -= 1
            count += 1
        if count > 0:
            result.append((coin_labels[i], count))
    if value > 0:
        return None
    return result

def draw_input_box(box, active=False):
    pygame.draw.rect(screen, BOX_COLOR, box["rect"])
    pygame.draw.rect(screen, HIGHLIGHT if active else BORDER_COLOR, box["rect"], 2)
    draw_text(box["text"], (box["rect"].x + 6, box["rect"].y + 6))

def main():
    global active_stock_box, coin_stock
    clock = pygame.time.Clock()
    message = ""
    result = []

    running = True
    while running:
        time_delta = clock.tick(30) / 1000.0
        screen.fill(BG_COLOR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            manager.process_events(event)

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED and event.ui_element == button:
                    try:
                        for i, box in enumerate(stock_boxes):
                            coin_stock[i] = int(box["text"])

                        valor_compra = float(input_box_compra.get_text().replace(",", "."))
                        valor_recebido = float(input_box_recebido.get_text().replace(",", "."))
                        troco = int(round((valor_recebido - valor_compra) * 100))
                        if troco < 0:
                            message = "Valor recebido é menor que a compra!"
                            result = []
                        else:
                            new_stock = coin_stock[:]
                            res = greedy_change(troco, new_stock)
                            if res:
                                coin_stock[:] = new_stock
                                for i, box in enumerate(stock_boxes):
                                    box["text"] = str(coin_stock[i])
                                message = f"Troco: R${troco / 100:.2f}"
                                result = res
                            else:
                                message = "Não é possível dar o troco com as moedas disponíveis."
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

        # Labels dos campos de entrada
        draw_text("Valor da Compra:", (60, 15), font_obj=font)
        draw_text("Valor Recebido:", (300, 15), font_obj=font)

        # Estoque de moedas
        draw_text("Estoque de Moedas:", (40, 100), font_obj=large_font)
        for i, label in enumerate(coin_labels):
            draw_text(f"{label}:", (40, 130 + i * 35))
            draw_input_box(stock_boxes[i], active_stock_box == stock_boxes[i])

        # Resultado
        draw_text(message, (40, 390), RED if "Erro" in message or "não" in message.lower() else BLACK, font_obj=large_font)
        for i, (coin, count) in enumerate(result):
            draw_text(f"{count} x {coin}", (40, 420 + i * 25))

        manager.draw_ui(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()