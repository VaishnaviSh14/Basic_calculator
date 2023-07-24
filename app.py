from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/Hello2")
def hello_world2():
    return "<h1>Hello, World2!</h1>"

@app.route("/hello1")
def hello_world1():
    return "<h1>Hello, World1!</h1>"

@app.route("/input_url")
def request_input():
    data = request.args.get('x')
    return "This is my input from url {}".format(data)


@app.route("/test")
def test():
    a = 5+6
    return "this is my first function in flask {} ".format(a)

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5001)
