from flask import Flask, request
from flask_restful import Api, Resource
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'prams'
# production api - keep it secret
api = Api(app)

jwt = JWT(app, authenticate, identity)
#JWT creates new endpoint /auth
# we save username and password
# sends to authenticate
# find correct user obj
# then compare 

# /auth endpoint return jwt token
# we can send it to next req
# calls the identity func 
# get userid , that jwt token represents

#2 resources
items = []
# GET /items
class Item(Resource):
    #authenticate before we call get
    # 401 - unauthorized
    # Header - Authorization - JWT paste_JST_TOKEN
    @jwt_required()
    def get(self, name):
        # for item in items:
        #     if item['name'] == name:
        #         return item
        #return {'item': None}, 404

        #USE filter func - 2 paramenters
        # return filter objects
        # used on list func list(filter())
        # next(filter()) -> first item matched
        # no items in db, next can cause errror
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item else 404

    def post(self, name):
        #we need json payload
        # header -> content type -> json
        #look into content and check json type (force=True)
        # silent=True gives none , no error
        # 400 - bad req

        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return {'message': "An item with name '{}' already exists.".format(name)}, 400

        data = request.get_json()
        item = {'name': name , 'price': data['price']}
        items.append(item)
        return item, 201

class ItemList(Resource):
    def get(self):
        return {'items': items}

api.add_resource(Item, '/item/<name>')
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)
# GET /item/<name>
# POST /item/<name>
# DELETE /item/<name>
# PUT /item/<name>

#pip3 install Flask-JWT

# JWT - Json web token - encoding some data
