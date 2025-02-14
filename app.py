from flask import Flask
from flask import render_template
#reder_template is a function that takes a template and a dictionary and renders the template with the dictionary


app = Flask(__name__)

companies = ['Microsoft', 'Google', 'Paypal', 'Meta']
jobs = [
    {
        'id' : 1, 'company': 'Microsoft', 'salary': 12000
    },
    {
        'id' : 2, 'company': 'Google', 'salary': 13000
    },
        {
        'id' : 3, 'company': 'Meta', 'salary': 14000
    },
    {
        'id' : 4, 'company': 'Paypal', 'salary': 15000
    },
]
@app.route("/")
def hello():
    return render_template("home.html", name = "Moksh R. Patel", companies = companies, jobs=jobs )


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
