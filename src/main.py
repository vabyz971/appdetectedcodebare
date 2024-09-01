import customtkinter as ctk
from Views.Home import HomeView
from Controllers.Home import HomeController
class App(ctk.CTk):
    def __init__(self):
        
        #setup
        super().__init__()
        ctk.set_appearance_mode("System") 
        self.title("Detecteur codebare")
        self.geometry("600x200")
        self.minsize(600,400)

        #layout
        self.rowconfigure(0, weight = 1)
        self.columnconfigure(0, weight = 2, uniform = "a")
        self.columnconfigure(1, weight = 6, uniform = "a")
        
        #page
        self.view = HomeView(self, None)
        
        #controller
        self.controller = HomeController(self.view)
        self.view.controller = self.controller

        #run
        self.mainloop()

App()

