from flask import Flask, render_template, jsonify

app = Flask(__name__)

quotes = [
  {
    'id': 1,
    'q_category': "Book",
    'quote': "Who in the world am I? Ah, that's the great puzzle.",
    'q_speaker': "Lewis Carroll",
    'q_source': "Alice in Wonderland"
  },
  {
    'id': 2,
    'q_category': "Book",
    'quote': "Only a few find the way, some don’t recognize it when they do – some… don’t ever want to.",
    'q_speaker': "Cheshire Cat",
    'q_source': "Alice in Wonderland"
  },
  {
    'id': 3,
    'q_category': "Movie",
    'quote': "Behind this mask there is more than just flesh. Beneath this mask there is an idea... and ideas are bulletproof.",
    'q_speaker': "V",
    'q_source': "V for Vendetta"
  },
  {
    'id': 4,
    'q_category': "Movie",
    'quote': "Equality and freedom are not luxuries to lightly cast aside. Without them, order cannot long endure before approaching depths beyond imagining.",
    'q_speaker': "V",
    'q_source': "V for Vendetta"
  },
  {
    'id': 5,
    'q_category': "Book",
    'quote': "Even the smallest person can change the course of the future.",
    'q_speaker': "Galadriel",
    'q_source': "Lord of the Rings"
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