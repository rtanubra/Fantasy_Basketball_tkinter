import tkinter as tk
import pandas as pd

#===================FUCNTIONS TO CREATE FRAME 2 TABLES#===================
            #*********Table1 header#*********
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

            #*********Table1 body#*********
def frame_2_create_row(frame,player,season_avg,last_10,last5,row_number):
    player_obj = tk.Label(frame,text=player,bd=8,bg="powder blue")
    player_obj.grid(row=row_number,column=0)
    season_obj = tk.Label(frame,text=str(round(season_avg,2)),bd=8,bg="powder blue")
    season_obj.grid(row=row_number,column=1)
    last_10_obj = tk.Label(frame,text=str(round(last_10,2)),bd=8,bg="powder blue")
    last_10_obj.grid(row=row_number,column=2)
    last_5_obj = tk.Label(frame,text=str(round(last5,2)),bd=8,bg="powder blue")
    last_5_obj.grid(row=row_number,column=3)
    return [player_obj,season_obj,last_10_obj,last_5_obj]

            #*********Table2 header#*********
def frame_2_table2_header(frame,row_number):
    frame_2_table2_header1 = tk.Label(frame,text="Time Duration",font=("ariel",15,"bold"),bd=8)
    frame_2_table2_header1.grid(row=row_number,column=0)
    frame_2_table2_header2 = tk.Label(frame,text="Winning Player",font=("ariel",15,"bold"),bd=8)
    frame_2_table2_header2.grid(row=row_number,column=1)
    return [frame_2_table2_header1,frame_2_table2_header2]
            #*********Table2 body#*********
def frame_2_table2_create_row(frame,time_frame,player,row_number):
    time_obj = tk.Label(frame,text=time_frame,bd=8,bg="powder blue")
    time_obj.grid(row=row_number,column=0)
    player_obj = tk.Label(frame,text=player,bd=8,bg="powder blue")
    player_obj.grid(row=row_number,column=1)
    return [time_obj,player_obj]
    

#===================FUCNTION TO PRE-POPULATE FRAME 2 ON START#===================
def initiate_frame2_on_start(
    cat_stat_df, cat_winner_df,cat_win_count_df, 
    cat_stat_df5, cat_winner_df5,cat_win_count_df5,
    cat_stat_df10, cat_winner_df10, cat_win_count_df10,
    contrib_df, contrib_winner_df,frame,stats_of_interest):

    #============Create frame2 table1 title ============#
    frame2_title = tk.Label(frame,text="Player Contribution Summary Breakdown",font=("ariel",20,"bold"),bd=8)
    frame2_title.grid(row=0, columnspan=3)

    #============Create frame2 table1 header============#
    frame2_table1_header = frame_2_header(frame,1) 

    #============Create frame2 table1 rows============#
    frame2_table1_rows = {}
    players = list(contrib_df["Player_Name"])
    season_avg = list(contrib_df["Avg_Contrib"])
    last_10 = list(contrib_df["Last10_Avg"])
    last_5 = list(contrib_df["Last5_Avg"])
    for i in range(len(players)):
        frame2_table1_rows[str(i)] = frame_2_create_row(frame,players[i],season_avg[i],last_10[i],last_5[i],i+2)
        
    #============Create frame2 table2 title ============#
    frame2_title2 = tk.Label(frame,text="Player Contribution Summary",font=("ariel",20,"bold"),bd=8)
    frame2_title2.grid(row=len(players)+3, columnspan=3)

    #============Create frame2 table2 header ============#
    frame2_table2_header = frame_2_table2_header(frame,len(players)+4)

    #============Create frame2 table2 rows ============#
    frame2_table2_body = {}
    time_durations = list(contrib_winner_df.index)
    winners = list(contrib_winner_df["Winner"])
    current_row = len(players)+5
    for i in range(len(time_durations)):
        frame2_table2_body[time_durations[i]]=frame_2_table2_create_row(frame,time_durations[i],winners[i],i+current_row)
    print(frame2_table2_body.keys())
    return frame2_table1_header,frame2_table1_rows,frame2_table2_header,frame2_table2_body

#=======================FUCNTIONS TO UPDATE FRAME 2 TABLES (3-PLAYERS)#=======================
                #*********Table1 body#*********
def frame_2_update_t1_row3p(frame,contrib_df,body_obj):
    players = list(contrib_df["Player_Name"])
    Avg_Contribs = list(contrib_df["Avg_Contrib"])
    Last10_Avgs = list(contrib_df["Last10_Avg"])
    Last5_Avgs = list(contrib_df["Last5_Avg"])
    for i in range(len(players)):
        body_obj[str(i)][0]["text"] = players[i]
        body_obj[str(i)][1]["text"] = round(Avg_Contribs[i],2)
        body_obj[str(i)][2]["text"] = round(Last10_Avgs[i],2)
        body_obj[str(i)][3]["text"] = round(Last5_Avgs[i],2)
    if len(players)==2:
        body_obj["2"][0]["text"] = "P3 Not-Applicable"
        body_obj["2"][1]["text"] = 0
        body_obj["2"][2]["text"] = 0
        body_obj["2"][3]["text"] = 0

    return body_obj

def frame_2_update_t2_row3p(frame,contrib_winner_df,body_obj):
    winners = list(contrib_winner_df["Winner"])
    time_duration = list(contrib_winner_df.index)
    for i,x in enumerate(time_duration):
        body_obj[x][1]["text"]= winners[i]
    return body_obj

#===================FUCNTION CALLED ON SUBMIT (DISPLAY ANALYSIS OF CALLED DATE)#===================
def frame_2_submit_3players(frame,contrib_df,contrib_winner_df,f2_t1_body,f2_t2_body):
    f2_t1_body = frame_2_update_t1_row3p(frame,contrib_df,f2_t1_body)
    f2_t2_body = frame_2_update_t2_row3p(frame,contrib_winner_df,f2_t2_body)
    return f2_t1_body,f2_t2_body

def frame_2_submit_2players(frame,contrib_df,contrib_winner_df,f2_t1_body,f2_t2_body):
    f2_t1_body = frame_2_update_t1_row3p(frame,contrib_df,f2_t1_body)
    f2_t2_body = frame_2_update_t2_row3p(frame,contrib_winner_df,f2_t2_body)
    return f2_t1_body,f2_t2_body