# main function, each function below it only executes if the one before it returns true
def main():
    user_input = input("Plate: ")
    check = no_special_characters(user_input)
    if check:
        print("Valid")
    else:
        print("Invalid")

#makes sure that there are at least two char in input
def two_letter_checker(input):
    length = len(input)
    half_length = length // 2
    splited_first = input[:half_length]

    # Check if the first two characters in splited_first are letters
    if splited_first[:2].isalpha():
        return True
    else:
        return False

# function that makes sure that there is a min of two char and a max of six char
def min_two_char_max_six_char(input):
    # have the function only operate if previous functions returns true
    if two_letter_checker(input):
        if 2 <= len(input) <= 6:
            return True
        else:
            return False
    else:
        return False


#function that makes sure there is no number in the middle of input and that the first number inputted is 0.
def middle_number_checker(input):
    if min_two_char_max_six_char(input):
        length = len(input)
        half_length = length // 2
        splited_last = input[half_length:]

        # Check if there is at least one number in splited_last
        if any(char.isdigit() for char in splited_last) and splited_last[0] != '0':
            return True
        else:
            return False
    else:
        return False

#function that makes sure there are no special characters
def no_special_characters(input):
    if middle_number_checker(input):
        special_characters = [".", " ", "(", ")", ",", ";", "'"]
        for char in input:
            if char in special_characters:
                return False
        return True
    else:
        return False



main()
