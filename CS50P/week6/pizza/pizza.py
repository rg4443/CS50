import sys
from tabulate import tabulate
import csv

pizza_list = []

if len(sys.argv) != 2:
    print("Please input exactly two command-line arguments")
    sys.exit(1)
else:
    file_name = sys.argv[1]
    if "." not in file_name:
        print("Please input a file name with a dot (.)")
        sys.exit(1)
    else:
        splitted = file_name.split(".")
        if splitted[-1] != "csv":
            print("Please input a CSV file")
            sys.exit(1)
        else:
            with open(file_name) as file:
                reader = csv.DictReader(file)
                # Extract headers dynamically from the CSV file
                headers = reader.fieldnames
                for row in reader:
                    pizza_dict = {}
                    for header in headers:
                        pizza_dict[header] = row[header]
                    pizza_list.append(pizza_dict)

            print(tabulate(pizza_list, headers="keys", tablefmt="grid"))
