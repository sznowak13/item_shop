import data_processing as data
import ui

def get_quantity(prompt):
    output = input(prompt)
    correct = False
    while output and not correct:
        try:
            if int(output) < 0:
                print("The quantity has to be a positive number.")
                output = input(prompt)
                continue
            correct = True
        except:
            print("You have to pass an integer value.")
            output = input(prompt)
    return output

def get_value(prompt):
    output = input(prompt)
    correct = False
    while output and not correct:
        try:
            if float(output) < 0:
                print("The value has to be a positive number.")
                output = input(prompt)
                continue
            correct = True
        except:
            print("You have to pass a floating point value.")
            output = input(prompt)
    return output

def quit_program():
    """ Quits the program, duh. Also, typing 'q' or 'exit' have the same effect."""
    return False


COMMAND_DICT = {'Add': data.add_item, 'Remove': data.remove_item, 'Edit': data.edit_item, 'Show': data.show, 'Help': help, 'Quit': quit_program}

def main():
    running = True
    data.setup_stock()
    print("Hi! Welcome to Stock Manager. For instructions type 'help'.")
    usr_inpt = input("# ")

    while running:
        usr_inpt = usr_inpt.split(' ')
        command = usr_inpt[0]
        if command.lower() in ['quit', 'exit', 'q']:
            print("Goodbye!")
            running = quit_program()
            continue
        elif command.lower() == "add":
            values = [] # list of the values to be passed to the dictionary
            values.append(data.get_id())
            values.append(input("Product name: ").upper())
            quantity = get_quantity("Quantity: ")
            if quantity == "": values.append(0)
            else: values.append(quantity)
            value = get_value("Value: ")
            if value == "": values.append(0)
            else: values.append(value)
            # unpacking the values to the proper dictionary with keys from FIELDNAMES constant
            item_dict = {title: values[data.FIELDNAMES.index(title)] for title in data.FIELDNAMES}
            data.add_item(item_dict)
            print("{} {} added!".format(values[2], values[1].title()))
        elif command.lower() == "remove":
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
        elif command.lower() == "edit":
            item_id = input("Type the product's ID: ")
            item = data.read_record(item_id)
            if item == None:
                print("No item with ID '{}'".format(item_id))
            else:
                updated_name = input("Change the name ({}): ".format(item["NAME"].title()))
                if updated_name != "": item["NAME"] = updated_name.upper()
                updated_quantity = get_quantity("Change the quantity ({}): ".format(item["QUANTITY"]))
                if updated_quantity != "": item["QUANTITY"] = updated_quantity
                updated_value = get_value("Change the value ({}): ".format(item["VALUE"]))
                if updated_value != "": item["VALUE"] = updated_value
                data.edit_item(item)
                print("Item updated!")
        elif command.lower() == "show":
            data.show()
        elif command.lower() == "help":
            if len(usr_inpt) > 1:
                argument = usr_inpt[1].title()
                if argument == "Help":
                    print("Really?")
                elif argument in list(COMMAND_DICT.keys()):
                    print(COMMAND_DICT[argument].__doc__)
                else:
                    print("Unknown argument for command 'help' - '{}'".format(argument))
            else:
                ui.print_menu("List of supported commands", list(COMMAND_DICT.keys()))
                print("To see help for specified command, type 'help COMMAND'")
        else:
            print("Unknown command '{}', try again.".format(command))
        usr_inpt = input("# ")


if __name__ == "__main__":
    main()
