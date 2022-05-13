from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

string_put_args = reqparse.RequestParser()
string_put_args.add_argument("string_to_cut", type=str, help="String is required", required=True)


#creating a Lyft resource, overriding the post method
class Lyft(Resource):
	def post(self):
		args =  string_put_args.parse_args()
		return_json = {"return_string": args['string_to_cut'][2::3]}
		return return_json, 201

api.add_resource(Lyft, "/test")

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000, debug=True)

