from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello():
    name = request.args.get('name')
    return f'Hello, {name}!' if name else 'Hello World!<br><br>Hint: add the name parameter to the URL: ?name=YourName'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
