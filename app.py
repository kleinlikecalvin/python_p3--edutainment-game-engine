from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/flashcards")
def flashcards():
    return render_template("flashcards/flashcards.html")


@app.route("/collection")
def collection():
    return render_template("flashcards/collection.html")


@app.route("/create_deck")
def create_deck():
    return render_template("flashcards/create_deck.html")


if __name__ == "__main__":
    app.run(debug=True)
