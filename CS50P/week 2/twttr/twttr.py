def main():
    user_input = input("Input: ")
    result = vowel_destroyer(user_input)
    print(result)


#removes vowels from input
def vowel_destroyer(input):
    vowel_list = ["a", "e", "i", "o", "u"]
    # for loop to iterate through each letter of input
    result_str = ""
    for char in input:
        # check if the character is not a vowel
        if char.lower() not in vowel_list:
            result_str += char

    return result_str




main()
