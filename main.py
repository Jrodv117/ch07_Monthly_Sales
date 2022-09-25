import csv

with open("monthly_sales.csv") as data_file:
    data = csv.reader(data_file)
    for row in data:
        print(row)
