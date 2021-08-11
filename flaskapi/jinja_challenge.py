#!/usr/bin/python3
from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

groups = [{"hostname": "hostA","ip": "192.168.30.22", "fqdn": "hostA.localdomain"},
          {"hostname": "hostB", "ip": "192.168.30.33", "fqdn": "hostB.localdomain"},
          {"hostname": "hostC", "ip": "192.168.30.44", "fqdn": "hostC.localdomain"}]

# pull in the value of score as an int
@app.route("/", methods = ["POST", "GET"])
def hello_name():
    # render the template with the value of score for marks
    # marks is a jinja var in the template
    return render_template("jinja_challenge.html", arr = groups)

@app.route("/add", methods = ["POST", "GET"])
def add_host():
    if request.method == "POST":
        hostname = request.form.get("hostname")# grab the value of nm from the POST
        ip = request.form.get("ip")# grab the value of nm from the POST
        fqdn = request.form.get("fqdn")# grab the value of nm from the POST

        groups.append({"hostname": hostname, "ip": ip, "fqdn": fqdn})
    return render_template("jinja_challenge.html", arr = groups)
if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224)

