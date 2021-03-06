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
        self.count = 0 #Submit clicks

#=============Initialize necessary variables for analyzis=====================#
        self.stats_of_interest = ["Reb","Ast","Pts","Tov","Stl","Blk","FgPct","FtPct","Fg3PtMade"]
        #self.create_widgets_f2(self.f2)

#==========================TOP is name input========================
    def create_widgets_Tops(self,frame):
        #this will create widgets for name inputs
        self.title = tk.Label(frame,text="Input player names for analysis",fg="black",bd=10,anchor="w",font=("ariel",20,"bold"))
        self.title.grid(row=0,column=2,columnspan=3)

        self.player1_label =tk.Label(frame,text="Player 1")
        self.player1_label.grid(row=1,column=0)
        self.player1_inp = tk.Entry(frame)
        self.player1_inp.grid(row=1,column=1)
       
        self.player2_label =tk.Label(frame,text="Player 2")
        self.player2_label.grid(row=1,column=2)
        self.player2_inp = tk.Entry(frame)
        self.player2_inp.grid(row=1,column=3)

        self.player3_label= tk.Label(frame,text="Player 3")
        self.player3_label.grid(row=1,column=4)
        self.player3_inp = tk.Entry(frame)
        self.player3_inp.grid(row=1, column=5)

        self.submit = tk.Button(
            frame, text = "SUBMIT", fg= "green",command = self.submit
        )
        self.submit.grid(row=3,column=3) 

        self.quit = tk.Button(frame, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.grid(row=3,column=4)
        #=====================Frame1 buttons to toggle avg v 5 v 10
        self.state= "avg"
        self.button_average = tk.Button(frame,text="Season-Average",font=("ariel",15,"bold"),command=lambda: self.toggle("avg"))
        self.button_average.grid(row=3,column=0)
        self.button_last_5 = tk.Button(frame,text="Last 5 Games",font=("ariel",15,"bold"),command=lambda: self.toggle("5"))
        self.button_last_5.grid(row=3,column=2)
        self.button_last_10 = tk.Button(frame,text="Last 10 games",font=("ariel",15,"bold"),command=lambda: self.toggle("10"))
        self.button_last_10.grid(row=3,column=1)

        self.status_label = tk.Label(frame,text="Status:",bd=8,font=("ariel",15,"bold"),relief="sunken",bg="grey")
        self.status_label.grid(row=4,column=0)
        self.status = tk.Label(frame,text="Input player names for analysis and hit Submit",bd=8,font=("ariel",15,"bold"),relief="sunken",bg="grey")
        self.status.grid(row=4,column=1,columnspan=3)

#==========================Initiate Frame 1 and Frame 2 at the start========================   
    def create_widgets_f1_f2_start(self,frame1,frame2):
        #this will create widgets to compare category stuff
        cat_stat_df, cat_winner_df,cat_win_count_df, cat_stat_df5, cat_winner_df5,cat_win_count_df5,cat_stat_df10, cat_winner_df10, cat_win_count_df10,contrib_df, contrib_winner_df = run_this_development()
        self.f1_t1_head,self.f1_t1_body,self.f1_t2_head,self.f1_t2_body =initiate_frame1_on_start(
            cat_stat_df, cat_winner_df,cat_win_count_df, 
            cat_stat_df5, cat_winner_df5,cat_win_count_df5,
            cat_stat_df10, cat_winner_df10, cat_win_count_df10,
            contrib_df, contrib_winner_df,frame1,stats_of_interest)
        self.f2_t1_head,self.f2_t1_body,self.f2_t2_head,self.f2_t2_body =initiate_frame2_on_start(
            cat_stat_df, cat_winner_df,cat_win_count_df, 
            cat_stat_df5, cat_winner_df5,cat_win_count_df5,
            cat_stat_df10, cat_winner_df10, cat_win_count_df10,
            contrib_df, contrib_winner_df,frame2,stats_of_interest)
        """
        #=====================Frame1 buttons to toggle avg v 5 v 10
        self.state= "avg"
        self.button_average = tk.Button(frame1,text="Season-Average",font=("ariel",15,"bold"),command=lambda: self.toggle("avg"))
        self.button_average.grid(row=12,column=0)
        self.button_last_5 = tk.Button(frame1,text="Last 5 Games",font=("ariel",15,"bold"),command=lambda: self.toggle("5"))
        self.button_last_5.grid(row=13,column=0)
        self.button_last_10 = tk.Button(frame1,text="Last 10 games",font=("ariel",15,"bold"),command=lambda: self.toggle("10"))
        self.button_last_10.grid(row=14,column=0)
        """
        
#===================================SUBMIT FUNCTION============================
    def submit(self):
        self.count += 1
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

        #====================Perform check how many players we obtained===================#
        obtained = list(self.cat_win_count_df.index)
        #===============Call the correct function based on the number of players successfully obtained ===============================
        if len(obtained)== 3:
            self.status["text"] = "Analyzing 3 players, displaying seaseon averages"
            self.f1_t1_head,self.f1_t1_body,self.f1_t2_body = update_frame1_3p(self.f1,self.cat_stat_df,self.cat_win_count_df,self.f1_t1_head,self.f1_t1_body,self.f1_t2_body,self.stats_of_interest)
            self.f2_t1_body,self.f2_t2_body = frame_2_submit_3players(self.f2,self.contrib_df, self.contrib_winner_df,self.f2_t1_body,self.f2_t2_body)
        elif len(obtained) == 2:
            self.status["text"] = "Analyzing 2 players, displaying seaseon averages"
            self.f1_t1_head,self.f1_t1_body,self.f1_t2_body = update_frame1_2p(self.f1,self.cat_stat_df,self.cat_win_count_df,self.f1_t1_head,self.f1_t1_body,self.f1_t2_body,self.stats_of_interest)
            self.f2_t1_body,self.f2_t2_body = frame_2_submit_2players(self.f2,self.contrib_df, self.contrib_winner_df,self.f2_t1_body,self.f2_t2_body)

#===================Toggle Category breakdown Season/5/10==========================#
    def toggle(self,time_frame):
        #Prevent unecessary change of state
        if self.state != time_frame:
            self.state = time_frame
            obtained = list(self.cat_win_count_df.index)
            if time_frame == "avg":
                if len(obtained)== 3:
                    self.status["text"] = "Analyzing 3 players, displaying seaseon averages"
                    self.f1_t1_head,self.f1_t1_body,self.f1_t2_body = update_frame1_3p(self.f1,self.cat_stat_df,self.cat_win_count_df,self.f1_t1_head,self.f1_t1_body,self.f1_t2_body,self.stats_of_interest)
                elif len(obtained) == 2:  
                    self.status["text"] = "Analyzing 2 players, displaying seaseon averages"
                    self.f1_t1_head,self.f1_t1_body,self.f1_t2_body = update_frame1_2p(self.f1,self.cat_stat_df,self.cat_win_count_df,self.f1_t1_head,self.f1_t1_body,self.f1_t2_body,self.stats_of_interest)
            elif time_frame == "5":
                if len(obtained)== 3:
                    self.status["text"] = "Analyzing 3 players, displaying last 5 games"
                    self.f1_t1_head,self.f1_t1_body,self.f1_t2_body = update_frame1_3p(self.f1,self.cat_stat_df5,self.cat_win_count_df5,self.f1_t1_head,self.f1_t1_body,self.f1_t2_body,self.stats_of_interest)
                elif len(obtained) == 2:
                    self.status["text"] = "Analyzing 2 players, displaying last 5 games"
                    self.f1_t1_head,self.f1_t1_body,self.f1_t2_body = update_frame1_2p(self.f1,self.cat_stat_df5,self.cat_win_count_df5,self.f1_t1_head,self.f1_t1_body,self.f1_t2_body,self.stats_of_interest)
            else:
                if len(obtained)== 3:
                    self.status["text"] = "Analyzing 3 players, displaying last 10 games"
                    self.f1_t1_head,self.f1_t1_body,self.f1_t2_body = update_frame1_3p(self.f1,self.cat_stat_df10,self.cat_win_count_df10,self.f1_t1_head,self.f1_t1_body,self.f1_t2_body,self.stats_of_interest)
                elif len(obtained) == 2:
                    self.status["text"] = "Analyzing 3 players, displaying last 10 games"
                    self.f1_t1_head,self.f1_t1_body,self.f1_t2_body = update_frame1_2p(self.f1,self.cat_stat_df10,self.cat_win_count_df10,self.f1_t1_head,self.f1_t1_body,self.f1_t2_body,self.stats_of_interest)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("NBA Fantasy Analysis App")
    root.geometry("1200x750+0+0")
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()