# MachineLebron
Machine learning technique's applied to the playing career of the GOAT, Lebron Raymone James Sr.

a.) Our project will attempt to determine which of Lebron James’ game statistics is the best predictor of him winning games. We will determine which individual statistic, which pair, and which trio is the best predictor. For example, we may determine that True Shooting Percentage is the best individual predictor but Assists and Points Scored is the best pair predictor. We will then take some of the best predictors and will use Logistic Regression to create a model and will test our model’s accuracy against the current season 2020-2021.
b.) The target variable will be if Lebron James won (W) or lost (L) the game. We will use data from the previous 10 NBA seasons, starting in the 2011-2012 season (Not counting the current season). Lebron has played 638 NBA regular season games in that span. Therefore, our project will include 638 items of data. Our test data will be this current season (which is 37 games and counting). Our variables will include the following (taken from https://www.basketball-reference.com/players/j/jamesle01.html). We will have a total of 24 variables.
•	Minutes Played, Personal Fouls
•	Field Goals Made, Field Goals Attempted, Field Goal Percentage
•	Three Pointers Made, Three Pointers Attempted, Three Point Percentage
•	Free Throws Made, Free Throws Attempted, Free Throw Percentage
•	Offensive Rebounds, Defensive Rebounds, Total Rebounds, 
•	Assists, Steals, Blocks, Turnovers, 
•	Points Scored, Game Score, Plus / Minus
•	True Shooting Percentage*, Double-Double*, Triple-Double*
o	These can be computed based on provided data, and are worth investigating as predictors.

c.) This project will focus on using multivariate regression to discern which of Lebron’s statistics best predict the outcomes of his games. Then we will use logistic regression to build a model for predicting the outcome of games based on Lebron’s stats alone. Glenn will be implementing the majority of the multivariate portion and Kyle will implement the majority of the logistic regression portion.
