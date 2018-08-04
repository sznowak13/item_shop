def read_stock(records):
    output = {}
    for i in range(len(records)):
        vals = records[i].split(',')
        output[vals[1]] = int(vals[2])
    return output

def read_values(records):
    output = {}
    for i in range(len(records)):
        vals = records[i].split(',')
        output[vals[1]] = int(vals[3])
    return output
