import csv
from inspect import Traceback


def command_menu():
    print("COMMAND MENU")
    print(
        "monthly - View monthly sales\n"
        + "yearly - View yearly summary\n"
        + "edit - Edit sales for a month\n"
        + "exit - Exit program\n"
    )


def open_read_csv():
    try:
        with open("monthly_sales.csv") as data_file:
            data = csv.reader(data_file)
            sales = []
            for row in data:
                sales.append([row[0], int(row[1])])
            return sales
    except:
        print("ERROR CSV FILE NOT FOUND OR COULDN'T BE READ")
        exit()


def save_to_csv(monthly_sales_list):
    with open("monthly_sales.csv", "w") as data_file:
        writer = csv.writer(data_file)
        for row in monthly_sales_list:
            writer.writerow([row[0], int(row[1])])


def monthly(monthly_sales_list):
    for row in monthly_sales_list:
        print(f'{row[0]} - {",".join(map(str, row[1:]))}')

    print("\n")


def yearly(monthly_sales_list):
    total_sales = 0
    for row in monthly_sales_list:
        total_sales += row[1]
    average = total_sales / len(monthly_sales_list)
    print(f"Yearly total: {total_sales}")
    print(f"Monthly Average: {round(average,2)}\n")


def edit(monthly_sales_list):
    months = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    ]
    month = input("Three-letter Month: ")
    if month not in months:
        print("Invalid three-letter month.\n")
    else:
        index_of_month = months.index(month)
        sales_for_month = int(input("Sales Amount: "))
        monthly_sales_list[index_of_month][1] = sales_for_month
        save_to_csv(monthly_sales_list)
        print(f"Sales amount for {month} was modified.\n")


def main():
    print("Monthly Sales program\n")
    monthly_sales_list = open_read_csv()
    command_menu()
    while True:
        command = input("command: ")
        if command == "monthly":
            monthly(monthly_sales_list)
        elif command == "yearly":
            yearly(monthly_sales_list)
        elif command == "edit":
            edit(monthly_sales_list)
        elif command == "exit":
            print("Bye!")
            exit()


if __name__ == "__main__":
    main()
