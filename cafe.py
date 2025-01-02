"""Task 2: Imagine you are running a café. Create a new Python file in your fold
called cafe.py.
● Create a list called menu, which should contain at least four items sold in
the café.
● Next, create a dictionary called stock, which should contain the stock
value for each item on your menu.
● Create another dictionary called price, which should contain the prices for
each item on your menu.
● Next, calculate the worth of the total_stock in the café. You will need to
remember to loop through the appropriate dictionaries and lists to do
this.
Tip: When you loop through the menu list, the “items” can be set as keys
to access the corresponding “stock” and “price” values. Each item_value is
calculated by multiplying the stock value by the price value. For example:
item_value = (stock[item] * price[item])
● Finally, print out the result of your calculation"""


# solution

# list of menu that contains items sold in a café
menu = ["salad", "bagel", "croissant", "coffee"]

# dictionary stock, which  contain the stock value for each item on the list of menu.
stock = {"salad": 10, "bagel": 6, "croissant": 8, "coffee": 20}

# price of each item in menu in pounds
price = {"salad": 12, "bagel": 4, "croissant": 50, "coffeee": 200}

# calculate the worth of all the total stock in the cafe
total_stock = 0 # initializes to zero

# loop through both dictionaries 
for (item, stock_value), (item, price) in zip(stock.items(), price.items()):
    item_value = stock_value * price # calculate the total worth of each item
    total_stock = total_stock + item_value # increase the total stock by the total value of each item

print(f"The worth of all items in the cafe is: £{total_stock}")
