import pygame as simulador_trocador
import sys

simulador_trocador.init()
font = simulador_trocador.font.SysFont(None, 24)

# Moedas disponíveis no Brasil
coins = [100, 50, 25, 10, 5, 1]
coin_labels = ["R$1,00", "R$0,50", "R$0,25", "R$0,10", "R$0,05", "R$0,01"]
coin_stock = [10, 10, 10, 10, 10, 10]  # Quantidade inicial de cada moeda

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (180, 180, 180)
GREEN = (0, 200, 0)
RED = (200, 0, 0)

# Janela
WIDTH, HEIGHT = 700, 500
screen = simulador_trocador.display.set_mode((WIDTH, HEIGHT))
simulador_trocador.display.set_caption("Simulador de Troco - Algoritmo Guloso")

# Inputs
input_boxes = {
    "Valor da Compra": {"rect": simulador_trocador.Rect(50, 40, 200, 32), "text": ""},
    "Valor Recebido": {"rect": simulador_trocador.Rect(300, 40, 200, 32), "text": ""},
}

active_box = None

# Inputs para estoque de moedas
stock_boxes = []
for i, label in enumerate(coin_labels):
    stock_boxes.append({
        "rect": simulador_trocador.Rect(250, 130 + i * 30, 60, 28),
        "text": str(coin_stock[i]),
        "index": i
    })

active_stock_box = None

def draw_text(text, pos, color=BLACK):
    screen.blit(font.render(text, True, color), pos)

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
        return None  # Não foi possível fazer o troco
    return result

def main():
    global active_box, active_stock_box, coin_stock
    clock = simulador_trocador.time.Clock()
    message = ""
    result = []

    while True:
        screen.fill(WHITE)

        # Eventos
        for event in simulador_trocador.event.get():
            if event.type == simulador_trocador.QUIT:
                simulador_trocador.quit()
                sys.exit()

            elif event.type == simulador_trocador.MOUSEBUTTONDOWN:
                active_box = None
                active_stock_box = None
                for label, box in input_boxes.items():
                    if box["rect"].collidepoint(event.pos):
                        active_box = label
                for box in stock_boxes:
                    if box["rect"].collidepoint(event.pos):
                        active_stock_box = box

                # Botão de calcular troco
                if 520 <= event.pos[0] <= 650 and 40 <= event.pos[1] <= 72:
                    try:
                        # Atualiza o estoque de moedas com o que está digitado nas caixas
                        for i, box in enumerate(stock_boxes):
                            coin_stock[i] = int(box["text"])

                        valor_compra = float(input_boxes["Valor da Compra"]["text"].replace(",", "."))
                        valor_recebido = float(input_boxes["Valor Recebido"]["text"].replace(",", "."))
                        troco = int(round((valor_recebido - valor_compra) * 100))
                        if troco < 0:
                            message = "Valor recebido é menor que a compra!"
                            result = []
                        else:
                            new_stock = coin_stock[:]
                            res = greedy_change(troco, new_stock)
                            if res:
                                # Atualiza o estoque real após dar o troco
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

            elif event.type == simulador_trocador.KEYDOWN:
                if active_box:
                    if event.key == simulador_trocador.K_BACKSPACE:
                        input_boxes[active_box]["text"] = input_boxes[active_box]["text"][:-1]
                    else:
                        input_boxes[active_box]["text"] += event.unicode
                elif active_stock_box:
                    if event.key == simulador_trocador.K_BACKSPACE:
                        active_stock_box["text"] = active_stock_box["text"][:-1]
                    elif event.unicode.isdigit():
                        active_stock_box["text"] += event.unicode

        # Desenha campos de texto
        for i, (label, box) in enumerate(input_boxes.items()):
            simulador_trocador.draw.rect(screen, GRAY if active_box == label else BLACK, box["rect"], 2)
            draw_text(label, (box["rect"].x, box["rect"].y - 20))
            draw_text(box["text"], (box["rect"].x + 5, box["rect"].y + 5))

        # Botão de calcular
        simulador_trocador.draw.rect(screen, GREEN, (520, 40, 130, 32))
        draw_text("Calcular Troco", (530, 48), WHITE)

        # Estoque de moedas
        draw_text("Estoque de Moedas:", (50, 100))
        for i, label in enumerate(coin_labels):
            draw_text(f"{label}:", (50, 130 + i * 30))
            simulador_trocador.draw.rect(
                screen,
                GRAY if active_stock_box == stock_boxes[i] else BLACK,
                stock_boxes[i]["rect"], 2
            )
            draw_text(stock_boxes[i]["text"], (stock_boxes[i]["rect"].x + 5, stock_boxes[i]["rect"].y + 5))

        # Resultado
        draw_text(message, (50, 320), RED if "Erro" in message or "não" in message.lower() else BLACK)
        for i, (coin, count) in enumerate(result):
            draw_text(f"{count} x {coin}", (50, 350 + i * 25))

        simulador_trocador.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()