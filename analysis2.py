
import pandas as pd

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
        if stat != "Tov":
            winners.append(cat_stat_df.loc[stat].idxmax())
        else:
            winners.append(cat_stat_df.loc[stat].idxmin())
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