from flask import Flask
import sqlite3
import os
app = Flask(__name__)

@app.route("/")
def hello():
    return "Дратути!"

@app.route("/db/")
def db():
    base = "app/base.db"
    conn = sqlite3.connect(base)
    conn.row_factory = sqlite3.Row
    result = conn.execute("select * from Measuring;")
    return "good"

    r_string = "<br/>".join("""
        id: {0[id]}
        name: {0[name]}
        measuring: {0[typeMeasuring]}
        type: {0[typeMeasure]}
        {0[upperRange]} {0[upperRange_unit]}
        {0[lowerRange]} {0[lowerRange_unit]}
        {0[accuracy]} {0[accuracy_unit]}
        realTimeMode: {0[realTimeMode]}
        probeUsage: {0[probeUsage]}""".format(row) for row in result)
    return r_string

if __name__ == "__main__":
    app.run(host="0.0.0.0")

