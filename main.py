from flask import Flask, render_template, request, redirect, jsonify
app = Flask(__name__)

@app.route("/")
@app.route("/login")
def login():
    return render_template("login/login.html")


@app.route("/index")
def index():
    return render_template("dashboard/home.html")

@app.route("/ambientes")
def ambientes():
    return render_template("dashboard/ambientes.html")

@app.route("/cursos")
def cursos():
    return render_template("dashboard/cursos.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)