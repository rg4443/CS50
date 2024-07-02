def main():
    user_input = input("Input: ")
    print(shorten(user_input))


#removes vowels from input
def shorten(word):
    vowel_list = ["a", "e", "i", "o", "u"]
    # start the result with blank
    result_str = ""
    # for loop to iterate through each letter of input and output letter if it is not in the list of vowels
    for char in word:
        # check if the character is not a vowel
        if char.lower() not in vowel_list:
            result_str += char
    return result_str

if __name__ == "__main__":
    main()

