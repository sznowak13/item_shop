import data_processing as data

def print_help():
    print("Command list:\n-Add\n-Remove (DANGEROUS! IN PROGRESS!)\n-Edit (NOT AVAILABLE)\n-Show (IN PROGRESS)\n-Help\n-Quit")

print("Hi! Welcome to Stock Manager. What do you wanna do?")
usr_inpt = input("# ")

while True:
    if usr_inpt.lower() in ['quit', 'exit', 'q']:
        print("Goodbye!")
        break
    elif usr_inpt.lower() == "add":
        values = []
        max_id = int(data.read_record(0)["ID"]) # reads the maximal ID so far
        if max_id < 9:
            values.append("0" + str(max_id + 1))
        else:
            values.append(str(max_id + 1))
        values.append(input("Product name: ").upper())
        values.append(input("Quantity: "))
        values.append(input("Value: "))
        item_dict = {title: values[data.FIELDNAMES.index(title)] for title in data.FIELDNAMES}
        data.add_item(item_dict)
        print("{} {} added!".format(values[2], values[1].title()))
    elif usr_inpt.lower() == "remove":
        item_id = input("Type the product's ID: ")
        item = data.read_record(item_id)
        decision = input("Are you sure you want to remove {} from stock? ".format(item["NAME"].title()))
        if decision.lower() in ['yes', 'y']:
            data.remove_item(item_id)
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
