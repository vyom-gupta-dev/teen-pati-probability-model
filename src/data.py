#This module contains all the data that is required for the Setup module

#Data contains all possible hands
#Each hand is of form [Higher,Middle,Lower]
data = []
for high in range(2, 15):
    for mid in range(2, high + 1):
        for low in range(2, mid + 1):
            data.append([high, mid, low])

#Find numeric Values
CardValues = {
    'A' : 14,
    'K' : 13,
    'Q' : 12,
    'J' : 11
}

#Card Counter
CardCount = {
    14 : 4,
    13 : 4,
    12 : 4,
    11 : 4,
    10 : 4,
    9 : 4,
    8 : 4,
    7 : 4,
    6 : 4,
    5 : 4,
    4 : 4,
    3 : 4,
    2 : 4
}
#Variables that are used later in the main program
Total = 49 #Number of cards after updation
Win = 0    #Winning Probability
Loss = 0    #Losing Probability
Draw = 0    #Drawing Probability
