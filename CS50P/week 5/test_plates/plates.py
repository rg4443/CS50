def main():
    user_input = input("Plate: ")
    if is_valid(user_input):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    length = len(s)
    half_length = length // 2
    splited_first = s[:half_length]
    middle_char = s[half_length]

    # Check if the first two characters in splited_first are letters
    if splited_first[:2].isalpha():
        if 2 <= len(s) <= 6:
            # Check if there is at least one number in the last part
            if any(char.isdigit() for char in s[half_length:]) and s[half_length] != '0':
                # Check if there are no special characters in the plate
                special_characters = [".", " ", "(", ")", ",", ";", "'"]
                if all(char not in special_characters for char in s):
                    # Check if there are no integers in the middle
                    if not middle_char.isdigit():
                            return True

    return False

if __name__ == "__main__":
    main()
