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
        customer_cart = cashing.add_to_cart(cart, pick, quantity)
        current_stock = cashing.remove_from_stock(pick, stock, quantity)
        print("Item(s) added.")
    elif status == 'Available' and quantity > stock[pick]:
        print("Unfortunately, we don't have that much {}, but we can add the remaining {} to your cart. Kk? (y/n)".format(pick, stock[pick]))
        decision = input(">>")
        if decision.lower() == 'y':
            customer_cart = cashing.add_to_cart(cart, pick, stock[pick])
            current_stock = cashing.remove_from_stock(pick, stock, stock[pick])
            print("Items added.")
        else:
            print('kthxbai')
    elif status == "No More":
        print("We ran out of that item.")
    else:
        print("We dont have that item.")

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
    #tutej implementacja kupowania paru sztuk na raz
    elif ' ' in pick:
        command = pick.split(' ')
        pick = command[0]
        try:
            quantity = int(command[1])
        except:
            print("something went wrong :/ type again")
            continue
        buy(pick, quantity)
    else:
        buy(pick)


print("Total amount to pay is:")
print("{} zł".format(cashing.sum_items(customer_cart)))
