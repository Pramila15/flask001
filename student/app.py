from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

#api works with resources
#every resource has to be a class
#inherits from class Resource
# stored in database
# in-mem database - list

class Student(Resource):
    def get(self, name):
        return {'student': name}

#we've created student resource 
#gonna be accesible via api
#add the end of resource append path

# no need of jsonify , flask-restful does it for us
# 404 - error
# 201 - created
# 200 - status ok

api.add_resource(Student, '/student/<string:name>')

app.run(port=5000)
