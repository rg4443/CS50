months = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12"
}

while True:
    try:
        user_input = input("Date: ")
        # Split the input using both "/" and " "
        splitted = user_input.replace(',', '').replace('/', ' ').split()
        month_input = splitted[0]
        day = splitted[1]
        year = splitted[2]

        # Check to see if month = str if so, make sure user does not input / then reject | if not continue
        if not month_input.isdigit() and '/' in user_input:
            print("Invalid Format, Please Input Again")
            continue

        # Check if month_input is a full month name
        if month_input in months:
            month = months[month_input]
        elif len(month_input) == 1 or len(month_input) == 2:
            month = month_input
        else:
            print("Invalid Month, Please Input Again")
            continue

        # Check if day and month are in the valid range
        if int(month) not in range(1, 13) or int(day) not in range(1, 32):
            print("Invalid Format, Please Input Again")
            continue
        # Check the length of day and year
        if len(day) != 1 and len(day) != 2 or (month_input.isdigit() and len(month) != 2 and len(month) != 1) or len(year) != 4:
            print("Invalid Format, Please Input Again")
        # Check to see if a user input 1 digit for day and/or month jf so, add a zero before it
        if len(day) == 1:
            day = "0" + day
        if len(month) == 1:
            month = "0" + month
            print(year + "-" + month + "-" + day)
            break
        else:
            print(year + "-" + month + "-" + day)
            break
    except (IndexError, ValueError):
        print("Invalid Format, Please Input Again")
