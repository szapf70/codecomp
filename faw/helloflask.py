from flask import Flask
# curl --noproxy localhost, http://localhost:5000

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)