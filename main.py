from flask import Flask, render_template
import sqlite3


app = Flask(__name__, static_url_path='')
base = "base.db"
conn = sqlite3.connect(base)
conn.row_factory = sqlite3.Row


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/shenka/")
def db():
    result = conn.execute("select * from Measuring;")
    return render_template("db.html", result=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
