def main():
    try:
        user_input = input("What is the time? ")
        converted_time = convert(user_input)

        if 7.0 <= converted_time <= 8.0:
            print("Breakfast time")
        elif 12.0 <= converted_time <= 13.0:
            print("Lunch time")
        elif 18.0 <= converted_time <= 19.0:
            print("Dinner time")
        else:
            print("Not meal time")

    except ValueError as e:
        print(f"Error: {e}")

def convert(time):
    split_time = time.split(":")

    if len(split_time) != 2:
        raise ValueError("Invalid time format. Please enter time in HH:MM format.")

    hours, minutes = map(int, split_time)
    result = hours + minutes / 60.0
    return result

if __name__ == "__main__":
    main()
