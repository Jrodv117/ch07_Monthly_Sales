import csv


def open_read_csv():
    with open("monthly_sales.csv") as data_file:
        data = csv.reader(data_file)
        sales = []
        for row in data:
            sales.append([row[0], int(row[1])])
        print(sales)
