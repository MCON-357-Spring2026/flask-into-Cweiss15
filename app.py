from flask import Flask, jsonify, request
from flask import request
app = Flask(__name__)

@app.before_request
def before_request():
    print(f"Request method: {request.method}; Request path: {request.path}")

@app.after_request
def after_request(response):
    response.headers["X-Custom-Header"] = "FlaskRocks"
    return response

@app.teardown_request
def teardown_request(exception):
    if exception:
        print("Exception thrown: ", exception)

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
    try:
        if operation == "add":
            return jsonify({"result": num1 + num2, "operation": "add"})
        elif operation == "subtract":
            return jsonify({"result": num1 - num2, "operation": "subtract"})
        elif operation == "multiply":
            return jsonify({"result": num1 * num2, "operation": "multiply"})
        elif operation == "divide":
            return jsonify({"result": num1 / num2, "operation": "divide"})
        else:
            return jsonify({"error": "Invalid operation"}), 400
    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify({"error": "Error occurred during calculation"}), 500

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

@app.route('/debug/routes')
def show_routes():
    routes = []
    for rule in app.url_map.iter_rules():
        routes.append({
            'endpoint': rule.endpoint,
            'methods': list(rule.methods),
            'path': str(rule)
        })
    return jsonify(routes)

if __name__ == "__main__":
    app.run(debug=True)

