from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

#2 resources
items = []
# GET /items
class Item(Resource):
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item
        return {'item': None}, 404

    def post(self, name):
        item = {'name': name , 'price': 16}
        items.append(item)
        return item, 201

api.add_resource(Item, '/item/<name>')

# GET /item/<name>
# POST /item/<name>
# DELETE /item/<name>
# PUT /item/<name>
