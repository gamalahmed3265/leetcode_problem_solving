prices = [7, 1, 5, 3, 6, 4]
min_price = float('inf')  # Initialize min_price to a very large value
max_price=0
for price in prices:
    min_price=min(min_price,price)
    max_price=max(max_price,price-min_price)
print(max_price)

