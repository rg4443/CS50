def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    try:
        s = ip.split(".")
        numbers = int(s[0]), int(s[1]), int(s[2]), int(s[3])
        if len(s) == 4:
            if 0 <= numbers[0] <= 255 and 0 <= numbers[1] <= 255 and 0 <= numbers[2] <= 255 and 0 <= numbers[3] <= 255:
                return True
            else:
                return False
        else:
            return False
    except (ValueError, IndexError):
        return False


if __name__ == "__main__":
    main()
