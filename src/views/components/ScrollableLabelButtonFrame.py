import customtkinter as ctk
import tkinter as ttk
import pyperclip as pc
from tkinter import messagebox
from config import FONT_STYLE


class ScrollableLabelButtonFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure((0, 1), weight=1)
        self.values = []

    def add_value(self, value):
        self.remove_items()
        self.values.append(value)
        for i, value in enumerate(self.values):
            self.create_items(i, value).pack(expand=True, fill="both", pady=4, padx=10)

    def create_items(self, index, value):
        frame = ctk.CTkFrame(self)
        frame.pack()

        # grid layout
        frame.rowconfigure(0, weight=1)
        frame.columnconfigure((0, 1, 2, 3, 4), weight=1, uniform="a")

        ctk.CTkLabel(frame, text=index, font=FONT_STYLE, width=12).grid(
            row=0, column=0, columnspan=1, padx=12, pady=5
        )
        ctk.CTkLabel(frame, text=f"type:{value.type}", font=FONT_STYLE).grid(
            row=0, column=1, padx=12, pady=5
        )
        ctk.CTkLabel(frame, text=f"{value.data.decode('utf-8')}", font=FONT_STYLE).grid(
            row=0, column=2, padx=12, pady=5
        )
        ctk.CTkLabel(frame, text=f"quality:{value.quality}", font=FONT_STYLE).grid(
            row=0, column=3, padx=12, pady=5
        )
        ctk.CTkButton(
            frame,
            text="Copier",
            font=FONT_STYLE,
            command=lambda: self.notification(value.data.decode("utf-8")),
        ).grid(row=0, column=4, padx=20, pady=5, ipady=20, columnspan=1, stick="ew")

        return frame

    def notification(self, code):
        pc.copy(code)
        messagebox.showinfo("Information", f"code {code} copier")


    def remove_items(self):
        for widget in self.winfo_children():
            widget.destroy()

    def remove_values(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.values = []
