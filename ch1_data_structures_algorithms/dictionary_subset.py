# use a dictionary comprehension!

stocks = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# get prices over 200
expensive = {key: value for key, value in stocks.items() if value > 200}
print(expensive)

# get only tech stocks
tech_companies = {'APPL', 'IBM', 'FB'}
tech = {key: value for key, value in stocks.items() if key in tech_companies}
print(tech)
