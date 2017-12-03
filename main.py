from flask import Flask, render_template
import sqlite3
import sys, os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/shenka/")
def db():
    base = "base.db"
    conn = sqlite3.connect(base)
    conn.row_factory = sqlite3.Row
    result = conn.execute("select * from Measuring;")
    return render_template("db.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0")

