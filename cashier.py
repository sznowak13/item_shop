item_values = {
    'Food': 5,
    'Drink': 2,
    'Fags': 10
}
current_stock = {
    'Food': 3,
    'Drink': 10,
    'Fags':1
}

def show_cart_and_value(cart, values=item_values):
    for item, amount in cart.items():
        print("{}: {}".format(item, amount))
    print("\nValue: {} zł".format(sum_items(cart, values)))

def show_stock(stock):
    for item, amount in stock.items():
        print("{}: {}".format(item, amount))

def check_availability(item, stock):
    if item in stock:
        if stock[item] > 0:
            return 'Available'
        else:
            return 'No More'
    else:
        return 'Unavailable'

def add_to_cart(cart, item):
    if item in cart:
        cart[item] += 1
    else:
        cart[item] = 1
    return cart

def remove_from_stock(item, stock):
    stock[item] -= 1
    return stock

def sum_items(cart, stock):
    item_sum = 0
    for item, amount in cart.items():
        item_sum += amount * stock[item]
    return item_sum

choosing = True
customer_cart = {}

while choosing:
    print("Enter an item to add to your cart. To see your cart type 'show cart', to see the stock type 'show stock', to exit type 'exit'.")
    pick = input(">> ")
    if pick == "exit":
        choosing = False
    elif pick == "show cart":
        show_cart_and_value(customer_cart)
    elif pick == "show stock":
        show_stock(current_stock)
    else:
        status = check_availability(pick, current_stock)
        if status == 'Available':
            customer_cart = add_to_cart(customer_cart, pick)
            current_stock = remove_from_stock(pick, current_stock)
            print("Item added.")
        elif status == "No More":
            print("We ran out of that item.")
        else:
            print("We dont have that item.")
        

print("Total amount to pay is:")
print("{} zł".format(sum_items(customer_cart, item_values)))