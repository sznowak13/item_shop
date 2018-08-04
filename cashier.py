import cashing

current_stock = {
    'Food': 3,
    'Drink': 10,
    'Fags': 1
}

choosing = True
customer_cart = {}
#wypierdoliłem to przed pętle bo mnie wkurwiało za każdym razem wyskakiwanie tego
#i sformatowałem to ładniej.
print("""
Enter an item that you want to add to your cart.
You can also type in a quantity of that item separated by space,
if you want to add more than one, e.g.: 'Tomato 3' adds 3 tomatoes.
To see your cart - type 'show cart'.
To see the stock - type 'show stock'.
To exit - type 'exit'.""")

while choosing:
    pick = input(">> ")
    #na chuj Ci ten chujwie jaki escape
    if pick == "exit":
        choosing = False
    elif pick == "show cart":
        cashing.show_cart_and_value(customer_cart)
    elif pick == "show stock":
        cashing.show_stock(current_stock)
    #tutej implementacja kupowania paru sztuk na raz
    elif ' ' in pick:
        command = pick.split(' ')
        pick = command[0]
        quantity = int(command[1])
        status = cashing.check_availability(pick, current_stock)
        #paczej kurwa jak szprytnie, nawet sprawdza czy ma tyle na stanie
        if status == 'Available' and quantity <= current_stock[pick]:
            customer_cart = cashing.add_to_cart(customer_cart, pick, quantity)
            current_stock = cashing.remove_from_stock(pick, current_stock, quantity)
            print("Item(s) added.")
        #a jak nie ma to pyta czy starczy tyle co ma
        elif status == 'Available' and quantity > current_stock[pick]:
            print("Unfortunately, we don't have that much {}, but we can add the remaining {} to your cart. Kk? (y/n)".format(pick, current_stock[pick]))
            decision = input(">>")
            if decision.lower() == 'y':
                customer_cart = cashing.add_to_cart(customer_cart, pick, current_stock[pick])
                current_stock = cashing.remove_from_stock(pick, current_stock, current_stock[pick])
                print("Items added.")
            else:
                print('kthxbai')
                continue
        elif status == "No More":
            print("We ran out of that item.")
        else:
            print("We dont have that item.")
    #kuniec implementacji
    else:
        status = cashing.check_availability(pick, current_stock)
        if status == 'Available':
            customer_cart = cashing.add_to_cart(customer_cart, pick)
            current_stock = cashing.remove_from_stock(pick, current_stock)
            print("Item added.")
        elif status == "No More":
            print("We ran out of that item.")
        else:
            print("We dont have that item.")


print("Total amount to pay is:")
print("{} zł".format(cashing.sum_items(customer_cart)))
