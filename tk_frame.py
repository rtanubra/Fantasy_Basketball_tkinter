import tkinter as tk
from run_me import *
from helper_fx0 import *
from pull_game_info1 import *
from analysis2 import *

import pandas as pd 
import numpy as np
from ohmysportsfeedspy import MySportsFeeds

from frame1_category import *
from frame2_contribution import *
#============Keep below if you want to prepopulate analysis on start=====================#
from development import *


class MainApplication(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        #initiate tk functions you will use here.
        self.master = master
        
        self.Tops = tk.Frame(self.master,width=1200,height=200,bg="powder blue",relief="sunken")
        self.Tops.pack(side="top",fill="x")

        self.f1 = tk.Frame(self.master,width=550,height=500,bg="powder blue",relief="sunken")
        self.f1.pack(side="left")

        self.f2 = tk.Frame(self.master,width=550,height=500,bg="powder blue",relief="sunken")
        self.f2.pack(side="right")
        
        self.create_widgets_Tops(self.Tops)
        self.create_widgets_f1_f2_start(self.f1,self.f2)

#=============Initialize necessary variables for analyzis=====================#
        self.stats_of_interest = ["Reb","Ast","Pts","Tov","Stl","Blk","FgPct","FtPct","Fg3PtMade"]
        #self.create_widgets_f2(self.f2)

#==========================TOP is name input========================
    def create_widgets_Tops(self,frame):
        #this will create widgets for name inputs
        self.title = tk.Label(frame,text="Input player names for analysis",fg="black",bd=10,anchor="w",font=("ariel",20,"bold"))
        self.title.grid(row=0,column=3)

        self.player1_label =tk.Label(frame,text="Player 1")
        self.player1_label.grid(row=1,column=0)
        self.player1_inp = tk.Entry(frame)
        self.player1_inp.grid(row=1,column=1)
       
        self.player2_label =tk.Label(frame,text="Player 2")
        self.player2_label.grid(row=2,column=0)
        self.player2_inp = tk.Entry(frame)
        self.player2_inp.grid(row=2,column=1)

        self.player3_label= tk.Label(frame,text="Player 3")
        self.player3_label.grid(row=3,column=0)
        self.player3_inp = tk.Entry(frame)
        self.player3_inp.grid(row=3, column=1)

        self.submit = tk.Button(
            frame, text = "SUBMIT", fg= "green",command = self.submit
        )
        self.submit.grid(row=3,column=2) 

        self.quit = tk.Button(frame, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.grid(row=4,column=2)

#==========================Initiate Frame 1 and Frame 2 at the start========================   
    def create_widgets_f1_f2_start(self,frame1,frame2):
        #this will create widgets to compare category stuff
        cat_stat_df, cat_winner_df,cat_win_count_df, cat_stat_df5, cat_winner_df5,cat_win_count_df5,cat_stat_df10, cat_winner_df10, cat_win_count_df10,contrib_df, contrib_winner_df = run_this_development()
        self.f1_t1_head,self.f1_t1_body,self.f1_t2_head,self.f1_t2_body =initiate_frame1_on_start(
            cat_stat_df, cat_winner_df,cat_win_count_df, 
            cat_stat_df5, cat_winner_df5,cat_win_count_df5,
            cat_stat_df10, cat_winner_df10, cat_win_count_df10,
            contrib_df, contrib_winner_df,frame1,stats_of_interest)
        initiate_frame2_on_start(
            cat_stat_df, cat_winner_df,cat_win_count_df, 
            cat_stat_df5, cat_winner_df5,cat_win_count_df5,
            cat_stat_df10, cat_winner_df10, cat_win_count_df10,
            contrib_df, contrib_winner_df,frame2,stats_of_interest)
    
#==========================RIGHT f2 contribution points breakdown======================== 
    def create_widgets_f2(self,frame2):
        #this will create widgets to compare contribution points
        pass
        
#===================================SUBMIT FUNCTION============================
    def submit(self):
        players_to_analyze = []
        if self.player1_inp.get() != "":
            players_to_analyze.append(self.player1_inp.get())
        if self.player2_inp.get() != "":
            players_to_analyze.append(self.player2_inp.get())
        if self.player3_inp.get() != "":
            players_to_analyze.append(self.player3_inp.get())
        print(f"Initializing Trade Analysis. Please wait: Analyzing {players_to_analyze}")
        players_to_analyze = list_into_string(players_to_analyze)
        self.cat_stat_df, self.cat_winner_df,self.cat_win_count_df,self.cat_stat_df5, self.cat_winner_df5,self.cat_win_count_df5,self.cat_stat_df10, self.cat_winner_df10,self.cat_win_count_df10,self.contrib_df, self.contrib_winner_df = run_functs(players_to_analyze,self.stats_of_interest)
        self.f1_t1_head,self.f1_t1_body,self.f1_t2_head,self.f1_t2_body = update_frame1_3p(self.f1,self.cat_stat_df,self.cat_win_count_df,self.f1_t1_head,self.f1_t1_body,self.f1_t2_body)


#===================Toggle Category breakdown Season/5/10==========================#
if __name__ == "__main__":
    root = tk.Tk()
    root.title("NBA Fantasy Analysis App")
    root.geometry("1200x750+0+0")
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()