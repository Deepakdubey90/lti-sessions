from flask import Flask


app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return 'Hola !!'


@app.route('/health', methods=['GET'])
def health():
    return 'I am good'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
