#!/usr/bin/env python3
# 2.7 direct string comaprison could be done using 
#from werkzeug.security import safe_str_cmp

from models.user import UserModel
# in mem table of registered table
# users = [
#     {
#         'id': 1,
#         'username': 'bob',
#         'password': 'abcd'
#     }
# ]

#users = [UserModel(1, 'bob', 'abcd')]

# index on bob and id
# username_mapping key bob with following values
# userid mapping key id with following values

# username_mapping = {
#     'bob': {
#         'id': 1,
#         'username': 'bob',
#         'password': 'abcd'
#     }
# }

# userid_mapping = {
#     'id': {
#         'id': 1,
#         'username': 'bob',
#         'password': 'abcd'
#     }
# }

# username_mapping = {u.username: u for u in users}
# userid_mapping = {u.id: u for u in users}

# find user by username
def authenticate(username, password):
    #user = username_mapping.get(username, None)
    user = UserModel.find_by_username(username)
    if user and user.password == password:
        return user

#takes payload
def identity(payload):
    user_id = payload['identity']
    #return userid_mapping.get(user_id, None)
    return UserModel.find_by_id(user_id)