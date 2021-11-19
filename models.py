from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]= "sqlite:///test.db"

db = SQLAlchemy(app)


class User(db.Model):
	id = db.Column(db.Integer, primary_key = True, autoincrement = True)
	name = db.Column(db.String, nullable = False)
	country = db.Column(db.String)
	pin = db.Column(db.Integer, nullable= False)

db.create_all()

user1 = User(name = "narendra", country ="India", pin = 200)
db.session.add(user1)
db.session.commit()