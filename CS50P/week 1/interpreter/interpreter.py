user_input = input ("Expression: ")

x = user_input.split()[0]
operator = user_input.split()[1]
y = user_input.split()[2]

floated_x = float(x)
floated_y = float(y)

if operator == "+":
    plus = floated_x + floated_y
    print (plus)

elif operator == "-":
    minus = floated_x - floated_y
    print (minus)

elif operator == "*":
    mutiply = floated_x * floated_y
    print (mutiply)

elif operator == "/":
    divide = floated_x / floated_y
    print (divide)

else:
    print("operator not valid")






