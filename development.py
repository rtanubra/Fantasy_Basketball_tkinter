"""
For Development use only. Does not require an api call to my_sports_feed
Will pull gamelogs from results directory. 
"""
from pull_game_info1 import *
from helper_fx0 import *

path = "results/player_gamelogs-nba-2018-2019-regular.json"
stats_of_interest = ["Reb","Ast","Pts","Tov","Stl","Blk","FgPct","FtPct","Fg3PtMade"]
input_names = ["Jae Crowder","Gordon Hayward","Garrett Temple"]
input_names = list_into_string(input_names)

def read_from_results(path,stats_of_interest):
    import json
    from pprint import pprint

    with open(path) as f:
        data = json.load(f)

    gamelogs = data['playergamelogs']['gamelogs']
    dfs, players_dict = create_DataFrames(gamelogs,stats_of_interest)
    return dfs, players_dict 

def find_max_stats(dfs,stats_of_interest):
    """Given data frame of gamelogs and stats of interest 
    returns a dictionary of max for each stat of interest"""
    stats_dict = {}
    stats_max_dict = {}
    for df_id in dfs:
        for stat in stats_of_interest:
            if stat in stats_dict:
                stats_dict[stat].extend(list(dfs[df_id][stat]))
            else:
                stats_dict[stat] = list(dfs[df_id][stat])
    for stat in stats_dict:
        stats_max_dict[stat]= max(stats_dict[stat])
    return stats_max_dict

def define_player_contribution(dfs, players_dict,stats_of_interest):
    stats_max_dict = find_max_stats(dfs,stats_of_interest)
    
    
dfs, players_dict = read_from_results(path, stats_of_interest)
find_max_stats(dfs,stats_of_interest)