"""
For Development use only. Does not require an api call to my_sports_feed
Will pull gamelogs from results directory. 
"""
from pull_game_info1 import *
from helper_fx0 import *
import pandas as pd

path = "results/player_gamelogs-nba-2018-2019-regular.json"
path1 = "results/LBJ_SC.json"
stats_of_interest = ["Reb","Ast","Pts","Tov","Stl","Blk","FgPct","FtPct","Fg3PtMade"]
input_names = ["Jae Crowder","Gordon Hayward","Garrett Temple"]
input_names = list_into_string(input_names)
"""
    read_from_results
For Development only:
This function is used because:
    1. Each API call into my sports feeds returns a JSON object and saves into a results direcotry
    2. Do not need internet to pull from that JSON object in directory during development.
"""
def read_from_results(path,stats_of_interest):
    print("Obtaining gamelogs for each player of interest \n")
    import json
    from pprint import pprint

    with open(path) as f:
        data = json.load(f)

    gamelogs = data['playergamelogs']['gamelogs']
    dfs, players_dict = create_DataFrames(gamelogs,stats_of_interest)
    return dfs, players_dict 
"""
    normalize_stats_sum
Currently this amends the players_dfs into a normalized df.
The purpose of this would be to be able to summarize the 9 category contribution into a single number 
    Much like team points for a real game.
At the current stats this amends the dfs. Need to change this so we create a new df.
    -If we ammend the df we cannot look back and change. 
"""
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

"""
    compare_player_contribution
First Analysis table. 
All 9 categories normalized present the following:
1. Season average
2. last 10 games
3. last 5 games
"""
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
    
    #Determine the category winner for each column.
    categories = ["season_avg","last_10","last_5"] 
    winners = [
        player_names[season_avgs.index(max(season_avgs))],
        player_names[last_10s.index(max(last_10s))],
        player_names[last_5s.index(max(last_5s))]
    ] 
    cat_win_dict = {
        "Category":categories,
        "Winner":winners
    }

    my_dict = {
        "Player_ID":player_ids,
        "Player_Name": player_names,
        "Avg_Contrib": season_avgs,
        "Last10_Avg":last_10s,
        "Last5_Avg":last_5s,
    }

    df = pd.DataFrame(my_dict)
    df = df.sort_values(["Last5_Avg",'Last10_Avg','Avg_Contrib'],ascending=False)
    df.set_index("Player_ID",inplace=True)
    cat_winners = pd.DataFrame(cat_win_dict)
    cat_winners.set_index("Category",inplace=True)

    return df , cat_winners

"""
    compare_stats_last_games
    Looks at the breakdown of each category of interest.
        Optional input the numnber_games_of_interest . used to compare across the last x games.
        If optional input is not provided a comparison for season average will be done.
    Identifies 
"""
def compare_stats_last_games(dfs,players_dict,stats_of_interest,numb_games=None):
    if numb_games != None:
        print(f"Comparing players across categories LAST {numb_games} GAMES")
        my_dict = {
            "Category": stats_of_interest
        }
        players_stats = {}   
        for player_id in players_dict:
            curr_player_stat = []
            for stat in stats_of_interest:
                if player_id in players_stats:
                    players_stats[player_id].append(dfs[player_id][stat][-numb_games:].mean())
                else:
                    players_stats[player_id] = [dfs[player_id][stat][-numb_games:].mean()]
            my_dict[players_dict[player_id]] = players_stats[player_id]
    else:
        print("Comparing players across categories SEASON AVERAGE")
        my_dict = {
            "Category": stats_of_interest
        }
        players_stats = {}   
        for player_id in players_dict:
            curr_player_stat = []
            for stat in stats_of_interest:
                if player_id in players_stats:
                    players_stats[player_id].append(dfs[player_id][stat].mean())
                else:
                    players_stats[player_id] = [dfs[player_id][stat].mean()]
            my_dict[players_dict[player_id]] = players_stats[player_id]
    
    cat_stat_df = pd.DataFrame(my_dict)
    cat_stat_df.set_index("Category",inplace=True)

    #Building table 2 winners per category
    winners = []
    for stat in stats_of_interest:
        winners.append(cat_stat_df.loc[stat].idxmax())
    cat_winner_df  = pd.DataFrame({
        "Category":stats_of_interest,
        "Winner":winners
    })
    cat_winner_df.set_index("Category",inplace=True)

    #Building table 3 win count
    players = []
    winners = list(cat_winner_df["Winner"])
    win_count = []
    for player_id in players_dict:
        players.append(players_dict[player_id])
        win_count.append(winners.count(players_dict[player_id]))
    cat_win_count_df = pd.DataFrame({
        "Player":players,
        "Category_wins":win_count
    })
    cat_win_count_df.set_index("Player",inplace=True)
    cat_win_count_df.sort_values("Category_wins",inplace=True,ascending=False)

    return cat_stat_df,cat_winner_df,cat_win_count_df


    
##dfs, players_dict = read_from_results(path1, stats_of_interest)
#Prenormalization category comparison averages 

##cat_stat_df, cat_winner_df,cat_win_count_df= compare_stats_last_games(dfs,players_dict,stats_of_interest)
"""
print("\nANALYZING CATEGORIES SEASON AVERAGE\n")
print(cat_stat_df)
print("\n")
print(cat_winner_df)
print("\n")
print(cat_win_count_df)

number = 5
cat_stat_df5, cat_winner_df5,cat_win_count_df5 = compare_stats_last_games(dfs,players_dict,stats_of_interest,number)
print(f"\nANALYZING CATEGORIES LAST {number} GAMES\n")
print(cat_stat_df5)
print("\n")
print(cat_winner_df5)
print("\n")
print(cat_win_count_df5)

number = 10 
cat_stat_df10, cat_winner_df10,cat_win_count_df10 = compare_stats_last_games(dfs,players_dict,stats_of_interest,number)
print(f"\nANALYZING CATEGORIES LAST {number} GAMES\n")
print(cat_stat_df10)
print("\n")
print(cat_winner_df10)
print("\n")
print(cat_win_count_df10)
"""

#Beyond this point all dataframes become normalized to analyze as a whole.
##normalized_dfs = normalize_stats_sum(dfs,players_dict,stats_of_interest)
##contrib_df, contrib_winner_df = compare_player_contribution(normalized_dfs,players_dict,stats_of_interest)

"""
print(contrib_df)
print("\n")
print(contrib_winner_df)


print("\n"*2)
print("*"*10+"ANALYSIS COMPLETE IN DEVELOPMENT"+"*"*10)
"""

def run_this_development():
    dfs, players_dict = read_from_results(path1, stats_of_interest)
    cat_stat_df, cat_winner_df,cat_win_count_df= compare_stats_last_games(dfs,players_dict,stats_of_interest)
    cat_stat_df5, cat_winner_df5,cat_win_count_df5 = compare_stats_last_games(dfs,players_dict,stats_of_interest,5)
    cat_stat_df10, cat_winner_df10, cat_win_count_df10 = compare_stats_last_games(dfs,players_dict,stats_of_interest,10)
    normalized_dfs = normalize_stats_sum(dfs,players_dict,stats_of_interest)
    contrib_df, contrib_winner_df = compare_player_contribution(normalized_dfs,players_dict,stats_of_interest)
    return cat_stat_df, cat_winner_df,cat_win_count_df, cat_stat_df5, cat_winner_df5,cat_win_count_df5,cat_stat_df10, cat_winner_df10, cat_win_count_df10,contrib_df, contrib_winner_df