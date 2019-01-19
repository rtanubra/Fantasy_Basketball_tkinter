APPLICATION GOAL:

The goal of this application is to allow NBA Fantasy GMs to analyze potential players for pickup. Analysis will be broken down in two main ways.

1. Category breakdown across three timelines (season average, last 10 games, last 5 games)
        Method:
            I.Pull game logs for each player of interest
            II.Compute simple descriptive statistics (mean) for each stat category across
            different timelines 

        Rationale:
            9 category leagues require the General Manager to procur the group of players
            that will win the most categories. This simple view will allow you to see 
            which player(s) will be able to win the most categories for you across different
            timelines. 

2. Analysis of the player's contribution to the overall team. 
        
        Method:
            I.normalizes each categorical stat by dividing it with category max obtained by
            the group of players chosen (multiplied by 100)

            II.the score obtained above is then summed across the 9 categories to describe 
            the player's overall contribution to the team on that given game.

            III. These single value scores are then displayed to be analyzed across different
            time frames, namely season average, last 10 games, and last 5 games
       
        Rationale: 
            Some players fill the stat categories across the board while other players are
            specialists. Both types of players will contribute differently to a team. A 
            speacialist can help you put a category out of your enemy's grasp. A board filler
            can help you across different categories. This method will allow you to compare 
            the different types of players using a single datapoint. 

    
DEPENDENCIES AND MUST INSTALLS/SUBSCRIBES:

    MYSPORTSFEEDS: https://www.mysportsfeeds.com/
    
        1. NBA Api key can be obtained for free. 
            This is required to pull game logs for the application.
            
        2. ohmysportsfeedspy 
        https://github.com/MySportsFeeds/mysportsfeeds-python/blob/master/README.md
            A wrapper used to make calls to my sports feeds api much
            easier. Used in this application to pull game logs.
    
    PANDAS & NUMPY
        numpy and pandas are both required to run this application.
        Used to easily work with the data pulled from my sports feeds. 

RUNNING THE APPLICATION:

    on your command prompt run:

        1. navigate to the directory
        
        2. run: python3 tk_frame.py

METHOD:

    0. .gitignore:
        I.create a directory called inputs
        II.create inputs/msf.txt
        III.in the above txt file save 2 lines of information.
            line 1 <mysportsfeeds apikey here>
            line 2 <mysportsfeeds apikey password>
    1. tk_frame
        I. Upon initializing it will pull previously stored analysis to display.
        II. this was done to create the objects that will later be used
        and modified through the different comparisons.
        III. input player names and SUBMIT!
        IV. you can toggle time frames by pressing the 3 time frame buttons.
    
    THE FOLLOWING ARE WHAT TAKES PLACE BEHIND THE SCENES.
    run_me.py ** uses the below to pull information necessary to display in tkinter GUI
    2. pull_game_info1.py
        I.using ohmysportsfeedspy wrapper we pull game logs from mysportsfeeds
        II.working with JSON we create a pandas dataframe to contain
        statistics category breakdown for each player we are analyzing.
    
    3. analysis2.py
        Utilizes each player df to create the following 6 main dataframes
        I. cat_stat_df
            -for each category what is each player's stat score.
            -creates a season average, last 10 games, last 5 games dataframes.
        II. cat_winner_df
            -for each category which player won that category explores 
            across different time frames.
            -creates a season average, last 10 games, last 5 games 
        III. cat_win_count_df
            -for each player, how many categories did the player win.
            -creates a season average, last 10 games, last 5 games
        IV. contrib_df
            -Displays each player's average contribution across time.
            -Displays avg contribution season average, last 10 games,
            last 5 games 
        V. contrib_winner_df
            -for each time frame, displays which player had the 
            highest contribution average.
    
    TKINTER STUFF
    
    4. frame1_category.py
        this houses all the functions that are used to modify tkinter
        frame 1. At present, frame 1 used to display category stats.
    5. frame2_contribution.py
        this houses all the functions that are used to modify tkinter
        frame 2. At present frame 2 is used to display information
        regarding single point contribution.



