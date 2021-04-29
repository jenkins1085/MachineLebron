# MachineLebron
Machine learning technique's applied to the playing career of the GOAT, Lebron Raymone James Sr.
* Regression Analysis
* Logistic Regression
* Neural Networks

Data is taken from https://www.basketball-reference.com/players/j/jamesle01.html). Training dataset combines Lebron's seasons from 2003-2004 to 2019-2020. Testing dataset is the current season, 2020-2021. Here is a legend for what each statistic represents.
* Minutes Played (MP), Personal Fouls (PF)
* Field Goals Made (FG), Field Goals Attempted (FGA), Field Goal Percentage (FG%)
* Three Pointers Made (3P), Three Pointers Attempted (3PA), Three Point Percentage (3P%)
* Free Throws Made (FTM), Free Throws Attempted (FTA), Free Throw Percentage (FT%)
* Offensive Rebounds (ORB), Defensive Rebounds (DRB), Total Rebounds (TRB), 
* Assists (AST), Steals (STL), Blocks (BLK), Turnovers (TOV, 
* Points Scored (PTS), Game Score (GmSc), Game outcome (Result)

Description of each file in this repository
* **MachineLebron.ipynb** the Google Colab python notebook containing all of the code, and some line-by-line analysis
* **best_predictors.txt** output from sections 1.3, 1.4, and 1.5 in the python notebook, showing what the best individual, and pair of predictors for each statistic is based on R2 and RMSE values.
* **lebron_test.csv** the testing dataset, containing statistics from Lebron's 2020-2021 season.
* **lebron_train.csv** the training dataset, containing statistics from Lebron's 2003-2004 to 2019-2020 seasons.
* **predict_pts.csv** output from section 1.2, containing the R2 and RMSE scores for each individual, pair, and trio of feature statistics for 'PTS'
* **predict_result.csv** output from section 1.1, containing the R2 and RMSE scores for each individual, pair, and trio of feature statistics for 'Result'
