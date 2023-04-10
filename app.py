from flask import Flask, render_template, jsonify

app = Flask(__name__)

quotes = [
  {
    'id': 1,
    'quote_cat': "Book",
    'quote': "Who in the world am I? Ah, that's the great puzzle.",
    'character': "Lewis Carroll",
    'source': "Alice in Wonderland"
  },
  {
    'id': 2,
    'quote_cat': "Book",
    'quote': "Only a few find the way, some don’t recognize it when they do – some… don’t ever want to.",
    'character': "Cheshire Cat",
    'source': "Alice in Wonderland"
  },
  {
    'id': 3,
    'quote_cat': "Movie",
    'quote': "Behind this mask there is more than just flesh. Beneath this mask there is an idea... and ideas are bulletproof.",
    'character': "V",
    'source': "V for Vendetta"
  },
  {
    'id': 4,
    'quote_cat': "Movie",
    'quote': "Equality and freedom are not luxuries to lightly cast aside. Without them, order cannot long endure before approaching depths beyond imagining.",
    'character': "V",
    'source': "V for Vendetta"
  },
  {
    'id': 5,
    'quote_cat': "Book",
    'quote': "Even the smallest person can change the course of the future.",
    'character': "Galadriel",
    'source': "Lord of the Rings"
  }
]

@app.route("/")
def quotable():
    return render_template("home.html")

@app.route("/inspirations.html")
def quotes_repository():
    return render_template("inspirations.html", quotes=quotes)

@app.route("/api/quotes")
def list_quotes():
    return jsonify(quotes)


if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True)