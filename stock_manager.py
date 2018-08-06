import data_processing as data

print("""
Hi! Welcome to Stock Manager. What do you wanna do?
""")
usr_inpt = input("# ")

while True:
    if usr_inpt.lower() in ['quit', 'exit', 'q']:
        print("Goodbye!")
        break;
    elif usr_inpt.lower() == "add":
        name = input("Product name: ")
        quantity = input("Quantity: ")
        value = input("Value: ")
        data.add_item(name, quantity, value)
        print("{} {} added!".format(quantity, name))
    elif usr_inpt.lower() == "remove":
        data.remove_item() # TO DO
    elif usr_inpt.lower() == "edit":
        data.edit_item() # TO DO
    elif usr_inpt.lower() == "show":
        data.show() # TO DO
    else:
        print("Unknown command '{}', try again.".format(usr_inpt))
    usr_inpt = input("# ")
