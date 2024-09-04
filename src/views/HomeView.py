import customtkinter as ctk
from tkinter import filedialog
from tkinter import messagebox
from views.View import View
import pyperclip as pc
from config import APP_SIZE_X, APP_SIZE_Y, APP_TITLE

"""
    View associated with HomeController. It will be responsible for program's 
    main screen view.
"""


class HomeView(ctk.CTk, View):
    # -----------------------------------------------------------------------
    #        Constructor
    # -----------------------------------------------------------------------
    """
        @param controller Controller of this view
    """

    def __init__(self, controller):
        super().__init__()
        self.homeController = controller
        self.minsize(APP_SIZE_X,APP_SIZE_Y)
        self.title(APP_TITLE)
        
        self._add_image()
        self.frame_list = self._list_code()
    
    

    # -----------------------------------------------------------------------
    #        Methods
    # -----------------------------------------------------------------------
    
    def _add_image(self):
        self.btn_add_image = ctk.CTkButton(self, text='Ouvrire une image',command=self._open_dialog_file,font=("Roboto",16))
        self.btn_add_image.pack(fill = 'both', ipady=20, padx=100 ,pady=30)
        
    def _open_dialog_file(self):
        path = filedialog.askopenfilename()
        self.homeController.detectedCode(path)
        
    
    def _list_code(self):
        self.frame = ctk.CTkScrollableFrame(master=self)
        self.frame.pack(padx=100, pady=30, fill="both", expand= True)
        self.label_frame = ctk.CTkLabel(self.frame, text="Liste Code",font=("Roboto",16))
        self.label_frame.pack(fill='both', ipady=5, padx=150, pady=5)
        
        return self.frame
        
    def _add_table(self, item):
        self.btn_code = ctk.CTkButton(self.frame_list, text=str(item),command=lambda: self._copy_and_notification_code(item))
        self.btn_code.pack(fill='both', ipady=5, padx=10, pady=10)
        
    def _copy_and_notification_code(self,code):
        pc.copy(code)
        messagebox.showinfo("Information", f"code {code} copier")

    
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