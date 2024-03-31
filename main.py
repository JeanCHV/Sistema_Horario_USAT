from flask import Flask, render_template, request, redirect, jsonify
app = Flask(__name__)
from routers.router_main import *

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)