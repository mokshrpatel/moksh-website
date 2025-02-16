from flask import Flask
from flask import render_template #reder_template is a function that takes a template and a dictionary and renders the template with the dictionary

from database import load_jobs_from_db  #if we importing something form the antoher python file then that file will be running first.



app = Flask(__name__)


@app.route("/")
def hello():
    jobs = load_jobs_from_db()
    return render_template("home.html", name = "Moksh R. Patel", jobs=jobs )


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
