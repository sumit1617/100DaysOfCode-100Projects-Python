from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Guess a number between 0 and 9</h1>"\
            "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExa2NoNHRoeDBtZ25vcGU1cHplNzFiZDJlYXZxMW9nYmgxbjI5NGpkdiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7aCSPqXE5C6T8tBC/giphy.gif'>"

randomNo = random.randint(0, 9)

@app.route("/<int:num>")
def guess_number(num):
    if randomNo == num:
        return "<h1 style='color:green'>You found me!!!</h1>"\
                "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMWx3emZibm5sbzcwYW40NmFnOTFnbWYyNWR3N25idWhrZzcwMWNlOCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/4T7e4DmcrP9du/giphy.gif'>"
    elif randomNo < num:
        return "<h1 style='color:red'>Too low, try again!!!</h1>"\
                "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExamNzbDFpcTlrcmd0OXJsOXJuZ2QwZnluN251enc0YngzeGNwazJzZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/jD4DwBtqPXRXa/giphy-downsized-large.gif'>"
    elif randomNo > num:
        return "<h1 src='color:purple'>Too high, try again!!!</h1>"\
                "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExb2U0bHc4bW01dTdtc295YjBkYmJnb2plamZ2b3IwYjhnOXZlZmYxeSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o6ZtaO9BZHcOjmErm/giphy.gif'>"


if __name__ == "__main__":
    app.run()