import tkinter as tk
import pandas as pd

#========================== FUNCTIONS FOR CREATING HEADERS AND TABLES ============================
        #***************Frame1 table1 header***************
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
    #***************Frame1 table1 body***************
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
        #***************Frame1 table2 header***************
def frame1_summary_header(frame,row_number):
    head_sum_1 = tk.Label(frame,text="Player",font=("ariel",15,"bold"),bd=8)
    head_sum_1.grid(row=row_number,column=2)
    head_sum_2 = tk.Label(frame,text="Category Win Count",font=("ariel",15,"bold"),bd=8)
    head_sum_2.grid(row=row_number,column=3)
    return [head_sum_1,head_sum_2]

        #***************Frame1 table2 body***************
def create_row_summary(frame,p,count,row_number):
    obj1 = tk.Label(frame,text=p,bd=8,bg="powder blue")
    obj1.grid(row=row_number,column=2)
    obj2 = tk.Label(frame,text=count,bd=8,bg="powder blue")
    obj2.grid(row=row_number,column=3)
    return [obj1,obj2]

#==============================FUNCTIONS TO UPDATE TABLES IN FRAME 1=======================
              
                #***************Frame1 table1 header***************
def frame1_header_update(frame,p1,p2,p3,header_obj):
    header_obj[1]["text"] = p1
    header_obj[2]["text"] = p2
    header_obj[3]["text"] = p3
    return header_obj
                
                #***************Frame1 table1 body***************
def frame1_update_body(frame,stat,s1,s2,s3,winner,body_obj):
    body_obj[1]["text"] = str(round(s1,2))
    body_obj[2]["text"] = str(round(s2,2))
    body_obj[3]["text"] = str(round(s3,2))
    body_obj[4]["text"] = winner

                #***************Frame1 table2 body***************
def frame1_update_body_summary(frame,players,counts,body_obj):
    for i in range(len(players)):
        body_obj[str(i)][0]["text"] = players[i]
        body_obj[str(i)][1]["text"] = counts[i]
    return body_obj


#========================== FUNCTION INITIATED AT THE START TO DISPLAY SOME DATA PULLED OFFLINE (EARLIER) ============================
def initiate_frame1_on_start(
    cat_stat_df, cat_winner_df,cat_win_count_df, 
    cat_stat_df5, cat_winner_df5,cat_win_count_df5,
    cat_stat_df10, cat_winner_df10, cat_win_count_df10,
    contrib_df, contrib_winner_df,frame,stats_of_interest):
    players = list(cat_stat_df.columns)
    
    header1 = frame1_header(frame,players[0],players[1],players[2],0)
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
        players_sum[str(i)] = create_row_summary(frame,player,cat_win_count_df.loc[player,"Category_wins"],i+12)
    
    button_average = tk.Button(frame,text="Season-Average",font=("ariel",15,"bold"))
    button_average.grid(row=12,column=0)
    button_last_5 = tk.Button(frame,text="Last 5 Games",font=("ariel",15,"bold"))
    button_last_5.grid(row=13,column=0)
    button_last_10 = tk.Button(frame,text="Last 10 games",font=("ariel",15,"bold"))
    button_last_10.grid(row=14,column=0)
    return header1,cats,header_sum,players_sum

def update_frame1_3p(frame,cat_stat_df,cat_win_count_df,f1_t1_head,f1_t1_body,f1_t2_body,stats_of_interest):
    players = list(cat_stat_df.columns)
    f1_t1_head = frame1_header_update(frame,players[0],players[1],players[2],f1_t1_head)
    for i,stat in enumerate(stats_of_interest):
        stat_scores = list(cat_stat_df.loc[stat])
        print(stat_scores)
        if stat != "Tov":
            winner = players[stat_scores.index(max(stat_scores))]
        else:
            winner = players[stat_scores.index(min(stat_scores))]
        f1_t1_body[stat] = frame1_update_body(frame,stat,stat_scores[0],stat_scores[1],stat_scores[2],winner,f1_t1_body[stat])
    
    #need to do this because the order of players are different from table to table
    players = list(cat_win_count_df.index) 
    cat_scores_summary = list(cat_win_count_df["Category_wins"])
    f1_t2_body = frame1_update_body_summary(frame,players,cat_scores_summary,f1_t2_body)
    return f1_t1_head,f1_t1_body,f1_t2_body 

    print(cat_win_count_df)