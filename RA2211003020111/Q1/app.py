from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate-average', methods=['POST'])
def calculate_average():
    data = request.get_json()
    numbers = data.get("numbers", [])
    if not numbers:
        return jsonify({"error": "No numbers provided"}), 400
    average = sum(numbers) / len(numbers)
    return jsonify({"average": average})

if __name__ == '__main__':
    app.run(debug=True)
