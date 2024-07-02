import re
import sys


def main():
    try:
        print(convert(input("Hours: ")))
    except ValueError:
        raise ValueError("ValueError")

def convert(s):
    matches = re.search(r"(\d{1,2})?(?::(\d{1,2}))? +(AM|PM) +to +(\d{1,2})?(?::(\d{1,2}))? +(AM|PM)", s)

    if matches:
        first_digit = convert_part(matches.group(1), matches.group(2), matches.group(3))
        second_digit = convert_part(matches.group(4), matches.group(5), matches.group(6))

        return f"{first_digit} to {second_digit}"
    else:
        raise ValueError("ValueError")


def convert_part(hours, minutes, period):
    if hours:
        hours = int(hours)
        if not (0 <= hours <= 12):
            raise ValueError("ValueError")

    if minutes:
        minutes = int(minutes)
        if not (0 <= minutes < 60):
            raise ValueError("ValueError")

    if period not in ["AM", "PM"]:
        raise ValueError("ValueError")

    if period == "AM":
        if hours:
            # Special case for 12 AM
            if hours == 12:
                return f"00:{minutes or '00'}"
            else:
                return f"{hours:02}:{minutes or '00'}"
        elif minutes:
            return f"{minutes:02}:00"
        else:
            return "00:00"
    elif period == "PM":
        if hours:
            # Special case for 12 PM
            if hours == 12:
                return f"12:{minutes or '00'}"
            else:
                return f"{hours + 12:02}:{minutes or '00'}"
        elif minutes:
            return f"{hours + 12:02}:{minutes or '00'}"
        else:
            return "12:00"


if __name__ == "__main__":
    main()
