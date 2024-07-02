import random
import sys

def main():
    level = get_level()

    if level:
        play_math_game(level)
    else:
        print("Invalid level. Exiting program.")

def get_user_input(prompt, is_level_input=False):
    while True:
        try:
            user_input = input(prompt)
            if is_level_input:
                # Check if the input is a digit
                if user_input.isdigit():
                    return int(user_input)
                else:
                    print("Invalid input. Please enter a valid number.")
            else:
                return int(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
def get_level():
    while True:
        level_input = get_user_input("Enter level (1, 2, or 3): ")
        if level_input in [1, 2, 3]:
            return level_input
        else:
            print("Invalid level. Please enter 1, 2, or 3.")

def generate_addition_problem(level):
    if level == 1:
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)
    elif level == 2:
        num1 = random.randint(10, 99)
        num2 = random.randint(10, 99)
    else:
        num1 = random.randint(100, 999)
        num2 = random.randint(100, 999)

    return num1, num2

def play_math_game(level):
    correct_answers = 0
    total_questions = 10
    max_attempts = 3
    incorrect_answers = 0

    for _ in range(total_questions):
        num1, num2 = generate_addition_problem(level)
        correct_answer = num1 + num2

        attempts = 0
        while attempts < max_attempts:
            user_answer = get_user_input(f"{num1} + {num2} = ")

            if user_answer == correct_answer:
                print("Correct!")
                correct_answers += 1
                break
            else:
                attempts += 1
                print("EEE")

        if attempts == max_attempts:
            print(f"{correct_answer}")
            incorrect_answers += 1

        if incorrect_answers == 3:
            print("You've reached the maximum number of incorrect answers. Game over.")
            return

    print(f"{correct_answers}")

if __name__ == "__main__":
    main()
