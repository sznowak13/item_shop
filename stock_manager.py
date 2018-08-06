import data_processing as data

def print_help():
    print("Command list:\n-Add\n-Remove (DANGEROUS! IN PROGRESS!)\n-Edit (NOT AVAILABLE)\n-Show (IN PROGRESS)\n-Help\n-Quit")

print("Hi! Welcome to Stock Manager. What do you wanna do?")
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
        id = input("Type the product's ID: ")
        item = data.read_record(id)
        decision = input("Are you sure you want to remove {} from stock? ".format(item["NAME"].title()))
        if decision.lower() in ['yes', 'y']:
            data.remove_item(id)
            print("Item removed.")
        else:
            print("Oof, that was close.")
    elif usr_inpt.lower() == "edit":
        data.edit_item() # TO DO
    elif usr_inpt.lower() == "show":
        data.show()
    elif usr_inpt.lower() == "help":
        print_help()
    else:
        print("Unknown command '{}', try again.".format(usr_inpt))
    usr_inpt = input("# ")
