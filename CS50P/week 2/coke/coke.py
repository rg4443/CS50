def main():
    total_paid = 0
    amount_due = 50  

    while total_paid < 50:
        user_input = input("Insert Coin: ")

        validated = validation(user_input)

        if validated:
            total_paid = caculation(validated, total_paid)
            amount_due = 50 - total_paid
            if amount_due <= 0:
                break  # Exit the loop if the amount due hits 0
        print(f"Amount Due: {amount_due}")

    change_owed = total_paid - 50
    print("Change Owed:", max(0, change_owed))  # Ensure the change owed is not negative

# Validation function that ensures the user inputs a denomination of either 5, 10, or 25
def validation(input):
    denominations = [5, 10, 25]
    user_input = int(input)
    if user_input in denominations:
        return user_input
    else:
        return False

def caculation(input, total_paid):
    user_input = int(input)

    if user_input in [5, 10, 25]:
        total_paid += user_input  # Update total_paid based on the inserted coin

    return total_paid

if __name__ == "__main__":
    main()
