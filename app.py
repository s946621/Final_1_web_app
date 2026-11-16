# Before running, make sure to run in the terminal:
# pip install flask

from flask import Flask, request, redirect, url_for, render_template, session, jsonify
from database import get_db

app = Flask(__name__)
app.secret_key = "supersecretkey"

# ---------- ROUTES ----------
@app.route("/", methods=["GET"])
def login():
    error = "Hello World"

    return render_template("placeholder.html", error=error)

# ---------- RUN ----------
if __name__ == "__main__":
    app.run(debug=True)