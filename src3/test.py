import os

from flask import Flask
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://elmu:5120045@localhost:5432/mydb'
db = SQLAlchemy(app)

#from sqlalchemy.orm import scoped_session, sessionmaker

#engine = create_engine("postgresql://elmu:5120045@localhost:5432/mydb")
#db = scoped_session(sessionmaker(bind=engine))

def main():
    flights = db.execute("SELECT origin, destination, duration FROM flights").fetchall()
    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.")

if __name__ == "__main__":
    main()
