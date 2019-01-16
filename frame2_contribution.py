import tkinter as tk
import pandas as pd

def frame_2_header(frame,row_number):
    frame_2_header_1 = tk.Label(frame,text="Player Name",font=("ariel",15,"bold"),bd=8)
    frame_2_header_1.grid(row=row_number, column= 0)
    frame_2_header_2 = tk.Label(frame,text="Season Average",font=("ariel",15,"bold"),bd=8)
    frame_2_header_2.grid(row=row_number, column= 1)
    frame_2_header_3 = tk.Label(frame,text="Last 10 Games",font=("ariel",15,"bold"),bd=8)
    frame_2_header_3.grid(row=row_number, column= 2)
    frame_2_header_4 = tk.Label(frame,text="Last 5 Games",font=("ariel",15,"bold"),bd=8)
    frame_2_header_4.grid(row=row_number, column= 3)
    
    return [frame_2_header_1,frame_2_header_2,frame_2_header_3,frame_2_header_4]  

def frame_2_create_row(frame,player,season_avg,last_10,last5,row_number):
    row_obj = []
    player_obj = tk.Label(frame,text=player,bd=8,bg="powder blue")
    player_obj.grid(row=row_number,column=0)
    season_obj = tk.Label(frame,text=str(round(season_avg,2)),bd=8,bg="powder blue")
    season_obj.grid(row=row_number,column=1)
    last_10_obj = tk.Label(frame,text=str(round(last_10,2)),bd=8,bg="powder blue")
    last_10_obj.grid(row=row_number,column=2)
    last_5_obj = tk.Label(frame,text=str(round(last5,2)),bd=8,bg="powder blue")
    last_5_obj.grid(row=row_number,column=3)

def frame_2_table2_header(frame,row_number):
    frame_2_table2_header1 = tk.Label(frame,text="Time Duration",font=("ariel",15,"bold"),bd=8)
    frame_2_table2_header1.grid(row=row_number,column=0)
    frame_2_table2_header2 = tk.Label(frame,text="Winning Player",font=("ariel",15,"bold"),bd=8)
    frame_2_table2_header2.grid(row=row_number,column=1)
    return [frame_2_table2_header1,frame_2_table2_header2]

def frame_2_table2_create_row(frame,time_frame,player,row_number):
    time_obj = tk.Label(frame,text=time_frame,bd=8,bg="powder blue")
    time_obj.grid(row=row_number,column=0)
    player_obj = tk.Label(frame,text=player,bd=8,bg="powder blue")
    player_obj.grid(row=row_number,column=1)

def initiate_frame2_on_start(
    cat_stat_df, cat_winner_df,cat_win_count_df, 
    cat_stat_df5, cat_winner_df5,cat_win_count_df5,
    cat_stat_df10, cat_winner_df10, cat_win_count_df10,
    contrib_df, contrib_winner_df,frame,stats_of_interest):

    #============Create frame2 table1 title ============#
    frame2_title = tk.Label(frame,text="Player Contribution Summary Breakdown",font=("ariel",20,"bold"),bd=8)
    frame2_title.grid(row=0, columnspan=3)

    #============Create frame2 table1 header============#
    frame2_header = frame_2_header(frame,1) 

    #============Create frame2 table1 rows============#
    frame2_rows = {}
    players = list(contrib_df["Player_Name"])
    season_avg = list(contrib_df["Avg_Contrib"])
    last_10 = list(contrib_df["Last10_Avg"])
    last_5 = list(contrib_df["Last5_Avg"])
    for i in range(len(players)):
        frame2_rows[players[i]] = frame_2_create_row(frame,players[i],season_avg[i],last_10[i],last_5[i],i+2)
        
    #============Create frame2 table2 title ============#
    frame2_title = tk.Label(frame,text="Player Contribution Summary",font=("ariel",20,"bold"),bd=8)
    frame2_title.grid(row=len(players)+3, columnspan=3)

    #============Create frame2 table2 header ============#
    frame2_table2_title = frame_2_table2_header(frame,len(players)+4)

    #============Create frame2 table2 rows ============#
    time_durations = list(contrib_winner_df.index)
    winners = list(contrib_winner_df["Winner"])
    current_row = len(players)+5
    for i in range(len(time_durations)):
        frame_2_table2_create_row(frame,time_durations[i],winners[i],i+current_row)

