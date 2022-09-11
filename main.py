from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello():
    ip_user = request.remote_addr
    return f'Hello, the ip is {ip_user}'


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
