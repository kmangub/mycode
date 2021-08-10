#!/usr/bin/python3
"""Alta3 APIs and HTML"""

## best practice says don't use commas in imports
# use a single line for each import
from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template

app = Flask(__name__)
## This is where we want to redirect users to
@app.route("/success")
def success():
    return f"Correct!!!"
# This is a landing point for users (a start)
@app.route("/") # user can land at "/"
@app.route("/start") # or user can land at "/start"
def start():
    return render_template("trivia_form.html") # look for templates/trivia_form.html
# This is where trivia_form.html POSTs data to
# A user could also browser (GET) to this location
@app.route("/correct", methods = ["POST", "GET"])
def login():
    # POST would likely come from a user interacting with postmaker.html
    if request.method == "POST":
        if request.form.get("answer"): # if nm was assigned via the POST
            ans = request.form.get("answer").lower() # grab the value of nm from the POST
            if ans == 'squall':
                return redirect(url_for("success", name = ans))
    return redirect("/") # pass back to /success with val for name

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application

