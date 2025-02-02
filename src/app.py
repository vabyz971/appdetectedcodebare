"""
    Main class. Responsible for running the application.
"""
import json
from PIL import Image
from pyzbar.pyzbar import decode
from flask import Flask, render_template , request

app = Flask(__name__)

def View(page):

    view = page + ".html"
    return render_template(view)


@app.route("/")
def Home():
    return View('home')



@app.route("/upload", methods=['GET','POST'])
def upload_file():
    if request.method == "POST":
        f = request.files['file']
        codes = detectedCode(f)
        return render_template('list.html', context=json.loads(codes))


def detectedCode(imageFile):
    decoded_data = []

    with Image.open(imageFile) as img:

        detected_codes = decode(img)

        # Transformer chaque objet Decoded en dictionnaire
        for index, code in enumerate(detected_codes, 1):
            code_entry = {
                "id": index,
                "type": code.type,
                "quality": code.quality,
                "data": code.data.decode('utf-8', errors='replace'),  # Conversion bytes -> str
                "position": {
                    "left": code.rect.left,
                    "top": code.rect.top,
                    "width": code.rect.width,
                    "height": code.rect.height
                }
            }
            decoded_data.append(code_entry)

        # Retourner le résultat formaté en JSON
        return json.dumps(
            {
                "count": len(decoded_data),
                "results": decoded_data
            },
            indent=2,
            ensure_ascii=False
        )
