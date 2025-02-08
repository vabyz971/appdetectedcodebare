from PIL import Image
from pyzbar.pyzbar import decode
from flask.views import View
from flask import render_template, request
import json
import os
import uuid
"""
    Main controller. It will be responsible for program's main screen behavior.
"""


class ProcessController(View):

    methods = ["GET", "POST"]

    def process_image(self,img_path):
    
        # Créer un dossier pour les images découpées
        output_dir = "src/static/cropped_images"
        self.delete_files_in_directory(output_dir)
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

    def delete_files_in_directory(self,directory_path):
        try:
            with os.scandir(directory_path) as entries:
                for entry in entries:
                    if entry.is_file():
                        os.unlink(entry.path)
            print("All files deleted successfully.")
        except OSError:
            print("Error occurred while deleting files.")


    def dispatch_request(self):
        if request.method == "POST":
            file = request.files['file']
            if not file:
                context = {
                    "erreur": "Vous devez ajouter un fichier"
                }
                return render_template("home.html", context=context)

            # Vérifier si le fichier est une image
            if not (file.mimetype.startswith('image/') or file.filename.lower().split('.')[-1] in ['png', 'jpg', 'jpeg', 'gif', 'bmp']):
                context = {
                    "erreur": "Seuls les images sont autoriser \n - png, jpg, jpeg, gif, bmp"
                }
                return render_template("home.html", context=context)

            process = self.process_image(file)
            return render_template("list.html", context=json.loads(process))
