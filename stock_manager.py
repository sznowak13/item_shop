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
        data.add_item()
    else:
        print("Unknown command '{}', try again.".format(usr_inpt))
    usr_inpt = input("# ")
