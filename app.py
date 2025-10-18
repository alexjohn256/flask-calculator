from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compute', methods=['POST'])
def compute():
    data = request.get_json() or {}
    a = data.get('a', '')
    b = data.get('b', '')
    op = data.get('op', '')
    try:
        # convert to float or int where appropriate
        x = float(a)
        y = float(b)
    except Exception as e:
        return jsonify({'error': 'Invalid number input.'}), 400

    try:
        if op == '+':
            res = x + y
        elif op == '-':
            res = x - y
        elif op == '*':
            res = x * y
        elif op == '/':
            if y == 0:
                return jsonify({'error': 'Division by zero.'}), 400
            res = x / y
        else:
            return jsonify({'error': 'Unknown operation.'}), 400

        # if result is integer-like, return as int
        if abs(res - int(res)) < 1e-9:
            res = int(res)
        return jsonify({'result': res})
    except Exception as e:
        return jsonify({'error': 'Computation error.'}), 500

# if __name__ == '__main__':
#     # debug mode for development; in production use a proper WSGI server
#     app.run(host='0.0.0.0', port=5000, debug=True)
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
