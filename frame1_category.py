import tkinter as tk
import pandas as pd

def frame1_header(frame,p1,p2,p3,row_number):
    objects = []
    head1 = tk.Label(frame,text="Category",font=("ariel",15,"bold"),bd=8)
    head1.grid(row=row_number,column=0)
    head2 = tk.Label(frame,text=p1,font=("ariel",15,"bold"),bd=8)
    head2.grid(row=row_number,column=1)
    head3 = tk.Label(frame,text=p2,font=("ariel",15,"bold"),bd=8)
    head3.grid(row=row_number,column=2)
    head4 = tk.Label(frame,text=p3,font=("ariel",15,"bold"),bd=8)
    head4.grid(row=row_number,column=3)
    head5 = tk.Label(frame,text="Category Winner",font=("ariel",15,"bold"),bd=8)
    head5.grid(row=row_number,column=4)

    objects.append(head1)
    objects.append(head2)
    objects.append(head3)
    objects.append(head4)
    objects.append(head5)

    return objects

def frame1_summary_header(frame,row_number):
    head_sum_1 = tk.Label(frame,text="Player",font=("ariel",15,"bold"),bd=8)
    head_sum_1.grid(row=row_number,column=2)
    head_sum_2 = tk.Label(frame,text="Category Win Count",font=("ariel",15,"bold"),bd=8)
    head_sum_2.grid(row=row_number,column=3)
    return [head_sum_1,head_sum_2]

def create_row_summary(frame,p,count,row_number):
    obj1 = tk.Label(frame,text=p,bd=8,bg="powder blue")
    obj1.grid(row=row_number,column=2)
    obj2 = tk.Label(frame,text=count,bd=8,bg="powder blue")
    obj2.grid(row=row_number,column=3)
    return [obj1,obj2]

def create_row(frame,cat,s1,s2,s3,winner,row_number):
    objects = []
    obj1 = tk.Label(frame,text=cat,bd=8,bg="powder blue")
    obj1.grid(row=row_number,column=0)
    obj2 = tk.Label(frame,text=str(s1),bd=8,bg="powder blue")
    obj2.grid(row=row_number,column=1)
    obj3= tk.Label(frame,text=str(s2),bd=8,bg="powder blue")
    obj3.grid(row=row_number,column=2)
    obj4= tk.Label(frame,text=str(s3),bd=8,bg="powder blue")
    obj4.grid(row=row_number,column=3)
    obj5= tk.Label(frame,text=str(winner),bd=8,bg="powder blue")
    obj5.grid(row=row_number,column=4)

    objects.append(obj1)
    objects.append(obj2)
    objects.append(obj3)
    objects.append(obj4)
    objects.append(obj5)

    return objects 

def initiate_frame1_on_start(
    cat_stat_df, cat_winner_df,cat_win_count_df, 
    cat_stat_df5, cat_winner_df5,cat_win_count_df5,
    cat_stat_df10, cat_winner_df10, cat_win_count_df10,
    contrib_df, contrib_winner_df,frame,stats_of_interest):
    players = list(cat_stat_df.columns)
    
    header = frame1_header(frame,players[0],players[1],players[2],0)
    cats = {}

    for i,stat in enumerate(stats_of_interest):
        stat_vals = list(cat_stat_df.loc[stat])
        if stat != "Tov":
            cats[stat] = create_row(frame,stat,round(stat_vals[0],2),round(stat_vals[1],2),round(stat_vals[2],2),players[stat_vals.index(max(stat_vals))],i+1)
        else:
            cats[stat] = create_row(frame,stat,round(stat_vals[0],2),round(stat_vals[1],2),round(stat_vals[2],2),players[stat_vals.index(min(stat_vals))],i+1)
    
    header_sum= frame1_summary_header(frame, 11)
    players_sum = {}

    for i,player in enumerate(players):
        players_sum[player] = create_row_summary(frame,player,cat_win_count_df.loc[player,"Category_wins"],i+12)
    
    button_average = tk.Button(frame,text="Season-Average",font=("ariel",15,"bold"))
    button_average.grid(row=12,column=0)
    button_last_5 = tk.Button(frame,text="Last 5 Games",font=("ariel",15,"bold"))
    button_last_5.grid(row=13,column=0)
    button_last_10 = tk.Button(frame,text="Last 10 games",font=("ariel",15,"bold"))
    button_last_10.grid(row=14,column=0)

