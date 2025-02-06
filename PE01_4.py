price = 99.99
discountPercent = 25
markdown = discountPercent / 100 * price
price -= markdown
print(f"The discounted price is: {round(price, 2)}")