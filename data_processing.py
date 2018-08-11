""" A module for manipulation of the csv file containing some kind of stock """

from tempfile import NamedTemporaryFile as nametempfile
from random import randrange
import csv, ui, shutil
import os

STOCK_PATH = "./data/stock.csv"
FIELDNAMES = ["ID", "NAME", "QUANTITY", "VALUE"]
ID_LENGTH = 6

def setup_stock():
    """
    Checks if the stock file exists in the data folder.
    If not, creates a new stock file with no items and displays an error.
    """
    
    if not os.path.exists(STOCK_PATH):
        data_dir = os.path.dirname(STOCK_PATH)
        os.makedirs(data_dir)
        with open(STOCK_PATH, 'w') as f:
            writer = csv.DictWriter(f, fieldnames = FIELDNAMES, lineterminator = '\n')
            writer.writeheader()
        ui.print_error_message("Cannot find a file, mght be deleted or moved.")
        ui.print_result("Created an empty datafile", "Handled")


def get_id(path = STOCK_PATH):
    """ Generates random, unique, ID_LENGTH-digit ID string (supports 10^6 unique products)"""
    with open(path) as f:
        records = csv.DictReader(f)
        all_ids = [record["ID"] for record in records]
        unique = False
        while not unique:
            new_id = "".join([str(randrange(0, 10)) for i in range(ID_LENGTH)])
            if new_id not in all_ids:
                unique = True
        return new_id

def read_record(item_id = 0, path = STOCK_PATH):
    """ Returns record from the csv file with given ID.
    If no arguments are passed, returns the last item from the file.
    If no match is found in the file, returns None.
    """
    with open(path) as f:
        records = csv.DictReader(f)
        if item_id == 0:
            return [record for record in records][-1]
        for record in records:
            if record["ID"] == item_id:
                return record
        return None

def read_stock(path = STOCK_PATH):
    """ Returns a dictionary in form of NAME: QUANTITY for every item in the stock """
    with open(path) as f:
        records = [record for record in csv.DictReader(f)]
        output = {}
        for record in records:
            output[record["NAME"]] = int(record["QUANTITY"])
        return output

def read_values(path = STOCK_PATH):
    """ Returns a dictionary in form of NAME: VALUE for every item in the stock """
    with open(path) as f:
        records = [record for record in csv.DictReader(f)]
        output = {}
        for record in records:
            output[record["NAME"]] = float(record["VALUE"])
        return output

def add_item(item_dict, path = STOCK_PATH):
    """ Adds a record to the csv file given a dictionary with FIELDNAMES as keys """
    with open(path, "a") as f:
        fieldnames = FIELDNAMES;
        writer = csv.DictWriter(f, fieldnames, lineterminator = '\n')
        writer.writerow(item_dict)

def remove_item(item_id, path = STOCK_PATH):
    """ Removes a record from the csv file given an items ID """
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


def edit_item(item, path = STOCK_PATH):
    """ Updates a record with item's ID to the values of given item dictionary """
    tempfile = nametempfile(mode = 'w', delete = False)
    with open(path) as csvfile, tempfile:
        reader = csv.DictReader(csvfile, fieldnames = FIELDNAMES)
        writer = csv.DictWriter(tempfile, fieldnames = FIELDNAMES, lineterminator = '\n')
        for record in reader:
            if record["ID"] == item["ID"]:
                record["NAME"], record["QUANTITY"], record["VALUE"] = item["NAME"], item["QUANTITY"], item["VALUE"]
            writer.writerow(record)
    shutil.move(tempfile.name, path)

def show(path = STOCK_PATH):
    """ Displays a fancy looking table of every item in the given stock """
    with open(path, "r+") as f:
        records = csv.reader(f)
        records_list = [record for record in records]
        header = []
        for column_name in records_list[0]:
            header.append(column_name.title())
        records_list.pop(0)
        ui.print_table(records_list, header)
