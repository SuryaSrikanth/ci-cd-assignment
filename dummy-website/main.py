from flask import Flask, render_template, send_from_directory, Blueprint
from flask_cors import CORS


app = Flask(__name__, static_folder='angular/dist/angular')
CORS(app)

angular = Blueprint('angular', __name__,
                    template_folder='angular/dist/angular')
app.register_blueprint(angular)

@app.route('/assets/<path:filename>')
def custom_static_for_assets(filename):
    return send_from_directory('angular/dist/angular/assets', filename)


@app.route('/<path:filename>')
def custom_static(filename):
    return send_from_directory('angular/dist/angular/', filename)

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)