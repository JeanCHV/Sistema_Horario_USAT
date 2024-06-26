from main import app
from flask import request, session, redirect, url_for,render_template


@app.errorhandler(404)
def page_not_found(e):
    # Aquí puedes redirigir al usuario al index.html o renderizar directamente esa plantilla
    return redirect(url_for('index'))

