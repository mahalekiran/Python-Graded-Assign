#Progam to add json file to DB
from flask import Flask, jsonify
import json
import pymongo
import configparser

configp = configparser.ConfigParser()
app = Flask(__name__)

try:
    #Read config file
    configp.read("sample-config.config")
    #Mongo DB client connection string
    mongoclient=pymongo.MongoClient('mongodb://localhost:27017/')
except Exception as error:
    print("Some error occurred: "+ str(error))
finally:
    print("Read Config File")

@app.route('/')
def index():
    return 'Hello, Flask with MongoDB!'


@app.route('/dbservers',methods=['GET'])
def get_dbservers():
        try:
            # Get Collection object using database name
            db = mongoclient.configMgmt
            coll=db.get_collection('kiranmahale')
            # Define dictionary
            dictValues={}

            # extract specific key-value pairs from the configuration file
            for section in configp.sections():
                keys=[]
                #print(section)
                for keyval in configp.items(section):
                    keys.append(keyval)
                dictValues[section]=keys
                print(dictValues)
            
            # Save dictionary values in json file
            with open('sample-output.json', 'a') as file:
                file.write(json.dumps(dictValues) + '\n')

            # save JSON file in the database.
            with open('sample-output.json') as fileload:
                file_data = json.load(fileload)
            
            if isinstance(file_data, list):
                coll.insert_many(file_data)  
            else:
                coll.insert_one(file_data)

            # Show json data
            return jsonify(dictValues)
        
        except Exception as error:
            print("Error occurred in GET api: "+ str(error))

if __name__ == '__main__':
    app.run()
