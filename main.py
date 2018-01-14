from flask import Flask, render_template, abort
from werkzeug import secure_filename
import sqlite3
import markdown
import os


app = Flask(__name__, static_url_path='')
base = "base.db"
conn = sqlite3.connect(base)
conn.row_factory = sqlite3.Row


@app.route("/")
def index():
    return render_template("index.html", title="Главная")


@app.route("/shenka/")
def db():
    result = conn.execute("select * from Measuring;")
    return render_template("db.html", title="Измерители толщины", result=result)


@app.route("/blog/<int:year>/<int:month>/<int:day>/<title>")
def blog(year, month, day, title):
    # написать нормальный код для загрузки файла
    fname = 'blog/' + secure_filename('{:04d}-{:02d}-{:02d}-{}.md'.format(year, month, day, title))
    if not os.path.exists(fname):
        abort(404)
    return markdown.markdown(open(fname).read())


if __name__ == "__main__":
    app.run(host="0.0.0.0")
