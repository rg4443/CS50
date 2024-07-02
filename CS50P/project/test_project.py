import unittest
from project import read_csv, compare_and_modify_data, write_csv

def test_read_csv():
    file1 = "Daily.csv"
    file2 = "Aging.csv"

    headers1, data1 = read_csv(file1)
    headers2, data2 = read_csv(file2)

    assert isinstance(headers1, list)
    assert isinstance(data1, list)
    assert isinstance(headers2, list)
    (data2, list)

def test_compare_and_modify_data():
    # Your test data
    data1 = [['First Name', 'Last Name', 'Employee Email Address'],
             ['John', 'Doe', 'john.doe@email.com']]
    headers1 = data1[0]

    data2 = [['GM'], ['John Doe']]
    headers2 = data2[0]

    key_column_name = 'GM'
    target_column_name = 'Employee Email Address'

    headers_out, data_out = compare_and_modify_data(data1, headers1, data2, headers2, key_column_name, target_column_name)

    assert isinstance(headers_out, list)
    assert isinstance(data_out, list)


def test_write_csv():
    # Your test data
    file_name = "output.csv"
    headers = ['GM', 'Employee Email Address']
    data = [['John Doe', 'john.doe@email.com']]

    write_csv(file_name, headers, data)

if __name__ == '__main__':
    unittest.main()
