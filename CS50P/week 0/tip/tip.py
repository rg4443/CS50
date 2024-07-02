def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    #remove $ and return as float
    replace = d.replace ("$","")
    floated = float(replace)
    return floated


def percent_to_float(p):
    #remove % and return as float
    replace = p.replace("%", "")
    floated = float(replace)
    return floated / 100.0

main()
