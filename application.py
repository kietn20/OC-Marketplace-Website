from flask import Flask, render_template, jsonify
from database import engine, load_items_from_db, load_item_from_db

app = Flask(__name__)

@app.route("/")
def home():
    items = load_items_from_db()
    return render_template('home.html', items=items)

@app.route("/api/items")
def list_items():
    items = load_items_from_db()
    return jsonify(items)

@app.route("/item/<id>")
def show_item(id):
    item = load_item_from_db(id)
    if not item:
        return "Not Found", 404
    return render_template("itempage.html", item=item)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)