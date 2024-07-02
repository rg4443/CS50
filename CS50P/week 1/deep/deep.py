user_input = input("What is the answer to the Great Question of Life, the Universe and Everything? ")

lowered_user_input = user_input.lower().strip()

if lowered_user_input == "42" or lowered_user_input == "forty-two" or lowered_user_input == "forty two":
    print("Yes")
else:
    print("No")
