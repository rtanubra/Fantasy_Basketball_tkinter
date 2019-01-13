import pandas as pd 
import numpy as np
from ohmysportsfeedspy import MySportsFeeds
from helper_fx0 import *

def pull_game_logs(player_names,stats_of_interest):
    msf_user = ""
    msf_pass = ""
    with open("inputs/msf.txt","r") as my_file:
        msf_user = my_file.readline()

    #Pull game logs for various player names and returns dfs. 
    msf = MySportsFeeds(version="1.2")
    msf.authenticate("e09cc51e-beb1-43ac-b888-20a591","0010RugbyFight")
    output = msf.msf_get_data(
        league='nba',
        season='2018-2019-regular',
        feed='player_gamelogs',
        format='json',
        player= player_names,
        sort= "player.lastname"
        )
    gamelogs = output['playergamelogs']['gamelogs']
    return gamelogs

    
def create_DataFrames(gamelogs,stats_of_interest):
    player_dict = pull_players_dict(gamelogs)
    player_dfs = {}
    for game in gamelogs:
        if game["player"]["ID"] not in player_dfs:
            player_dfs[game["player"]["ID"]] = {}
            player_dfs[game["player"]["ID"]]["Game"] = [game["game"]["date"]]
            for statistic in stats_of_interest:
                player_dfs[game["player"]["ID"]][statistic] = [float(game["stats"][statistic]["#text"])] 
        else:
            player_dfs[game["player"]["ID"]]["Game"].append(game["game"]["date"])
            for statistic in stats_of_interest:
                player_dfs[game["player"]["ID"]][statistic].append(float(game["stats"][statistic]["#text"]))
    
    for DataFrame in player_dfs:
        player_dfs[DataFrame] = pd.DataFrame(player_dfs[DataFrame])
        player_dfs[DataFrame]["Game"] = pd.to_datetime(player_dfs[DataFrame]["Game"])
        player_dfs[DataFrame] = player_dfs[DataFrame].set_index(player_dfs[DataFrame]["Game"])
        player_dfs[DataFrame] = player_dfs[DataFrame][stats_of_interest]
    
    return player_dfs, player_dict

input_names = ["Jae Crowder","Gordon Hayward","Garrett Temple"]
input_names = list_into_string(input_names)
stats_of_interest = ["Reb","Ast","Pts","Tov","Stl","Blk","FgPct","FtPct","Fg3PtMade"]
#gamelogs = pull_game_logs(input_names,stats_of_interest)
#dfs, player_dict = create_DataFrames(gamelogs,stats_of_interest)
