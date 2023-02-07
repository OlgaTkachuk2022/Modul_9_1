from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/", methods=["GET" , "POST"])
def index():
    if request.metod == "POST":
        #Get the form data
        num1 = int(request.form["num1"])
        num2 = int(request.form["num2"])

        # Perform the calculation
        result = num1 * num2

        # Render the result pade with the result
        return render_template("result.html", result = result)
    # If it's a GET reguest , render the form
    return render_template("form.html")    

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


if __name__ == "__main__":
    app.run(debug=True)



