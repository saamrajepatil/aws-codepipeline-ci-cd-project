from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Devops!'

if __name__ == '__main__':
    app.run()

