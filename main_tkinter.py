import tkinter as tk
from run_me import *
from helper_fx0 import *
from pull_game_info1 import *
from analysis2 import *

import pandas as pd 
import numpy as np
from ohmysportsfeedspy import MySportsFeeds

class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        #initiate tk functions you will use here.
        self.master = master
        #self.pack()
        self.grid()
        self.create_widgets()
    
    def submit(self):
        print("Initializing Trade Analysis. Please wait:")
        my_names = []
        if self.player1_inp.get():
            my_names.append(self.player1_inp.get())
        if self.player2_inp.get():
            my_names.append(self.player2_inp.get())
        if self.player3_inp.get():
            my_names.append(self.player3_inp.get())
        if len(my_names) < 2:
            print()
        input_names = list_into_string(my_names)
        stats_of_interest = ["Reb","Ast","Pts","Tov","Stl","Blk","FgPct","FtPct","Fg3PtMade"]
        #run_functs(my_names,stats_of_interest)
        print(f"Running Analysis for {input_names}")
        print(f"Categories of interest {stats_of_interest}")
        cat_stat_df, cat_winner_df,cat_win_count_df,cat_stat_df5, cat_winner_df5,cat_win_count_df5,cat_stat_df10, cat_winner_df10,cat_win_count_df10,contrib_df, contrib_winner_df = run_functs(input_names,stats_of_interest)
    
    def create_widgets(self):
        self.title = tk.Label(self)
        self.title["text"] = "Fantasy NBA Analyst\nLet's Begin"
        self.title.pack(side="top",fill="x")
        
        self.player1_label =tk.Label(self,text="Player 1")
        self.player1_label.pack()
        self.player1_inp = tk.Entry(self)
        self.player1_inp.pack(side="left")
       
        self.player2_label =tk.Label(self,text="Player 2")
        self.player2_label.pack()
        self.player2_inp = tk.Entry(self)
        self.player2_inp.pack()

        self.player3_label= tk.Label(self,text="Player 3")
        self.player3_label.pack()
        self.player3_inp = tk.Entry(self)
        self.player3_inp.pack()

        self.submit = tk.Button(
            self, text = "SUBMIT", fg= "green",command = self.submit
        )
        self.submit.pack()

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack()

        #******* STATUS BAR *******
        self.status = tk.Label(self,text="Ready to Analyze",bd=1,relief="sunken",anchor="w")
        self.status.pack(side="bottom",fill="x")

    

root = tk.Tk()
root.minsize(width=350, height=250)
app = Application(master=root)
app.mainloop()