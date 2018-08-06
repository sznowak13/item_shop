stock_path = "./data/stock.csv"

def read_stock(path = stock_path):
    with open(path) as f:
        records = f.readlines()
        output = {}
        for i in range(len(records)):
            vals = records[i].split(',')
            output[vals[1]] = int(vals[2])
        return output

def read_values(path = stock_path):
    with open(path) as f:
        records = f.readlines()
        output = {}
        for i in range(len(records)):
            vals = records[i].split(',')
            output[vals[1]] = float(vals[3])
        return output

def add_item(name, quantity, value, path = stock_path):
    with open(path, "r+") as f:
        records = f.readlines()

        if len(records) < 9:
            id = "0" + str(len(records) + 1)
        else:
            id = str(len(records) + 1)

        record = [id, name.upper(), quantity, value, "\n"]
        f.write(",".join(record))

def remove_item(path = stock_path):
    return None

def edit_item(path = stock_path):
    return None

def show(path = stock_path):
    return None
