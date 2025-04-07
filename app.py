import pathlib as pl

import numpy as np
import pandas as pd

from flask import Flask, jsonify, request, make_response
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

data = pl.Path(__file__).parent.absolute() / 'data'

# Charger les données CSV
associations_df = pd.read_csv(data / 'associations_etudiantes.csv')
evenements_df = pd.read_csv(data / 'evenements_associations.csv')


## Vous devez ajouter les routes ici :
@app.route("/api/alive", methods=['GET'])
def alive_function():
    response = make_response(jsonify({"message": "Alive"}), 200)
    return response

@app.route("/api/associations", methods=['GET'])
def assos_function():
    response = make_response(jsonify(associations_df["nom"].to_dict()), 200)
    return response

if __name__ == '__main__':
    app.run(debug=False)