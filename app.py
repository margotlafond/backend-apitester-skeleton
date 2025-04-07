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
print(associations_df["type"] == "BDA")
print(associations_df[associations_df['type'] == 'BDA'])  # noqa: E721

## Vous devez ajouter les routes ici :
@app.route("/api/alive", methods=['GET'])
def alive_function():
    response = make_response(jsonify({"message": "Alive"}), 200)
    return response

@app.route("/api/associations", methods=['GET'])
def assos_function():
    response = make_response(jsonify(associations_df["id"].values.tolist()), 200)
    return response

@app.route("/api/associations/<int:id>", methods=['GET'])
def assos_details(id):
    if id >= 1 and id <=4 :
        response = make_response(jsonify(associations_df.loc[id-1, "description"]), 200)
    else:
        response = make_response(jsonify({"error": "Association not found"}), 404)
    return response

@app.route("/api/associations/<int:id>/evenements", methods=['GET'])
def assos_evts(id):
    if id >= 1 and id <=4 :
        response = make_response(jsonify(evenements_df.loc[id-1, "description"]), 200)
    else:
        response = make_response(jsonify({"error": "Association not found"}), 404)
    return response

@app.route("/api/associations/type/<type>", methods=['GET'])
def assos_type(type):
    df_assos = associations_df[associations_df['type'] == type]
    response = make_response(jsonify(df_assos["nom"].tolist()), 200)
    return response


if __name__ == '__main__':
    app.run(debug=False)