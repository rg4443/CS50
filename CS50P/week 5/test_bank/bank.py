def main():
    greeting = input("Greeting: ")
    print(value(greeting))


def value(greeting):
    first = greeting.split()[0]
    firstL = first[0]
    if first == "Hello" or first == "Hello,":
        return 0

    elif firstL == "H" and first != "Hello":
        return 20

    else:
        return 100

if __name__ == "__main__":
    main()
