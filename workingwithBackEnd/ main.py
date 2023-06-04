# pip install Flask-PyMongo
# pip install Flask
# pip install dnspython 
# npm install -g --force nodemon
# pip install flask-cors

# Import the Flask module that has been installed.
from flask import Flask, send_file, jsonify, request
from flask_pymongo import PyMongo
from flask_cors import CORS

# Creating a new "app" by using the Flask constructor. Passes __name__ as a parameter.
app = Flask(__name__)

# Annotation that allows the function to be hit at the specific URL.
@app.route("/")
# Generic Python functino that returns "Hello world!"
def Hp():
    return "Hello world!"
    
    
# Annotation that allows the function to be hit at the specific URL.
# @app.route("/")
# Generic Python functino that returns "Hello world!"
# def Hp():
#     return books()


# Annotation that allows the function to be hit at the specific URL (/books).
@app.route("/books")
# Generic Python functino that returns books.json
def books():
    return send_file('/workspace/Angular_Maps/workingwithBackEnd/data/books.json')
















# Checks to see if the name of the package is the run as the main package.
if __name__ == "__main__":
    # Runs the Flask application only if the main.py file is being run.
    app.run()