prices = {
    'IBM': 50.5,
    'AAPL': 40.2,
    'GOOG': 99.9
}

max_value = max(zip(prices.values(), prices.keys()))
print(max_value)

min_value = min(zip(prices.values(), prices.keys()))
print(min_value)

print(zip(prices.values(), prices.keys()))
