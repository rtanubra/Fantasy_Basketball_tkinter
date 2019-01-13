import pandas as pd
import numpy as np

def list_into_string(names):
    my_str=""
    for i,name  in enumerate(names):
        name = name.replace(" ","-")
        my_str += name 
        if i < len(names)-1:
            my_str += ","
    return my_str

def pull_players_dict(games):
    my_dict = {}
    for game in games:
        if game["player"]["ID"] not in my_dict:
            my_dict[game["player"]["ID"]] =game["player"]["FirstName"] +" "+game["player"]["LastName"] 
    return my_dict

"""
    normalize_stats_sum
Currently this amends the players_dfs into a normalized df.
The purpose of this would be to be able to summarize the 9 category contribution into a single number 
    Much like team points for a real game.
At the current stats this amends the dfs. Need to change this so we create a new df.
    -If we ammend the df we cannot look back and change. 
"""
def normalize_stats_sum(player_dfs,player_dict,stats_of_interest):
    print("Normalizing stats in each game for comparison at a single number \n")
    list_of_dfs = [player_dfs[each] for each in player_dict]
    main_df = pd.concat(list_of_dfs,axis=0)
    
    ##Short way to find maximums of each cat stat
    maximums = {}
    for statistic in stats_of_interest:
        maximums[statistic] = np.max(main_df.loc[:,statistic])
    
    for player in player_dfs: 
        for statistic in stats_of_interest:
            if statistic == "Tov":
                player_dfs[player][statistic] = player_dfs[player][statistic].div(maximums[statistic]).mul(-100)
            else:
                player_dfs[player][statistic] = player_dfs[player][statistic].div(maximums[statistic]).mul(100)
        player_dfs[player]["g_summary"] = player_dfs[player].sum(axis=1)
        player_dfs[player]["5g_ma"] = player_dfs[player]["g_summary"].rolling(5).mean()
        player_dfs[player]["10g_ma"] = player_dfs[player]["g_summary"].rolling(10).mean()

    return player_dfs