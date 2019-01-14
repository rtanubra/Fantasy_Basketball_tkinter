import tkinter as tk
from run_me import *
from helper_fx0 import *
from pull_game_info1 import *
from analysis2 import *

import pandas as pd 
import numpy as np
from ohmysportsfeedspy import MySportsFeeds


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.Top = tk.Frame(self,width=1100,height=90,bg="powder blue", relief="sunken")
        self.Top.pack(side="top")

        self.left = tk.Frame(self,width=440,height=245,bg="red", relief="sunken")
        self.left.pack(side="left")
        
        self.right = tk.Frame(self,width=640,height=245,bg="red", relief="sunken")
        self.right.pack(side="right")   

        """
        self.bottom = tk.Frame(self,width=1100,height=345,bg="powder blue", relief="sunken")
        self.bottom.pack(side="bottom")
        """

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1100x700+0+0")
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()