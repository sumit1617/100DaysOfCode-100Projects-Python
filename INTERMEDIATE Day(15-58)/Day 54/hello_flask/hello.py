from flask import Flask

app = Flask(__name__)

def make_bold(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<b>{result}</b>"
    return wrapper

def make_italic(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<em>{result}</em>"
    return wrapper

def make_underline(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<u>{result}</u>"
    return wrapper

@app.route("/")
@make_bold
@make_italic
@make_underline
def hello_world():
    return "Hello, World!"
    
@app.route("/bye")
def say_bye():
    return "<h1>Bye👋</h1>"

@app.route("/<name>/<int:number>")
def greet(name, number):
    return f"<h1>Hello, {name}, you are {number} years old</h1>"\
    "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExY3BpbDY5YmU2YTFkd2ZiNWl2c21pZHlrMTVsbGN3NXlvYTRmanJ4eCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/FO9C6FIPur9XKgFDon/giphy.gif'>"


if __name__ == "main":
    app.run() 