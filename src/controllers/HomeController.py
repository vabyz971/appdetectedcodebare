from core.Controller import Controller
from tkinter import messagebox
from PIL import Image
from pyzbar.pyzbar import decode

"""
    Main controller. It will be responsible for program's main screen behavior.
"""


class HomeController(Controller):
    # -----------------------------------------------------------------------
    #        Constructor
    # -----------------------------------------------------------------------
    def __init__(self):
        self.homeView = self.loadView("Home")

    # -----------------------------------------------------------------------
    #        Methods
    # -----------------------------------------------------------------------
    
    
    def detectedCode(self, imagePath):
        try:
            with Image.open(imagePath) as img:
                for code in decode(img):
                    code_data = code.data.decode("utf-8")
                    self.homeView._add_table(code_data)
            return True
        except OSError:
            messagebox.showinfo("Erreur", "Vous devez selectioner une image")
            return False
        pass
    
    """
        @Override
    """

    def main(self):
        self.homeView.main()