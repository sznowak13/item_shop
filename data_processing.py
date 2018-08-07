import csv
STOCK_PATH = "./data/stock.csv"

def read_record(item_id, path = STOCK_PATH):
    with open(path) as f:
        records = f.readlines()
        output = {}
        record = records[int(item_id) - 1].split(',')
        output["ID"] = record[0]
        output["NAME"] = record[1]
        output["QUANTITY"] = record[2]
        output["VALUE"] = record[3]
        return output

def read_stock(path = STOCK_PATH):
    with open(path) as f:
        records = f.readlines()
        output = {}
        for i in range(len(records)):
            vals = records[i].split(',')
            output[vals[1]] = int(vals[2])
        return output

def read_values(path = STOCK_PATH):
    with open(path) as f:
        records = f.readlines()
        output = {}
        for i in range(len(records)):
            vals = records[i].split(',')
            output[vals[1]] = float(vals[3])
        return output

def add_item(name, quantity, value, path = STOCK_PATH):
    with open(path, "r+") as f:
        records = f.readlines()

        if len(records) < 9:
            item_id = "0" + str(len(records) + 1)
        else:
            item_id = str(len(records) + 1)

        record = [item_id, name.upper(), quantity, value, "\n"]
        f.write(",".join(record))

def remove_item(item_id, path = STOCK_PATH):
    with open(path, "r+") as f:
        records = f.readlines()
        records.pop(int(item_id) - 1)

        f.seek(0)
        f.truncate()

        for record in records:
            f.write(record)

def edit_item(path = STOCK_PATH):
    return None

def show(path = STOCK_PATH):
    with open(path, "r+") as f:
        records = f.readlines()
        print("ID || NAME || QUANTITY || VALUE")
        for i in range(len(records)):
            record = read_record(i + 1)
            # making name look fancy
            record["NAME"] = record["NAME"].title()
            print(*record.values())
