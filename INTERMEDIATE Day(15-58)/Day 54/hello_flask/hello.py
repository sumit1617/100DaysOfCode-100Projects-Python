import time

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


# def outer_function():
#     print("outer function")
#
#     def nested_functio():
#         print("inner function")
#
#     return nested_functio()
#
#
# inner_function = outer_function()


# Python Decorators

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)

        # do something before the function
        function()
        # do something after the function

    return wrapper_function


@delay_decorator
def hello():
    print("hello")


@delay_decorator
def name():
    print("sumit")


@delay_decorator
def greeting():
    print("how are you")


