import csv
import sys

def read_csv(file_name):
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        headers = next(reader)  # Use next() to get the header row
        data = list(reader)
    return headers, data

def compare_and_modify_data(data1, headers1, data2, headers2, key_column_name, target_column_name):
    key_index = headers2.index(key_column_name)
    target_index = headers1.index(target_column_name)

    for row2 in data2:
        key_value = row2[key_index].title()

        for row1 in data1:
            full_name = f"{row1[headers1.index('First Name')]} {row1[headers1.index('Last Name')]}"

            if full_name == key_value:
                # If names match, add the target column to data2
                row2.append(row1[target_index])
                break  # Break the inner loop once a match is found

    return headers2 + [target_column_name], data2

def write_csv(file_name, headers, data):
    with open(file_name, 'w', newline="") as f:
        writer = csv.writer(f)

        # Write headers
        writer.writerow(headers)

        # Write data to the output file
        writer.writerows(data)

def main():
    input_file_name = sys.argv[1]
    input_file_name_2 = sys.argv[2]
    output_file_name = "output.csv"

    # Read data from the first CSV file
    headers1, data1 = read_csv(input_file_name)

    #Read data from the second CSV file
    headers2, data2 = read_csv(input_file_name_2)

    # Compare and modify data2 with email addresses from data1
    key_column_name = "GM"
    target_column_name = "Employee Email Address"
    headers_out, data_out = compare_and_modify_data(data1, headers1, data2, headers2, key_column_name, target_column_name)

    # Write the modified data2 to the new output file
    write_csv(output_file_name, headers_out, data_out)

if __name__ == "__main__":
    main()
