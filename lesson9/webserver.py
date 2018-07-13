from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/get-result/', methods=['GET'])
def result():
    return render_template('result.html')

@app.route('/get-result-json/', methods=['GET'])
def result_js():
    data = [("Вася", "30", "$ 7 830",), ("Маша", "23", "$ 4 830",), ("Петя", "5", "$ 210",)]
    return jsonify(sales=data)


if __name__ == "__main__":
    app.run(debug=True)