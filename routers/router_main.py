from flask import Flask, render_template, request, redirect, jsonify
from main import app


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


@app.route("/docentes")
def docentes():
    return render_template("dashboard/docentes.html")

@app.route("/horarios")
def horarios():
    return render_template("dashboard/horarios.html")

