from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
import configparser

configp = configparser.ConfigParser()
app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/your_database'
mongo = PyMongo(app)

@app.route('/')
def index():
    return 'Hello, Flask with MongoDB!'

@app.route('/users', methods=['GET'])
def get_users():
    users = mongo.db.users.find()
    result = []
    for user in users:
        result.append({'username': user['username'], 'email': user['email']})
    return jsonify(result)

if __name__ == '__main__':
    app.run()

# try:
#     configp.read("sample-config.config")

#     for section in configp.sections():
#         dictValues={}
#         keys=[]
#         #print(section)
#         for keyval in configp.items(section):
#             keys.append(keyval)
#         dictValues[section]=keys
#         print(dictValues)
# except:
#     print("Some error occurred")
# finally:
#     print("Clear")