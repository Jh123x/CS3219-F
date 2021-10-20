import sqlite3
from flask import Flask, jsonify



app = Flask(__name__)

cache = None
DB_PATH = "server/data/test.db"


@app.route('/', methods=["GET"])
def route_factorize():
    global cache
    if cache is not None:
        return cache
    with sqlite3.connect(DB_PATH) as db:
        cur = db.cursor()
        cur.execute("SELECT * FROM data d1 CROSS JOIN data d2 limit 40000")
        result = []
        for row in cur.fetchall():
            result.append(row)
    cache = jsonify(result)
    return cache


if __name__ == "__main__":
    app.run(debug=True)
