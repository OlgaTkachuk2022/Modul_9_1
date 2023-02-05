import requests

SEPARATOR = ';'


def create_rates():
    response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
    data = response.json()

    rates: list[dict] = data[0]['rates']

    col_names = ['currency', 'code', 'bid', 'ask']

    csv_result = SEPARATOR.join(col_names) + '\n'
    for rate in rates:
        csv_result += SEPARATOR.join([str(value) for value in rate.values()]) + '\n'

    with open('result.csv', 'w') as f:
        f.write(csv_result)


if __name__ == '__main__':
    create_rates()
