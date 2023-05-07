from flask import Flask, render_template, jsonify
from database import engine, load_items_from_db

app = Flask(__name__)

@app.route("/")
def home():
    items = load_items_from_db()
    return render_template('home.html', items=items)

@app.route("/api/items")
def list_items():
    items = load_items_from_db()
    return jsonify(items)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)