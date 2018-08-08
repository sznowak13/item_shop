import csv, ui
STOCK_PATH = "./data/stock.csv"
FIELDNAMES = ["ID", "NAME", "QUANTITY", "VALUE"]

def read_record(item_id = 0, path = STOCK_PATH):
    """ Returns record from the csv file with given ID.
    If no arguments are passed, returns the last item from the file.
    If no match is found in the file, returns Null.
    """
    with open(path) as f:
        records = csv.DictReader(f)
        if item_id == 0:
            return [record for record in records][-1]
        for record in records:
            if record["ID"] == item_id:
                return record
        return Null

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
        fieldnames = FIELDNAMES;
        records = [record for record in csv.DictReader(f)]
        records.insert(0, {key: key for key in fieldnames})
        for record in records:
            if record["ID"] == item_id:
                records.pop(records.index(record))

        f.seek(0)
        f.truncate()

        for record in records:
            add_item(record)


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
