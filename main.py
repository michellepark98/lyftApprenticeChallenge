from flask import Flask
from flask_restful import Api, Resource, reqparse
from requests import request


app = Flask(__name__)
api = Api(app)


video_put_args = reqparse.RequestParser()
video_put_args.add_argument("string_to_cut", type=str, help="String is required", required=True)


#creating a resource
class Lyft(Resource):
	def post(self):
		args =  video_put_args.parse_args()



		return_json = {"return_string": args['string_to_cut'][2::3]}

		return return_json, 201


api.add_resource(Lyft, "/test")

if __name__ == "__main__":
	app.run(port=5000, debug=True)

