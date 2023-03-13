from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"{brand} - made in {year}"

@app.route('/')
def index():
    return "Hello!"