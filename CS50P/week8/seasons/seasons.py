from datetime import datetime, date
import inflect
import sys

def calculate_age_in_minutes(user_date):
    today = datetime.combine(date.today(), datetime.min.time())
    age_in_seconds = (today - user_date).total_seconds()
    age_in_minutes = round(age_in_seconds / 60)
    return age_in_minutes

def convert_to_words(total_minutes):
    p = inflect.engine()
    if total_minutes == 0:
        return "zero minutes"
    else:
        return f"{p.number_to_words(total_minutes).capitalize().replace(" and","")} {'minute' if total_minutes == 1 else 'minutes'}"

def main():
    try:
        user_input = input("Date of Birth (YYYY-MM-DD): ")
        year, month, day = map(int, user_input.split("-"))

        user_date = datetime(year, month, day)
        age_in_minutes = calculate_age_in_minutes(user_date)
        print(convert_to_words(age_in_minutes))
    except ValueError:
        sys.exit(1)

if __name__ == "__main__":
    main()
