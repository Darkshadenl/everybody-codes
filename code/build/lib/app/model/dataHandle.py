import csv

data = []

with open('../data/cameras-defb.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')

    for row in reader:
        data.append(row)