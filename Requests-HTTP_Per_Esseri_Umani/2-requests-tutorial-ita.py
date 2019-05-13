import requests

def get_rates(a, b):
    # response = requests.get("https://api.exchangeratesapi.io/latest?base=USD&symbols=CAD")

    payload = {"base": a, "symbols": b}
    response = requests.get("https://api.exchangeratesapi.io/latest", params=payload)

    if response.ok:
        data = response.json()
        print(data)
        rate_date = data["date"]
        exchange_rate = data["rates"][b]
        print(f"1 { a } corrisponde a { exchange_rate } { b } il giorno { rate_date }")
    else:
        print("Status Code: ", response.status_code)
        print("Response Content: ", response.content)
        raise Exception("C'è stato un errore...")


if __name__ == "__main__":
    a = "TRY"
    b = "GBP"
    get_rates(a, b)
