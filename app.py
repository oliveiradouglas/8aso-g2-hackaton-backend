from flask import Flask, jsonify, request
from flask_wtf.csrf import CSRFProtect
from flask_cors import CORS
from db import get_songs
import os 

cors_origins = os.environ.get('CORS_ORIGINS')

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": cors_origins, "send_wildcard": "False"}}) # Compliant
csrf = CSRFProtect(app) 

@app.route('/')
def songs():
    return get_songs()    

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
