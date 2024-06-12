""" Task 7: Handling dictionaries.
- Imagine you are running a café.
- Create dictionaries to handle data regarding stock and prices.
- Calculate the total stock worth in your café by
looping through the dictionaries.
- A tip to achieve this is to set "items" as keys to access
the corresponding "stock" and "price" values.

"""
# list of products on my menu
menu = ["cheesecake", "cookie", "brownie", "croissant"]
# number of items in stock for each product
stock_values_list = [20, 35, 25, 22]
# price of each product on my menu
price_values_list = [5.50, 2.50, 4.50, 3]


stock_value_pairs = zip(menu, stock_values_list)
# created a dictionary with products and items in stock
stock = dict(stock_value_pairs)

price_value_pairs = zip(menu, price_values_list)
# created a dictionary with products and their correponding prices
price = dict(price_value_pairs)


total_stock = 0
# for loop to go through each product on the menu and
# multiply the number of items in stock by their price
for key in stock:
    # += to add each multiplication result to the previous one to get the total
    total_stock += stock[key] * price[key]


print(f"The total value of my cafe stock is: £{total_stock}")
# Output: The total value of my cafe stock is: £376.0
