#!/usr/bin/python3
''' first go at apis '''
from flask import Flask, jsonify
from api.v1.views import app_views
from models import storage
from os import getenv
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()

@app.errorhandler(404)
def page_not_found(e):
    ''' handles page not found error '''
    return jsonify({"error": "Not found"}), 404



if __name__ == '__main__':
    port = getenv('PORT')

    port = '5000' if port is None else port
    app.run(port=port, threaded=True, debug=True)
