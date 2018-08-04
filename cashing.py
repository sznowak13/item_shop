def show_cart_and_value(cart, values):
    for item, amount in cart.items():
        print("{}: {}".format(item, amount))
    print("\nValue: {} zł".format(sum_items(cart, values)))

def show_stock(stock):
    items_available = 0
    for item, amount in stock.items():
        if amount:
            items_available += 1
            print("{}: {}".format(item, amount))
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

def sum_items(cart, stock):
    item_sum = 0
    for item, amount in cart.items():
        item_sum += amount * stock[item]
    return item_sum
