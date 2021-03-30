import pandas as pd
import numpy as np
import time

start = time.time()

# Import datasets
train = pd.read_csv('lebron_train.csv')
test = pd.read_csv('lebron_test.csv')

colNames = list(train)
colNames.pop(0)
colNames.pop(0)

# Target variable, winning or losing
train_result = train['Result'].tolist()
test_result = test['Result'].tolist()

# Predict which individual variable is the best predictor of Lebron winning
def singleVariable(df, colNames, result):
    bestStat = ''
    bestVal = 0
    for cn in colNames:
        stat = df[cn].tolist()
        wins = []
        losses = []
        for i, v in enumerate(stat):
            if v == v: # eliminates nan values
                if result[i][0] == 'W': wins.append(v)
                else: losses.append(v)
        winMean = np.mean(wins) / (np.mean(wins) + np.mean(losses))
        loseMean = 1 - winMean
        print(f'{cn:4}: Mean of wins: {winMean:.4f}, Mean of losses: {loseMean:.4f}')

        if winMean > bestVal:
            bestStat = cn
            bestVal = winMean
    
    print(f'The best individual statistic is {bestStat}, with a normalize value of {bestVal:.4f}')
    return bestStat

# Predict which two variables combined best predict Lebron winning
def twoVariables(df, colNames, result):
    bestStat = ''
    bestVal = 0
    for cn1 in colNames:
        for cn2 in colNames:
            if cn1 != cn2:
                stat1 = df[cn1].tolist()
                stat2 = df[cn2].tolist()
                wins = []
                losses = []
                for i, v in enumerate(stat1):
                    if v == v and stat2[i] == stat2[i]: # eliminates nan values
                        if result[i][0] == 'W': wins.append([v, stat2[i]])
                        else: losses.append([v, stat2[i]])
                winMean = (np.mean(wins[0]) / (np.mean(wins[0]) + np.mean(losses[0])) + np.mean(wins[1]) / (np.mean(wins[1]) + np.mean(losses[1]))) / 2
                loseMean = 1 - winMean
                print(f'{cn1:4}, {cn2:4}: Mean of wins: {winMean:.4f}, Mean of losses: {loseMean:.4f}')

        if 1 > winMean > bestVal:
            bestStat = [cn1, cn2]
            bestVal = winMean
    
    print(f'The best individual statistic is {bestStat}, with a normalize value of {bestVal:.4f}')
    return bestStat

singleVariable(train, colNames, train_result)
twoVariables(train, colNames, train_result)

end = time.time()
print("Elapsed time: " + str(end-start))
