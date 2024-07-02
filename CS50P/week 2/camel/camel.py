def main():
    input_str = input("camelCase: ")
    converted_snake_case = convert_to_snake_case(input_str)
    print("snake_case:", converted_snake_case)

def spliter(input_str):
    if uppercase_checker(input_str):
        splitted = split_on_uppercase(input_str)
        snake_case_substrings = convert_to_snake_case(splitted)
        return snake_case_substrings

def uppercase_checker(input_str):
    for char in input_str:
        if char.isupper():
            return True
    else:
        return False

def split_on_uppercase(input_str):
    result = []
    current_word = ''

    for char in input_str:
        if char.isupper():
            if current_word:
                result.append(current_word)
            current_word = char
        else:
            current_word += char

    if current_word:
        result.append(current_word)

    return result

def convert_to_snake_case(input_str):
    snake_case_str = ''

    for char in input_str:
        if char.isupper():
            snake_case_str += '_' + char.lower()
        else:
            snake_case_str += char

    # Remove leading underscore (if any)
    if snake_case_str.startswith('_'):
        snake_case_str = snake_case_str[1:]

    return snake_case_str


if __name__ == "__main__":
    main()
