prices = [7, 1, 5, 3, 6, 4]
min_price = float('inf')  # Initialize min_price to a very large value
max_price=0
for price in prices:
    min_price=min(min_price,price)
    max_price=max(max_price,price-min_price)
print(max_price)


def maxProfit(prices):
    max_profit = 0  # Initialize max_profit to 0

    for price in prices:
        # Update min_price if the current price is smaller
        min_price = min(min_price, price)
        
        # Update max_profit if the current profit is larger
        max_profit = max(max_profit, price - min_price)

    return max_profit