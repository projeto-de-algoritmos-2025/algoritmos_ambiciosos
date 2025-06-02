# coin_logic.py

coins = [100, 50, 25, 10, 5, 1]
coin_labels = ["R$1,00", "R$0,50", "R$0,25", "R$0,10", "R$0,05", "R$0,01"]

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
    return result if value == 0 else None
