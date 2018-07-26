item_values = {
    'Food': 5,
    'Drink': 2,
    'Fags': 10
}
current_stock = {
    'Food': 3,
    'Drink': 10,
    'Fags': 1
}

def show_cart_and_value(cart, values=item_values):
    for item, amount in cart.items():
        print("{}: {}".format(item, amount))
    print("\nValue: {} zł".format(sum_items(cart, values)))
#jak nie ma stanów to smutna_baza.png
def show_stock(stock):
    items_available = 0
    for item, amount in stock.items():
        #żeby nie drukowało zerowych stanów
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
#teraz dodaje x do koszyka a nie po jednej sztuce jak za króla świeczka
def add_to_cart(cart, item, quantity = 1):
    if item in cart:
        cart[item] += quantity
    else:
        cart[item] = quantity
    return cart
#i analogicznie odejmuje
def remove_from_stock(item, stock, quantity = 1):
    stock[item] -= quantity
    return stock

def sum_items(cart, stock):
    item_sum = 0
    for item, amount in cart.items():
        item_sum += amount * stock[item]
    return item_sum

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
    print("\033c")
    if pick == "exit":
        choosing = False
    elif pick == "show cart":
        show_cart_and_value(customer_cart)
    elif pick == "show stock":
        show_stock(current_stock)
    #tutej implementacja kupowania paru sztuk na raz
    elif ' ' in pick:
        command = pick.split(' ')
        pick = command[0]
        quantity = int(command[1])
        status = check_availability(pick, current_stock)
        #paczej kurwa jak szprytnie, nawet sprawdza czy ma tyle na stanie
        if status == 'Available' and quantity <= current_stock[pick]:
            customer_cart = add_to_cart(customer_cart, pick, quantity)
            current_stock = remove_from_stock(pick, current_stock, quantity)
            print("Item(s) added.")
        #a jak nie ma to pyta czy starczy tyle co ma
        elif status == 'Available' and quantity > current_stock[pick]:
            print("Unfortunately, we don't have that much {}, but we can add the remaining {} to your cart. Kk? (y/n)".format(pick, current_stock[pick]))
            decision = input(">>")
            if decision.lower() == 'y':
                customer_cart = add_to_cart(customer_cart, pick, current_stock[pick])
                current_stock = remove_from_stock(pick, current_stock, current_stock[pick])
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
