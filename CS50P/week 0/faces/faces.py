def convert(str):
    converted = str.replace(":)","🙂").replace(":(", "🙁").replace(":(", "🙁")
    return converted

def main():
    user_input = input("")
    print(convert(user_input))

main()
