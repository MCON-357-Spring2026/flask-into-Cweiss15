from flask import Flask, jsonify, request

app = Flask(__name__)
@app.route('/', methods=['GET'])
def welcome():
    return "<h1>Welcome to My Flask API!</h1>"

@app.route('/about', methods=['GET'])
def about():
    return jsonify({"name": "Chana", "course": "Practicum", "Semester": "Spring 2026"})

@app.route('/greet/chana', methods=['GET'])
def greet():
    return "<h1>Hi Chana! Welcome to Flask!</h1>"

@app.route('/calculate', methods=['GET'])
def calculate():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    operation = request.args.get('operation')
    if operation == "add":
        return jsonify({"result": num1 + num2, "operation": "add"})
    elif operation == "subtract":
        return jsonify({"result": num1 - num2, "operation": "subtract"})
    elif operation == "multiply":
        return jsonify({"result": num1 * num2, "operation": "multiply"})
    elif operation == "divide":
        return jsonify({"result": num1 / num2, "operation": "divide"})

@app.route('/echo', methods=['POST'])
def echo():
    message = request.get_json()

    return jsonify({"message": message, "echoed": True})

@app.route('/status/<int:code>', methods=['GET'])
def status_not_found(code):
    if code == 200:
        return ("OK", 200)
    if code==400:
        return ("Bad Request", 400)
    else:
        return ("Server error", 500)

if __name__ == "__main__":
    app.run(debug=True)