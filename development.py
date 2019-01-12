"""
For Development use only. Does not require an api call to my_sports_feed
Will pull gamelogs from results directory. 
"""
from pull_game_info1 import *
from helper_fx0 import *
import pandas as pd

path = "results/player_gamelogs-nba-2018-2019-regular.json"
stats_of_interest = ["Reb","Ast","Pts","Tov","Stl","Blk","FgPct","FtPct","Fg3PtMade"]
input_names = ["Jae Crowder","Gordon Hayward","Garrett Temple"]
input_names = list_into_string(input_names)

def read_from_results(path,stats_of_interest):
    print("Obtaining gamelogs for each player of interest \n")
    import json
    from pprint import pprint

    with open(path) as f:
        data = json.load(f)

    gamelogs = data['playergamelogs']['gamelogs']
    dfs, players_dict = create_DataFrames(gamelogs,stats_of_interest)
    return dfs, players_dict 

def normalize_stats_sum(player_dfs,player_dict,stats_of_interest):
    print("Normalizing stats in each game for comparison \n")
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

def compare_player_contribution(normalized_dfs, players_dict,stats_of_interest):
    print("Building final output for comparison \n")
    """
    Build a single DF defining player contribution
    player_ID,player_name,season_avg, last_10, last_5
    """
    player_ids = []
    player_names = []
    season_avgs = []
    last_10s = []
    last_5s = []
    for player in players_dict:
        player_ids.append(player)
        player_names.append(players_dict[player])
        df = normalized_dfs[player][["g_summary","5g_ma","10g_ma"]]
        season_avgs.append(df["g_summary"].mean()) 
        last_10s.append(df["10g_ma"].iloc[-1])
        last_5s.append(df["5g_ma"].iloc[-1])
    
    my_dict = {
        "Player_ID":player_ids,
        "Player_Name": player_names,
        "Avg_Contrib": season_avgs,
        "Last10_Avg":last_10s,
        "Last5_Avg":last_5s
    }
    df = pd.DataFrame(my_dict)
    df = df.sort_values(['Avg_Contrib', 'Last10_Avg',"Last5_Avg"],ascending=False)
    return df

    
    
dfs, players_dict = read_from_results(path, stats_of_interest)
normalized_dfs = normalize_stats_sum(dfs,players_dict,stats_of_interest)
print(compare_player_contribution(normalized_dfs,players_dict,stats_of_interest))
