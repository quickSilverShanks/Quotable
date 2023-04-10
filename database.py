from sqlalchemy import create_engine, text
# import os

# db_connection_string = os.environ['DB_CONNECTION_STRING_NEW']
db_connection_string = "mysql+pymysql://tmw9ywwhd4t5vj5t83mv:pscale_pw_gvfp7OzoUCkM1MdZTKZ682ioUCsmTUOhoKTXpD7DvsT@aws.connect.psdb.cloud/quotable?charset=utf8mb4"

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
      # dict(row) no longer works in new version of sqlalchemy
      # quotes.append(dict(row))
      quotes.append(row._mapping)
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