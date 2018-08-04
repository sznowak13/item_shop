import cashing

current_stock = {
    'Food': 3,
    'Drink': 10,
    'Fags': 1
}

customer_cart = {}

def buy(pick, quantity = 1, stock = current_stock, cart = customer_cart):
    status = cashing.check_availability(pick, stock)
    if status == 'Available' and quantity <= stock[pick]:
        cashing.add_to_cart(cart, pick, quantity)
        cashing.remove_from_stock(pick, stock, quantity)
        return "Item(s) added."
    elif status == 'Available' and quantity > stock[pick]:
        print("Unfortunately, we don't have that much {}, but we can add the remaining {} to your cart. Kk? (y/n)".format(pick, stock[pick]))
        decision = input(">>")
        if decision.lower() == 'y':
            cashing.add_to_cart(cart, pick, stock[pick])
            cashing.remove_from_stock(pick, stock, stock[pick])
            return "Items added."
        else:
            return 'kthxbai'
    elif status == "No More":
        return "We ran out of that item."
    else:
        return "We dont have that item."

def print_help():
    print("""
Enter an item that you want to add to your cart.
You can also type in a quantity of that item separated by space,
if you want to add more than one, e.g.: 'Tomato 3' adds 3 tomatoes.
To see your cart - type 'show cart'.
To see the stock - type 'show stock'.
To see this message again - type 'help'.
To exit - type 'exit'.""")

choosing = True
print_help()

while choosing:
    pick = input(">> ")
    if pick == "exit":
        choosing = False
    elif pick == "help":
        print_help()
    elif pick == "show cart":
        cashing.show_cart_and_value(customer_cart)
    elif pick == "show stock":
        cashing.show_stock(current_stock)
    elif ' ' in pick:
        command = pick.split(' ')
        pick = command[0]
        try:
            quantity = int(command[1])
        except:
            command = "Unknown"
        if command == "Unknown" or quantity <= 0:
            print("something went wrong :/ type again")
            continue
        print(buy(pick, quantity))
    else:
        print(buy(pick))


print("Total amount to pay is:")
print("{} zł".format(cashing.sum_items(customer_cart)))
