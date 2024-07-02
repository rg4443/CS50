import sys
import csv

if len(sys.argv) != 3:
    print("Please input exactly three command-line arguments")
    sys.exit(1)
else:
    input_file_name = sys.argv[1]
    output_file_name = sys.argv[2]

    if "." not in input_file_name:
        print("Please input a file name with a dot (.)")
        sys.exit(1)
    else:
        splitted = input_file_name.split(".")
        if splitted[-1] != "csv":
            print("Please input a CSV file")
            sys.exit(1)
        else:
            with open(input_file_name, newline='') as input_file:
                reader = csv.DictReader(input_file)
                input_lines = list(reader)

            # Split the names and assign to the "last" variable
            for row in input_lines:
                if 'name' in row:
                    name_parts = row['name'].split(', ', 1)
                    row['first'] = name_parts[1]
                    row['last'] = name_parts[0] if len(name_parts) > 1 else ''
                    del row['name']

            with open(output_file_name, "w", newline='') as output_file:
                # Rewrite fieldnames
                fieldnames = ["first", "last", "house"]
                writer = csv.DictWriter(output_file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(input_lines)
