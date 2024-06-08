from flask import Flask
app = Flask(__name__)
app.debug = False
app.secret_key = 'super-secret'
app.config['UPLOAD_FOLDER'] = 'static/img'
from routers.router_main import *

if __name__ == "__main__":
    app.run( debug=True)
    