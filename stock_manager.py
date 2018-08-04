import data_processing as data

file = open("./data/stock.csv", "r+")
records = file.readlines()

print("""
Hi! Welcome to Stock Manager. What do you wanna do? Add something to the stock? Okey-dokey!
""")
if len(records) < 9:
    id = "0" + str(len(records))
else:
    id = str(len(records))
name = input("Product name: ")
quantity = input("Quantity: ")
value = input("Value: ")

record = [id, name.upper(), quantity, value, "\n"]
file.write(",".join(record))

print("Done, thanks!")

file.close()
