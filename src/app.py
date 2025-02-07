"""
    Main class. Responsible for running the application.
"""

from flask import Flask
from controllers.HomeController import HomeController
from controllers.ProcessController import ProcessController

app = Flask(__name__)

# Router Url
app.add_url_rule("/", view_func=HomeController.as_view("home"))
app.add_url_rule("/upload", view_func=ProcessController.as_view("process"))
