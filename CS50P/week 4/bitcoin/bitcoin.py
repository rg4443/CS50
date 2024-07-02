import sys
import requests

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url)
data = response.json()

try:
    # Remove commas from the USD rate string and then convert to float
    usd_rate = float(data["bpi"]["USD"]["rate"].replace(",", ""))
except ValueError:
    print("Unable to convert USD rate to float.")
    sys.exit(1)

if len(sys.argv) != 2:
    print("Please input two cmd arguments")
    sys.exit(1)
else:
    input_value = sys.argv[1]
    try:
        input_value = float(input_value)
        multiplied = usd_rate * input_value
        print(f"${multiplied:,.4f}")
    except ValueError:
        print("Not a valid float. Please input a valid number.")
        sys.exit(1)
    except requests.RequestException:
        print("Unable to get data, input a valid number.")
        sys.exit(1)
