from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/greet", methods=["POST"])
def greet():
    data = request.get_json()
    name = data.get("name", "")

    message = f"Hello, {name}! Welcome to our team project!"

    return jsonify({
        "message": message
    })


if __name__ == "__main__":
    app.run(debug=True)