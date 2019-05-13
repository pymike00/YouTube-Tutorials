import requests

def get_json(endpoint):
    response = requests.get(endpoint)

    if response.ok:
        json_data = response.json()
        return json_data
    else:
        print("Status Code: ", response.status_code)
        print("Response Content: ", response.content)
        raise Exception("C'è stato un errore...")

def show_rates(data, currency):
    print("JSON data: ", data)
    rate_date = data["date"]
    exchange_rate = data["rates"][currency]
    print(f"1 EUR corrisponde a { exchange_rate } { currency } il giorno { rate_date }")


if __name__ == "__main__":
    endpoint = "https://api.exchangeratesapi.io/latest"
    data = get_json(endpoint)
    show_rates(data, "SEK")