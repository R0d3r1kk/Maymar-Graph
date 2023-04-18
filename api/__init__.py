import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import urllib

# Creating a new "app" by using the Flask constructor. Passes __name__ as a parameter.
app = Flask(__name__)
# Configuring a database for the Flask application defined above.
#app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.getcwd()}/marymar.db"
sqlconnection = urllib.parse.quote_plus('DRIVER={SQL Server};Server=P4ND0R4;Database=miramar;Trusted_Connection=True')
app.config["SQLALCHEMY_DATABASE_URI"] = "mssql+pyodbc:///?odbc_connect=%s" % sqlconnection
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# Annotation that allows for the endpoints / URL to be hit.
@app.route('/')
def hello_world():
	return 'Hello World!'
