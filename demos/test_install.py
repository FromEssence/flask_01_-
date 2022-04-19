from flask import Flask
app = Flask(__name__)

@app.route('/helloworld')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    # app.run(host, port, debug, options)
    app.run(host="0.0.0.0", port=5000)