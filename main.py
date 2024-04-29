from flask import Flask
app = Flask(__name__)
app.debug = True
app.secret_key = 'super-secret'
from routers.router_main import *

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)