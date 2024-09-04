from PIL import Image
from pyzbar.pyzbar import decode


class HomeController:
    def __init__(self,view):
        self.view = view

    def UplodeFile(self, path):
        try:
            with Image.open(path) as img:
                for code in decode(img):
                    code_data = code.data.decode("utf-8")
                    print(code_data)
                    self.view.add_table(code_data)
                return True
        except OSError:
            return False
