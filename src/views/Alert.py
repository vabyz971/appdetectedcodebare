import customtkinter as ctk

class AlertView(ctk.CTkToplevel):
    def __init__(self,text):
        super().__init__()
        self.geometry("400x250")
        self.label = ctk.CTkLabel(self, text=text, font=("",18), text_color="red")
        self.label.pack(expand = True)