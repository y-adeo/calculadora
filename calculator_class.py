import tkinter
import tkinter as tk
from typing import List

class Claculator:
    def __init__(
            self,
            root: tk.Tk,
            label: tk.Label,
            display: tkinter.Entry,
            buttons: List[List[tk.Button]]
    ):
        self.root = root
        self.label = label
        self.display = display
        self.buttons = buttons

