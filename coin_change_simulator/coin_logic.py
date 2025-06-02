# coin_logic.py

from constants import all_values, all_labels

def greedy_change(value, stock):
    result = []
    for i, unit in enumerate(all_values):
        count = 0
        while unit <= value and stock[i] > 0:
            value -= unit
            stock[i] -= 1
            count += 1
        if count > 0:
            result.append((all_labels[i], count))
    return result if value == 0 else None
