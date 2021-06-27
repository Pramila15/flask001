from flask import Flask, jsonify , request
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

stores = [
    {
        'name': 'PD',
        'items': [
            {
                'name': 'My item',
                'price': 16
            }
        ]
    }
]

@app.route('/')
def home():
    return "Stores"

@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})

@app.route('/store/<string:name>')
def get_store(name):
    #iterate over stores
    #if the store name mtches, return it
    #if none match, return an error message
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
        
    return jsonify({'message': 'store not found'})

@app.route('/store/<string:name>/item')
def get_items_in_stores(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
        
    return jsonify({'message': 'store not found'})

@app.route('/store',methods=['POST'])
def create_store():
    #request made to /store
    #create new store dictionary
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

@app.route('/store/<string:name>/item',methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    
    return jsonify({'message': 'store not found'})

app.run(port=5000)
