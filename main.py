from flask import Flask
import datetime
app = Flask(__name__)
app.debug = False
app.secret_key = 'super-secret'
app.config['UPLOAD_FOLDER'] = 'static/img'
app.permanent_session_lifetime = datetime.timedelta(minutes=1)
from routers.router_main import *
from routers.router_horario import *

if __name__ == "__main__":
    app.run( debug=True)