from flask import Flask, render_template, jsonify, request
from database import load_quotes_from_db, load_quote_from_db, add_quote_to_db

app = Flask(__name__)


@app.route("/")
def quotable():
    return render_template("home.html")


@app.route("/inspirations.html")
def quotes_repository():
    quotes = load_quotes_from_db()
    return render_template("inspirations.html", quotes=quotes)


@app.route("/api/quotes")
def list_quotes():
    quotes = load_quotes_from_db()
    return jsonify(quotes)


@app.route("/api/quote/<id>")
def show_quote_json(id):
  quote = load_quote_from_db(id)
  return jsonify(quote)


@app.route("/contribute.html")
def contrib():
    return render_template("contribute.html")


@app.route("/newquote/submit", methods=['post'])
def add_to_quote_repo():
  data = request.form
  add_quote_to_db(data)
  return render_template('quote_submitted.html')




if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True)