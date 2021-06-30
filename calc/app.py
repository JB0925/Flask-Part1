from flask import Flask, request

from operator import add, sub, mul, truediv


app = Flask(__name__)

OPERATIONS = {
    'add': add,
    'sub': sub,
    'mult': mul,
    'div': truediv
}


@app.route('/add')
def addition():
    a, b = int(request.args.get('a')), int(request.args.get('b'))
    return f'<h1 style="text-align: center">{add(a,b)}</h1>'


@app.route('/sub')
def subtraction():
    a, b = int(request.args.get('a')), int(request.args.get('b'))
    return f'<h1 style="text-align: center">{sub(a,b)}</h1>'


@app.route('/mult')
def multiplication():
    a, b = int(request.args.get('a')), int(request.args.get('b'))
    return f'<h1 style="text-align: center">{mul(a,b)}</h1>'


@app.route('/div')
def division():
    a, b = int(request.args.get('a')), int(request.args.get('b'))
    return f'<h1 style="text-align: center">{truediv(a,b)}</h1>'


@app.route('/math/<operation>')
def math(operation):
    a, b = int(request.args.get('a')), int(request.args.get('b'))
    result = OPERATIONS.get(operation)(a,b)
    return f'<h1 style="text-align: center">{result}</h1>'


if __name__ == '__main__':
    app.run(debug=True)
