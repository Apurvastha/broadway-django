import requests
import json

# fetch data from the API
response = requests.get("https://www.onlinekhabar.com/smtm/home/trending")
# parse into json
if response.status_code == 200:
    data = response.json()
    print(data)
    response_data = data["response"]

    # format the data
    formatted_data = []

    for item in response_data:
        formatted_data.append(
            f"Ticker: {item['ticker']}\n"
            f"Ticker Name: {item['ticker_name']}\n"
            f"Latest Price: {item['latest_price']}\n"
            f"Points Change: {item['points_change']}\n"
            f"Percentage Change: {item['percentage_change']}\n"
            f"Traded of Market Cap: {item['traded_of_mkt_cap']}\n"
            "--------------------------------------------\n"
        )
    # store the data in a txt file   
    with open("trending.txt", "w") as file:
        file.writelines(formatted_data)
        
    print("Data has been stored in a trending.txt file")

else:
    print(f"Failed to fetch data. Status code: {status_code}")
