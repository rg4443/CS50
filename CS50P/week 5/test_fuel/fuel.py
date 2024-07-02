def main():
    while True:
        try:
            user_input = input("Fraction: ")
            result = convert(user_input)
            print(gauge(result))
        except (ValueError, ZeroDivisionError):
            print("Please provide a valid fraction.")
        else:
            break


def convert(fraction):
    try:
        numerator, denominator = map(int, fraction.split("/"))
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise ValueError("Both numerator and denominator must be integers.")
        if denominator == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        if numerator > denominator:
            raise ValueError("Numerator must be less than or equal to denominator.")
        percentage = round((numerator / denominator) * 100)
        return percentage
    except ValueError:
        raise ValueError("Invalid fraction format:")


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
