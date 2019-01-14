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

def create_row(cat,s1,s2,s3,winner,row_number):
    objects = []
    obj1 = tk.Label(frame,text=cat,bd=8)
    obj1.grid(row=row_number,column=0)
    obj2 = tk.Label(frame,text=str(s1),bd=8)
    obj2.grid(row=row_number,column=1)
    obj3= tk.Label(frame,text=str(s2),bd=8)
    obj3.grid(row=row_number,column=2)
    obj4= tk.Label(frame,text=str(s3),bd=8)
    obj4.grid(row=row_number,column=3)
    obj5= tk.Label(frame,text=str(winner),bd=8)
    obj5.grid(row=row_number,column=4)

    objects.append(obj1)
    objects.append(obj2)
    objects.append(obj3)
    objects.append(obj4)
    objects.append(obj5)

    return objects 

def initiate_frame1_on_start(cat_stat_df, cat_winner_df,cat_win_count_df, cat_stat_df5, cat_winner_df5,cat_win_count_df5,cat_stat_df10, cat_winner_df10, cat_win_count_df10,contrib_df, contrib_winner_df,frame):
    players = list(cat_stat_df.columns)

    header = frame1_header(frame,players[0],players[1],"Player 3",0)