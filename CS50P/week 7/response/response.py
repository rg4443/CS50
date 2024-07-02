import validators

user_input = input("Email: ")
validator = validators.email(user_input)

if validator:
    print("Valid")
else:
    print("Invalid")
