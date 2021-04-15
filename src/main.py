from flask import Flask
app = Flask(__name__)

def suma(a, b):
    return a+b

@app.route('/')
def hello_world():
    res = suma(4, 3)
    return 'Hello, World! %s' %(res)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
