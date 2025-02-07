from PIL import Image
from pyzbar.pyzbar import decode
from flask.views import View
from flask import render_template

"""
    Main controller. It will be responsible for program's main screen behavior.
"""


class HomeController(View):
    def dispatch_request(self):
        items = {
            "title": "Home",
            "header": False
        }
        return render_template("home.html", context=items)