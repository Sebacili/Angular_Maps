# pip install Flask-PyMongo
# pip install Flask
# pip install dnspython 
# npm install -g --force nodemon
# pip install flask-cors



# npm i -g nodemon
# nodemon main.py




# Import the Flask module that has been installed.
from flask import Flask, send_file, jsonify, request
from flask_pymongo import PyMongo
from flask_cors import CORS

app = Flask(__name__)

# Stringa di connessione al DB
app.config["MONGO_URI"] = "mongodb+srv://S3ba26:Facebook2015@cluster0.ztaqymo.mongodb.net/Relab" #Importante qui va specificato il nome del DB --> /Relab

mongo = PyMongo(app)
# Per rispondere alle chiamate cross origin
CORS(app)

# Annotation that allows the function to be hit at the specific URL.
@app.route("/")
# Generic Python function that returns "Hello world!"
def index():
    return "Hello world!"

# Questa route effettua una find() su tutto il DB (si limita ai primi 100 risultati)
@app.route('/addresses', methods=['GET'])
def get_all_addresses():
    mil4326WKT = mongo.db.MilWKT4326
    output = []
    for s in mil4326WKT.find().limit(100):
        output.append({"indirizzo": s['INDIRIZZO'], "tipo" : s['CI_VETTORE']})
    return jsonify({'result': output})



@app.route('/ci_vettore/<foglio>', methods=['GET'])
def get_vettore(foglio):
    mil4326WKT = mongo.db.MilWKT4326
    output = []
    query = {
        "FOGLIO" : int(foglio)
    }
    for s in mil4326WKT.find(query).limit(100):
        output.append({
            "INDIRIZZO":s['INDIRIZZO'],
            "WGS84_X":s["WGS84_X"],
            "WGS84_Y":s["WGS84_Y"],
            "CLASSE_ENE":s["CLASSE_ENE"],
            "EP_H_ND":s["EP_H_ND"],
            "FOGLIO":s["FOGLIO"],
            "CI_VETTORE":s['CI_VETTORE']
            })
    return jsonify(output)




@app.route('/ci_vettore/sezione/<sez>', methods=['GET'])
def sezione(sez):
    mil4326WKT = mongo.db.MilWKT4326
    output = []
    query = {
        "SEZ" : int(sez)
    }
    for s in mil4326WKT.find(query).limit(100):
        output.append({
            "INDIRIZZO":s['INDIRIZZO'],
            "WGS84_X":s["WGS84_X"],
            "WGS84_Y":s["WGS84_Y"],
            "CLASSE_ENE":s["CLASSE_ENE"],
            "EP_H_ND":s["EP_H_ND"],
            "FOGLIO":s["FOGLIO"],
            "CI_VETTORE":s['CI_VETTORE']
            })
    return jsonify(output)






import geojson
import shapely.wkt
# pip install geojson
# pip install shapely



@app.route('/geogeom/<float:lng>/<float:lat>/<float:r>', methods=['GET'])
def get_avg(lng, lat, r):
    print(type(lng))
    mil4326WKT = mongo.db.MilWKT4326
    output = []

    match = {
        '$match': {
            '$and':
            [
                {'EP_H_ND': {'$gt': 0}},
                {'WGS84_X': {'$gt': lng - r}},
                {'WGS84_X': {'$lt': lng + r}},
                {'WGS84_Y': {'$gt': lat - r}},
                {'WGS84_Y': {'$lt': lat + r}}
            ]
        }
    }
    group = {
        '$group': {
            '_id': {
                'SEZ': '$SEZ',
                'WKT': '$WKT'
            },
            'AVG': {
                '$avg': '$EP_H_ND'
            },
            'SUM': {
                '$sum': '$EP_H_ND'
            }
        }
    }
    limit = {
        '$limit': 10
    }

    for s in mil4326WKT.aggregate([match, group, limit]):
        # Converte da WKT in GeoJson Geometry
        g1 = shapely.wkt.loads(s['_id']['WKT'])
        g2 = geojson.Feature(geometry=g1,
                             properties={'id': s['_id']['SEZ'], 'media': s['AVG'], 'somma': s['SUM'], 'sezione': s['_id']['SEZ']})
        output.append(g2)
    return jsonify(geojson.FeatureCollection(output))
































# Checks to see if the name of the package is the run as the main package.
if __name__ == "__main__":
    # Runs the Flask application only if the main.py file is being run.
    app.run()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           