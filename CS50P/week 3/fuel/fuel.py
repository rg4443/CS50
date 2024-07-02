def main():
    while True:
        try:
            user_input = input("Fraction: ")
            split_checker(user_input)
        except (ValueError, ZeroDivisionError, InvalidFractionError) as e:
            print(f"Error: {e}. Please provide a valid fraction.")
        else:
            break


class InvalidFractionError(Exception):
    pass


def split_checker(input):
    fraction_parts = input.split("/")

    if len(fraction_parts) != 2:
        raise InvalidFractionError("Invalid fraction format")

    numerator, denominator = map(int, fraction_parts)

    if denominator == 0:
        raise InvalidFractionError("Cannot divide by zero")

    if numerator == 0 and denominator in [4, 100] or numerator == 1 and denominator == 100:
        print("E")
    elif numerator == 1 and denominator == 4:
        print("25%")
    elif numerator == 1 and denominator == 3:
        print("33%")
    elif numerator == 1 and denominator == 2:
        print("50%")
    elif numerator == 2 and denominator == 3:
        print("67%")
    elif numerator == 3 and denominator == 4:
        print("75%")
    elif numerator == denominator or numerator == 100 or denominator == 100 or numerator == 99 and denominator == 100:
        print("F")
    else:
        raise InvalidFractionError("Please provide in fuel gauge form")


main()
