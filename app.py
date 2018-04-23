from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/foo/')
def foo():
    return 'The foo page'

@app.route('/bar')
def bar():
    return 'The bar page'

@app.route('/hello/')
@app.route('/hello/<name>')
def say_hello(name=None):
    return render_template('hello.html', name=name)
