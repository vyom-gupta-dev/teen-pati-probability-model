#Proper Attempt for 2 CARD NO SUIT
import math

data = [
[2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9], [2, 10], [2, 11], [2, 12], [2, 13], [2, 14],
[3, 3], [3, 4], [3, 5], [3, 6], [3, 7], [3, 8], [3, 9], [3, 10], [3, 11], [3, 12], [3, 13], [3, 14],
[4, 4], [4, 5], [4, 6], [4, 7], [4, 8], [4, 9], [4, 10], [4, 11], [4, 12], [4, 13], [4, 14],
[5, 5], [5, 6], [5, 7], [5, 8], [5, 9], [5, 10], [5, 11], [5, 12], [5, 13], [5, 14],
[6, 6], [6, 7], [6, 8], [6, 9], [6, 10], [6, 11], [6, 12], [6, 13], [6, 14],
[7, 7], [7, 8], [7, 9], [7, 10], [7, 11], [7, 12], [7, 13], [7, 14],
[8, 8], [8, 9], [8, 10], [8, 11], [8, 12], [8, 13], [8, 14],
[9, 9], [9, 10], [9, 11], [9, 12], [9, 13], [9, 14],
[10, 10], [10, 11], [10, 12], [10, 13], [10, 14],
[11, 11], [11, 12], [11, 13], [11, 14],
[12, 12], [12, 13], [12, 14],
[13, 13], [13, 14],
[14, 14]
         ]
data2 = [
[2,2],[2,3],[2,4],
[3,3],[3,4],
[4,4]
          ]
Pair = False
Win_Prob = 0
Loss_Prob = 0
Draw_Prob = 0

#Get Cards
Card1 = input("Enter the Card you have")
Card2 = input("Enter the Card you have")
#Find numeric Values
CardValues = {
    'A' : 14,
    'K' : 13,
    'Q' : 12,
    'J' : 11
}

if(Card1.isdigit() == True):
  Value1 = int(Card1)
else:
  Value1 = CardValues[Card1]

if(Card2.isdigit() == True):
  Value2 = int(Card2)
else:
  Value2 = CardValues[Card2]

print(Card1, ":", Value1)
print(Card2, ":", Value2)

#NOTE CARD1, CARD 2 ARE STRINGS
#PLEASE USE VALUE1, VALUE2
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

#Update Cards (Remove your cards)
CardCount[Value1] -= 1
CardCount[Value2] -= 1
Total = 50 #NOTE: 2 CARDS ARE REMOVED !!THIS IS FOR ONLY SAMPLY DATA PLEASE CHANGE LATER BACK TO 52!!

print(CardCount)

# data = []
# Getting Data
# for i in range (2,15):
  # for j in range (i,15):
    # rec = [i,j]
    # data.append(rec)
# print(data)

if(Card1 == Card2):
  Pair = True
else:
  Pair = False

#Algo for paired numbers
if(Pair == True):
  for row in data: #!!PLEASE CHANGE DATA2 TO DATA AFTER TESTING IS DONE!!
    i = row[0]
    j = row[1]

    #Optimization, pair beats most things, check for only other pairs
    if(i==j):
      if(Value1 < i):
        Loss_Prob += ((CardCount[i])/(Total))*((CardCount[i] - 1)/(Total - 1)) #This is basic probability !!VERIFY!!
      if(Value1 == i):
        Draw_Prob += ((CardCount[i])/(Total))*((CardCount[i] - 1)/(Total - 1)) #This is basic probability
  Win_Prob = 1 - (Loss_Prob + Draw_Prob)

#Algo for Non Pairs
else:
  for row in data:
    i = row[0]
    j = row[1]
    #Optimization, Non Pairs only beats Non Pairs
    if(i!=j):
      myMax = max(Value1,Value2)
      myMin = min(Value1,Value2)

      oppMax = max(i,j)
      oppMin = min(i,j)
      if(oppMax < myMax):
        Win_Prob += 2*((CardCount[i])/(Total))*((CardCount[j])/(Total - 1)) #%The order of the cards distributing matters, i first then j is distinct from j first i later%
      if(oppMax == myMax):
        if(oppMin < myMin): #%Program logic at first was wrong since it skipped the Max condition being the same for both cards
          Win_Prob += 2*((CardCount[i])/(Total))*((CardCount[j])/(Total - 1))
        if(oppMin == myMin):
          Draw_Prob += 2*((CardCount[i])/(Total))*((CardCount[j])/(Total - 1))
      else:
        continue
  Loss_Prob = 1 - (Win_Prob + Draw_Prob)

print("Win:",Win_Prob)
print("Loss:",Loss_Prob)
print("Draw",Draw_Prob)




