import requests


class CurrencyConverter:
    def __init__(self):
        self.url = "https://bank.gov.ua/NBUStatService/v1/statist/exchange?valcode=USD&json"
        response = requests.get(self.url)
        data = response.json()
        if isinstance(data, list) and len(data) > 0:
            self.usd_rate = float(data[0]["rate"])
        else:
            self.usd_rate = 41.50
    def convert(self, uah):
        return uah / self.usd_rate
if __name__ == "__main__":
    converter = CurrencyConverter()
    print(f"Поточний курс НБУ: 1 USD = {converter.usd_rate:.2f} UAH")

    uah_amount = float(input("Введіть суму в гривнях (UAH): "))
    usd_result = converter.convert(uah_amount)
    print(f"Результат: {usd_result:.2f} USD")