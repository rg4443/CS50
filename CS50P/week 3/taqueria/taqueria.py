def main():
    price = {
        "baja taco": 4.25,
        "burrito": 7.50,
        "bowl": 8.50,
        "nachos": 11.00,
        "quesadilla": 8.50,
        "super burrito": 8.50,
        "super quesadilla": 9.50,
        "taco": 3.00,
        "tortilla salad": 8.00
    }

    total = 0.0  # Initialize the total variable outside the loop

    try:
        while True:
            user_input = input("Item: ").lower()
            if user_input in price:
                item_price = price[user_input]
                total += item_price  # Add the item price to the total
                formatted_total = "${:.2f}".format(total)  # Include "$" symbol in the output
                print(formatted_total)
            else:
                print("Not in Menu, Please Input Again")
    except EOFError:
        pass  # Ignore EOFError

main()
