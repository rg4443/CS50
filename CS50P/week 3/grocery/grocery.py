total = 0.0
users_grocerys = {}

while True:
    try:
        user_input = input("")
        if not user_input:
            break

        item = user_input.upper()
        #create count so that it that adds up user's input
        total += 1
        if item in users_grocerys:
            users_grocerys[item] += 1
        else:
            users_grocerys[item] = 1

    except EOFError:
        for grocery, number in sorted(users_grocerys.items()):
            print(f"{number} {grocery}")
        break
