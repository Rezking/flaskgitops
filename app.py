import os
from flask import Flask
from flask import render_template


app = Flask(__name__)
stage = os.environ["stage"]
name = os.environ["name"]
# print(name)

@app.route("/")
def main():
    return render_template("main.html", name=name, stage=stage)

if __name__ == "__main__":
    app.run("0.0.0.0",5000)