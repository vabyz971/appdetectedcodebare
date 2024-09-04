import pyperclip as pc
import customtkinter as ctk
from tkinter import filedialog
from .Alert import AlertView

class HomeView(ctk.CTkFrame):
    def __init__(self, parent ,controller):
        super().__init__(master=parent)
        self.controller = controller
        self.alerte_window = None
        self.grid(column = 0, columnspan= 2, row=0, sticky='nsew')
        self.list_code = []

        ctk.CTkButton(self, text='Open Image', command=self.open_file_dialog, font=("Roboto",16)).pack(fill = 'both', ipady=20, padx=100 ,pady=30)


    def add_table(self, data):
        self.list_code.append(data)
        label_btn_code = ctk.CTkButton(self, text=data,command=lambda: pc.copy(data))
        label_btn_code.pack(fill='both', ipady=5, padx=150, pady=5)

    def open_file_dialog(self):
        path = filedialog.askopenfile().name
        if self.controller.UplodeFile(path):
            print(self.list_code)
        else:
            self.open_alert_view("Se n'est pas une image")

    def open_alert_view(self, text):
        if self.alerte_window is None or not self.alerte_window.winfo_exists():
            self.alerte_window = AlertView(text)  # create window if its None or destroyed
        else:
            self.alerte_window.focus()  # if window exists focus it
