import data_processing as data

file = open("./data/stock.csv")
records = file.readlines()

item_values = data.read_values(records)

file.close()

def show_cart_and_value(cart, values = item_values):
    for item, amount in cart.items():
        print("{}: {}".format(item.title(), amount))
    print("\nValue: {} zł".format(sum_items(cart, values)))

def show_stock(stock):
    items_available = 0
    for item, amount in stock.items():
        if amount:
            items_available += 1
            print("{}: {}".format(item.title(), amount))
    if not items_available:
        print("Empty stock ;___;")

def check_availability(item, stock):
    if item in stock:
        if stock[item] > 0:
            return 'Available'
        else:
            return 'No More'
    else:
        return 'Unavailable'

def add_to_cart(cart, item, quantity = 1):
    if item in cart:
        cart[item] += quantity
    else:
        cart[item] = quantity
    return cart

def remove_from_stock(item, stock, quantity = 1):
    stock[item] -= quantity
    return stock

def sum_items(cart, values = item_values):
    item_sum = 0
    for item, amount in cart.items():
        item_sum += amount * values[item]
    return item_sum
