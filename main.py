from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


def extract_data():
    return ["ala", "bala", "portocala"]


@app.route("/")
def index():
    data = extract_data()

    if request.is_json:
        return jsonify(data)

    return render_template("index.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)