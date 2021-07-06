#!/usr/bin/env python3
import re
from flask import Flask, request, Response
from functools import wraps 
import base64

from werkzeug.datastructures import Headers

app = Flask(__name__)

def check(authorization_header):
    encoded_uname_pass = authorization_header.split()[-1]
    if encoded_uname_pass == base64.b64encode(b'username:password'):
        return True

def auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        authorization_header = request.headers.get('Authorization')
        if authorization_header and check(authorization_header):
            return f(*args, **kwargs)
        else:
            resp = Response()
            resp.headers['WWW-Authenticate'] = 'Basic'
            return resp, 401
        return f(*args, **kwargs)
    return decorated

@app.route('/')
@auth_required
def index():
    return 'Index Page'

@app.route('/page')
def page():
    Headers

@app.route('/otherpage')
@auth_required
def other_page():
    return '<h1>You are on the other page!</h1>'

if __name__ == '__main__':
    app.run(debug=True)
