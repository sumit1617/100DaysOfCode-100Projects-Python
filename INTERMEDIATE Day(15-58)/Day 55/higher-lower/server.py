from flask import Flask
import random

app = Flask(__name__)


random_number = random.randint(0, 9)


@app.route("/")
def home():
    return "<h1 style='color: blue'>Guess a Number between 0 to 9 😉😎</h1>" \
           "<img style='border-radius: 50%; display: block; margin: 0 auto' width='500' height='400' " \
           "src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"


@app.route("/<int:number>")
def guess(number):
    if random_number == number:
        return "<h1 style='color: green'>Bilkul Sahi Jawab 🥳👏😂</h1>" \
                "<img style='display: inline;' width='500' height='400' " \
                "src='https://media.giphy.com/media/5LjdaiYVzl27bGhHhe/giphy.gif'>" \
                "<div style='display:inline;width:5px;'></div>"\
                "<img style='display: inline' width='500' height='400' " \
                "src='https://media.giphy.com/media/L6bZ1hgv5orHODdsYi/giphy.gif'>"

    elif random_number > number:
        return "<h1 style='color: red'>Naa Wapis Bol It's too neeche 😂👇😞</h1>" \
                "<img style='display: block; margin: 0 auto' width='500' height='400' " \
                "src='https://media.giphy.com/media/IevhwxTcTgNlaaim73/giphy.gif'>"

    elif random_number < number:
        return "<h1 style='color: yellow'>Wapis bol bhaut Upar Chala gya tu 😂☝😭</h1>" \
                "<img style='display: block; margin: 0 auto' width='500' height='400' " \
                "src='https://media.giphy.com/media/qziHvgtMviofnyiTXu/giphy.gif'>"


if __name__ == "__main__":
    app.run(debug=True)