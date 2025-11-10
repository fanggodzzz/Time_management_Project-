from flask import Flask
import mysql.connector
from _mysql_connector import Error
import os
from dotenv import load_dotenv


load_dotenv
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)