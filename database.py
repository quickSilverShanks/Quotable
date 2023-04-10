from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(
  db_connection_string, 
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  })


def load_quotes_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from quotes"))
    quotes = []
    for row in result.all():
      jobs.append(dict(row))
    return quotes

def load_quote_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(
      text("SELECT * FROM quotes WHERE id = :val"),
      val=id
    )
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return dict(rows[0])


def add_quote_to_db(data):
  with engine.connect() as conn:
    query = text("INSERT INTO quotes (q_category, quote, q_speaker, q_source) VALUES (:q_category, :quote, :q_speaker, :q_source)")

    conn.execute(query, 
                 q_category=data['q_category'],
                 quote=data['quote'],
                 q_speaker=data['q_speaker'],
                 q_source=data['q_source'])