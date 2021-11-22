from flask import Flask, request
from flask_restful import Api, Resource, fields, marshal_with, reqparse, abort
from models import *

parser = reqparse.RequestParser()
parser.add_argument('name', type = str, help = "Name should be a string", required = True)
parser.add_argument('pin', type = int, help= "Pin should be a Integer.")
parser.add_argument('country', type = str, help = "Country should be a string.")


api = Api(app)

resource_fields = {
	'id': fields.Integer,
	'name' : fields.String,
	'pin' : fields.Integer,
	'country' : fields.String
}


# class User:
# 	def __init__(self, name,  pin, country):
# 		self.name = name
# 		self.pin = pin
# 		self.country = country

class FirstResource(Resource):
	@marshal_with(resource_fields)
	def get(self, id):
		person = User.query.filter_by(id=id).first()
		if person is None:
			abort(404, message= "The User not found.")
		return person

	@marshal_with(resource_fields)
	def put(self, id):
		data = parser.parse_args()
		person = User.query.filter_by(id=id)
		if not person.first():
			abort(404, message="User does not exist.")

		person.update(data)
		db.session.commit()
		return person.first()

	def delete(self, id):
		person = User.query.filter_by(id=id).first()
		if not person:
			abort(404, message = "Could not found the user.")
		db.session.delete(person)
		db.session.commit()

		return "User successfully deleted."

class UserPost(Resource):
	@marshal_with(resource_fields)
	def post(self):
		data = parser.parse_args()
		pers1 = User.query.filter_by(pin = data['pin']).first()
		if pers1:
			abort(409, message = "Pin already exist.")

		person = User(name = data['name'], country = data['country'], pin = data['pin'])
		db.session.add(person)
		db.session.commit()
		return person 

api.add_resource(FirstResource, "/api/<int:id>")
api.add_resource(UserPost, "/api/" )

if __name__ == "__main__":
	app.run(debug=True)
