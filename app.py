import os
from flask import Flask


app = Flask(__name__)

@app.route("/")
def home():
    return "Big Git Example"

@app.route("/about")
def about():
    return "This is about page"


if __name__ == "__main__":
    port = os.environ.get("PORT", 5000)
    app.run("0.0.0.0", port)