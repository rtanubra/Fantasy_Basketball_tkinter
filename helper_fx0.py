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