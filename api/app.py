import json

from flask import Flask, request, make_response
from functools import wraps
import sqlite3 as sql
from sqlite3.dbapi2 import connect
from flask_restful import Resource, reqparse

app = Flask(__name__)

def auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if auth and auth.username == 'username' and auth.password == 'password':
            return f(*args, **kwargs)

        return make_response('Could not verify your login!', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})

    return decorated

@app.route('/')
def index():
    if request.authorization and request.authorization.username == 'username' and request.authorization.password == 'password':
        return '<h1>Rising Ahead Demo API</h1>'

    return make_response('Could not verify!', 401, {'WWW-Authenticate' : 'Basic realm="Login Required"'})

@app.route('/allproducts')
@auth_required
def get_all_products():
    connection = sql.connect('database.db')
    cursor = connection.cursor()

    query = "SELECT * FROM products"
    result = cursor.execute(query)
    products = []

    for row in result:
        products.append({
            'behavior': row[0],
            'trend': row[1],
            'product_name': row[2],
            'business_purpose': row[3],
            'short_des': row[4],
            'long_des': row[5],
            'function': row[6],
            'strategy': row[7],
            'business_impact': row[8],
            'enterprise_value': row[9],
            'feature_attribute': row[10],
            'report_embed_code': row[11]
        })


    connection.close()

    return {'products': products}

@app.route('/product',methods= ['POST'])
@auth_required
def add_product():
    data = request.get_json()
    prod = {
        'behavior': data['behavior'],
        'trend': data['trend'],
        'product_name': data['product_name'],
        'business_purpose': data['business_purpose'],
        'short_des': data['short_des'],
        'long_des': data['long_des'],
        'function': data['function'],
        'strategy': data['strategy'],
        'business_impact': data['business_impact'],
        'enterprise_value': data['enterprise_value'],
        'feature_attribute': data['feature_attribute'],
        'report_embed_code': data['report_embed_code']
    }

    connection = sql.connect('database.db')
    cursor = connection.cursor()

    query = "INSERT INTO products VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    cursor.execute(query, (
        prod['behavior'],
        prod['trend'],
        prod['product_name'],
        prod['business_purpose'],
        prod['short_des'],
        prod['long_des'],
        prod['function'],
        prod['strategy'],
        prod['business_impact'],
        prod['enterprise_value'],
        prod['feature_attribute'],
        prod['report_embed_code']
    ))

    connection.commit()
    connection.close()

    return {'prod': prod}

@app.route('/product/<string:product_name>',methods= ['GET'])
@auth_required
def get_product(product_name):
    connection = sql.connect('database.db')
    cursor = connection.cursor()

    query = "SELECT * FROM products WHERE product_name=?"
    result = cursor.execute(query, (product_name,))
    row = result.fetchone()
    connection.close()

    if row:
        return {'behavior': row[0],
            'trend': row[1],
            'product_name': row[2],
            'business_purpose': row[3],
            'short_des': row[4],
            'long_des': row[5],
            'function': row[6],
            'strategy': row[7],
            'business_impact': row[8],
            'enterprise_value': row[9],
            'feature_attribute': row[10],
            'report_embed_code': row[11]}

    return {'message': 'Item not found'}, 404

if __name__ == '__main__':
    app.run(debug=True)