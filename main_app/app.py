from flask import Flask, url_for
from main_app import static
app = Flask(__name__, static_url_path=static, static_folder=static)

@app.route('/')
def hello_world():
    file = url_for('static', filename='test.json')
    return 'hello world'+ open(file, 'r').read()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
