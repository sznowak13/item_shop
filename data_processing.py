import csv, ui
STOCK_PATH = "./data/stock.csv"
FIELDNAMES = ["ID", "NAME", "QUANTITY", "VALUE"]

def read_record(item_id, path = STOCK_PATH):
    with open(path) as f:
        records = csv.DictReader(f)
        records_list = [record for record in records]
        return records_list[int(item_id) - 1]

def read_stock(path = STOCK_PATH):
    with open(path) as f:
        records = [record for record in csv.DictReader(f)]
        output = {}
        for record in records:
            output[record["NAME"]] = int(record["QUANTITY"])
        return output

def read_values(path = STOCK_PATH):
    with open(path) as f:
        records = [record for record in csv.DictReader(f)]
        output = {}
        for record in records:
            output[record["NAME"]] = float(record["VALUE"])
        return output

def add_item(item_dict, path = STOCK_PATH):
    with open(path, "a") as f:
        fieldnames = FIELDNAMES;
        writer = csv.DictWriter(f, fieldnames, lineterminator = '\n')
        writer.writerow(item_dict)

def remove_item(item_id, path = STOCK_PATH):
    with open(path, "r+") as f:
        records = f.readlines()
        records.pop(int(item_id))

        f.seek(0)
        f.truncate()

        for record in records:
            f.write(record)

def edit_item(path = STOCK_PATH):
    return None

def show(path = STOCK_PATH):
    with open(path, "r+") as f:
        records = csv.reader(f)
        records_list = [record for record in records]
        header = []
        for column_name in records_list[0]:
            header.append(column_name.title())
        records_list.pop(0)
        ui.print_table(records_list, header)
