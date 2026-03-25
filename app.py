from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    num1 = data.get('num1')
    num2 = data.get('num2')
    operation = data.get('operation')

    try:
        num1 = float(num1)
        num2 = float(num2)
    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid numbers'}), 400

    if operation == 'add':
        result = num1 + num2
        symbol = '+'
    elif operation == 'subtract':
        result = num1 - num2
        symbol = '−'
    elif operation == 'multiply':
        result = num1 * num2
        symbol = '×'
    elif operation == 'divide':
        if num2 == 0:
            return jsonify({'error': 'Cannot divide by zero'}), 400
        result = num1 / num2
        symbol = '÷'
    elif operation == 'modulo':
        if num2 == 0:
            return jsonify({'error': 'Cannot modulo by zero'}), 400
        result = num1 % num2
        symbol = '%'
    elif operation == 'power':
        result = num1 ** num2
        symbol = '^'
    else:
        return jsonify({'error': 'Invalid operation'}), 400

    # Format result nicely
    if result == int(result):
        result_str = str(int(result))
    else:
        result_str = f"{result:.10g}"

    return jsonify({
        'result': result_str,
        'expression': f"{num1:g} {symbol} {num2:g} = {result_str}"
    })

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)  # Set debug=False for production
