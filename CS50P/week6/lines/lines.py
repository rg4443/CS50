import sys

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
        if splitted[-1] != "py":
            print("Please input a Python file")
            sys.exit(1)
        else:
            line_count = 0
            with open(file_name) as file:
                for lines in file:
                    if lines.strip() and not lines.strip().startswith("#"):
                        line_count += 1

            print(line_count)
