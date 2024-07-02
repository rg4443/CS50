import random

while True:
    try:
        # Validating to make sure that inputs are postitive integers
        level_input = int(input("Level: "))
        user_input = int(input("Guess: "))
        if level_input < 0 or user_input < 0:
            print("Please Input a Positive Integer")
            continue

        break

    except ValueError:
        print("Please input an Integer")

randomizer = random.randrange(1, level_input + 1)

while True:
    if user_input < randomizer:
        print("Too Small!")
    elif user_input > randomizer:
        print("Too Large!")
    else:
        print("Just right!")
        break

    user_input = int(input("Guess: "))

print(randomizer)
