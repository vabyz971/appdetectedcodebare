import customtkinter as ctk
import tkinter as ttk
import cv2
from views.View import View
from .components.ScrollableLabelButtonFrame import ScrollableLabelButtonFrame
import pyperclip as pc
from PIL import Image, ImageTk
from config import APP_SIZE_X, APP_SIZE_Y, APP_TITLE, FONT_STYLE, APP_VERSION


# -----------------------------------------------------------------------
#        Variables
# -----------------------------------------------------------------------

LIST_CODE = []


# -----------------------------------------------------------------------
#        Style
# -----------------------------------------------------------------------


class MainView(ctk.CTk, View):

    # -----------------------------------------------------------------------
    #        Constructor
    # -----------------------------------------------------------------------
    """
    @param controller Controller of this view
    """

    def __init__(self, controller):
        super().__init__()
        self.homeController = controller
        self.minsize(APP_SIZE_X, APP_SIZE_Y)
        self.title(APP_TITLE)

        # top window camera
        self.topcamera_window = None

        """ Frame sidebare left """
        self.frame_sidebare = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.frame_sidebare.pack(side="left", fill="y", ipadx=10)

        """ Frame container """
        self.frame_container = ctk.CTkFrame(self, corner_radius=0)
        self.frame_container.pack(side="left", fill="both", expand=True)

        """Components show list code"""
        # self.list_frame =  ListFrame(self.frame_container, LIST_CODE, 50)
        self.liste_button = ScrollableLabelButtonFrame(
            self.frame_container,
            label_text="Liste des codes",
            label_font=("Roboto", 16),
        )
        self.liste_button.pack(side="left", fill="both", expand=True)

        """titre sidebare"""
        self.label_title_sidebare = ctk.CTkLabel(
            self.frame_sidebare, text="Mode de detection", font=FONT_STYLE
        ).pack(side="top", pady=(15, 5))
        """ bouton pour ajouter une image """
        self.button_add_image_sidebare = ctk.CTkButton(
            self.frame_sidebare,
            width=self.frame_sidebare.winfo_width(),
            font=FONT_STYLE,
            text="Image",
            command=self.add_file,
        ).pack(side="top", pady=5, ipady=12)

        """bare de séparation"""
        self.bare_sidebare = ctk.CTkFrame(
            self.frame_sidebare,
            width=self.frame_sidebare.winfo_width(),
            height=10,
        ).pack(side="top", pady=(5))

        """ bouton reset liste code """
        self.button_remove_list_sidebare = ctk.CTkButton(
            self.frame_sidebare,
            font=FONT_STYLE,
            width=self.frame_sidebare.winfo_width(),
            text="Vider la liste",
            command=self.remove_list,
        ).pack(side="top", pady=5, ipady=5)

        """Label version APP"""
        self.label_app_version_sidebare = ctk.CTkLabel(
            self.frame_sidebare, text=APP_VERSION, font=FONT_STYLE
        ).pack(side="bottom", pady=(5))

    # -----------------------------------------------------------------------
    #        Methods Function
    # -----------------------------------------------------------------------

    def add_file(self):
        file_path = ttk.filedialog.askopenfilename()
        if file_path:
            codes = self.homeController.detectedCode(file_path)
            for code in codes:
                LIST_CODE.append(code)
                self.liste_button.add_value(code)

    def remove_list(self):
        LIST_CODE = []
        self.liste_button.remove_values()

    """
    @Overrite
    """

    def main(self):
        self.mainloop()

    """
    @Overrite
    """

    def close(self):
        return
