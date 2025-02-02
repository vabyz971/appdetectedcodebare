"""
    Main class. Responsible for running the application.
"""
import json
import os
import uuid
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
        codes = process_image(f)
        return render_template('list.html', context=json.loads(codes))


def process_image(img_path):

    # Créer un dossier pour les images découpées
    output_dir = "src/static/cropped_images"
    delete_files_in_directory(output_dir)
    os.makedirs(output_dir, exist_ok=True)

    results = []
    unique_id = str(uuid.uuid4())[:8]  # Pour éviter les collisions de noms


    decoded_data = []

    with Image.open(img_path) as img:
        original_width, original_height = img.size

        
        for index, code in enumerate(decode(img), 1):

            # Découper l'image selon les coordonnées du code
            rect = code.rect
            cropped = img.crop((
                max(0, rect.left - 10), 
                max(0, rect.top - 10),
                min(original_width, rect.left + rect.width + 10),
                min(original_height, rect.top + rect.height + 100)
            ))

            # Sauvegarder l'image découpée
            cropped_filename = f"{unique_id}_code_{index}.webp"
            cropped_path = os.path.join(output_dir, cropped_filename)
            cropped.save(cropped_path, "WEBP", quality=100)

            # Transformer chaque objet Decoded en dictionnaire
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
                },
                "image": f"/static/cropped_images/{cropped_filename}"
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



def delete_files_in_directory(directory_path):
    try:
     with os.scandir(directory_path) as entries:
       for entry in entries:
         if entry.is_file():
            os.unlink(entry.path)
     print("All files deleted successfully.")
    except OSError:
     print("Error occurred while deleting files.")