from flask import Flask, render_template, jsonify

app = Flask(__name__)

ITEMS = [
    {
        'id': 1,
        'name': 'Jucier',
        'location': 'Garden Grove',
        'price':  '$25'
    },
    {
        'id': 2,
        'name': 'Valencia Orange Tree',
        'location': 'Santa Ana',
        'price':  '$29.95'
    },
    {
        'id': 3,
        'name': 'Blood Orange Tree',
        'location': 'Tustin',
        'price':  '$35'
    },
    {
        'id': 4,
        'name': 'Tangerine Tree',
        'location': 'Garden Grove',
    }
]

@app.route("/")
def helloWorld():
    return render_template('home.html', items=ITEMS)

@app.route("/api/items")
def list_items():
    return jsonify(ITEMS)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)