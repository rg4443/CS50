import inflect

p = inflect.engine()

inputs = []

while True:
    try:
        user_input = input("")

        inputs.append(user_input)

        # Join the inputs outside the loop
        result = p.join(inputs)
        print("Adieu, adieu, to " + result)
    except EOFError:
        break

