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
        self.view = self.loadView("Main")

    # -----------------------------------------------------------------------
    #        Methods
    # -----------------------------------------------------------------------
    
    
    def detectedCode(self, imagePath):
        try:
            tab = []
            with Image.open(imagePath) as img:
                index = 0
                for code in decode(img):
                    index +=1
                    print(code)
                    tab.append(code)
                    
                if index >1 :
                    return tab
                else:
                    return tab
            return True
        except OSError:
            messagebox.showinfo("Erreur", "Vous devez selectioner une image")
            return False
        pass
    
    """
        @Override
    """

    def main(self):
        self.view.main()