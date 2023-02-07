from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1 style='text-align: center; color: blue'>Hello 🙏🤝</h1>" \
           "<img style='border-radius: 50%; display: block; margin: 0 auto' width='500' height='400' " \
           "src='https://media.giphy.com/media/ie8M6ieLofDiqEGiYT/giphy.gif'>"


@app.route("/bye")
def bye():
    return "<h1>Bye 👋</h1>"


@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"hello {name}!, you are {number} years old😉"


if __name__ == "__main__":
    app.run(debug=True)
