import tkinter as tk
from tkinter import ttk

class MensagemGUI(ttk.Label):
    def __init__(self, parent):
        super().__init__(parent)
        self.config(
            text="",
            foreground="black"
        )

    def limpar(self):
        self.config(text="", foreground="black")

    def erro(self, texto):
        self.config(text=texto, foreground="red")

    def sucesso(self, texto):
        self.config(text=texto, foreground="green")
