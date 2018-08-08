import data_processing as data
import ui
COMMAND_LIST = ['Add', 'Remove', 'Edit', 'Show', 'Help', 'Quit']

print("Hi! Welcome to Stock Manager. For instructions type 'help'.")
usr_inpt = input("# ")

while True:
    if usr_inpt.lower() in ['quit', 'exit', 'q']:
        print("Goodbye!")
        break
    elif usr_inpt.lower() == "add":
        values = [] # list of the values to be passed to the dictionary
        # max_id = int(data.read_record()["ID"]) # reads the maximal ID so far
        values.append(data.get_id())
        values.append(input("Product name: ").upper())
        values.append(input("Quantity: "))
        values.append(input("Value: "))
        # unpacking the values to the proper dictionary with keys from FIELDNAMES constant
        item_dict = {title: values[data.FIELDNAMES.index(title)] for title in data.FIELDNAMES}
        data.add_item(item_dict)
        print("{} {} added!".format(values[2], values[1].title()))
    elif usr_inpt.lower() == "remove":
        item_id = input("Type the product's ID: ")
        item = data.read_record(item_id)
        if item == None:
            print("No item with ID '{}'".format(item_id))
        else:
            decision = input("Are you sure you want to permanently remove {} from stock? ".format(item["NAME"].title()))
            if decision.lower() in ['yes', 'y']:
                data.remove_item(item_id)
                print("Item removed.")
            else:
                print("Oof, that was close.")
    elif usr_inpt.lower() == "edit":
        item_id = input("Type the product's ID: ")
        item = data.read_record(item_id)
        if item == None:
            print("No item with ID '{}'".format(item_id))
        else:
            updated_name = input("Change the name ({}): ".format(item["NAME"].title()))
            if updated_name != "":
                item["NAME"] = updated_name.upper()
            updated_quantity = input("Change the quantity ({}): ".format(item["QUANTITY"]))
            if updated_quantity != "":
                item["QUANTITY"] = updated_quantity
            updated_value = input("Change the value ({}): ".format(item["VALUE"]))
            if updated_value != "":
                item["VALUE"] = updated_value
            data.edit_item(item)
            print("Item updated!")
    elif usr_inpt.lower() == "show":
        data.show()
    elif usr_inpt.lower() == "help":
        ui.print_menu("List of supported commands", COMMAND_LIST)
    else:
        print("Unknown command '{}', try again.".format(usr_inpt))
    usr_inpt = input("# ")
