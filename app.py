from flask import Flask , jsonify
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
    return "Hello World"

@app.route('/store',methods=['POST'])
def create_store():
    pass

@app.route('/store/<string:name>')
def get_store(name):
    pass

@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})

@app.route('/store/<string:name>',methods=['POST'])
def get_items_in_stores():
    pass

app.run(port=5000)
