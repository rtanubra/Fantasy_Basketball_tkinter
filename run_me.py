import pandas as pd 
import numpy as np
from ohmysportsfeedspy import MySportsFeeds

from helper_fx0 import *
from pull_game_info1 import *
from analysis2 import *

def run_functs(input_names,stats_of_interest,number_games=None):
    """
    Pull game logs API call takes time
        uses pull_game_info1 module
    """
    gamelogs = pull_game_logs(input_names,stats_of_interest)
    dfs, players_dict = create_DataFrames(gamelogs,stats_of_interest)
    
    """
    Analysis prior to normalizing dataframes.
        uses analysis2 module
    """
    cat_stat_df, cat_winner_df,cat_win_count_df= compare_stats_last_games(dfs,players_dict,stats_of_interest)
    cat_stat_df5, cat_winner_df5,cat_win_count_df5= compare_stats_last_games(dfs,players_dict,stats_of_interest,5)
    cat_stat_df10, cat_winner_df10,cat_win_count_df10= compare_stats_last_games(dfs,players_dict,stats_of_interest,10)
    
    """
    Normalizes dfs for comparison as a single number
        uses analysis2 module
    """
    normalized_dfs = normalize_stats_sum(dfs,players_dict,stats_of_interest)
    contrib_df, contrib_winner_df = compare_player_contribution(normalized_dfs,players_dict,stats_of_interest)
    """
    print("LAST 10 GAMES")
    print(cat_win_count_df10)
    print("\n")
    print(cat_winner_df10)
    print("LAST 5 GAMES")
    print(cat_win_count_df5)
    print("\n")
    print(cat_winner_df5)
    print("\n")
    print("THIS Season Average")
    print(cat_win_count_df)
    print("\n")
    print(cat_winner_df)
    print("\n")
    print("ANALYZING CONTRIBUTIONS AS SINGLE NUMBER")
    print(contrib_df)
    print("\n")
    print(contrib_winner_df)
    """
    return cat_stat_df, cat_winner_df,cat_win_count_df,cat_stat_df5, cat_winner_df5,cat_win_count_df5,cat_stat_df10, cat_winner_df10,cat_win_count_df10,contrib_df, contrib_winner_df

"""
##These inputs will be provided by tkinter GUI from the person

input_names = ["Stephen Curry", "Lebron James","Kevin Durant"]
input_names = list_into_string(input_names)
stats_of_interest = ["Reb","Ast","Pts","Tov","Stl","Blk","FgPct","FtPct","Fg3PtMade"]

cat_stat_df, cat_winner_df,cat_win_count_df,cat_stat_df5, cat_winner_df5,cat_win_count_df5,cat_stat_df10, cat_winner_df10,cat_win_count_df10,contrib_df, contrib_winner_df = run_functs(input_names,stats_of_interest)
"""