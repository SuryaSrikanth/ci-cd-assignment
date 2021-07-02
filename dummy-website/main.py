import os
from flask import Flask, render_template, request, Blueprint, send_from_directory
import firebase_admin
from firebase_admin import credentials
from flask_cors import CORS


if os.environ.get('ENV', '') in ['dev']:
    # Use the application default credentials
    cred = credentials.ApplicationDefault()
    firebase_admin.initialize_app(cred, {
        'projectId': os.environ.get('PROJECT_ID', '')
    })

else:
    # cred = credentials.Certificate('creds/firestore_creds.json')
    cred = credentials.Certificate('../../cred.json')
    firebase_admin.initialize_app(cred)


app = Flask(__name__, static_folder='angular-src/dist/Angular-app')
CORS(app)

angular = Blueprint('angular', __name__,
                    template_folder='angular-src/dist/Angular-app')
app.register_blueprint(angular)

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)