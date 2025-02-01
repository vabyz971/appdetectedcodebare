"""
    Main class. Responsible for running the application.
"""
from flask import Flask, render_template

app = Flask(__name__)

def View(page):

    view = page + ".html"
    return render_template(view)


@app.route("/")
def Home():
    return View('home')