greeting = input("Greeting: ")

first = greeting.split()[0]
firstL = first[0]
if first == "Hello" or first == "Hello,":
    print("$0")

elif firstL == "H" and first != "Hello":
    print("$20")

else:
    print("$100")

