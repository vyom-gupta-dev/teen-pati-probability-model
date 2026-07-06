#ATTEMPT FOR 2 CARDS + SUITED

#Data is of form: [Lower,Higher]

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

Suit = False
Pair = False
Win_Prob = 0
Loss_Prob = 0
Draw_Prob = 0

#Get Cards

#CARD1's is lower card data
#CARD2'S is higher card data

Card1 = input("Enter the Lower Card you have")
Suit1 = input("Enter your Lower Card's Suit")

Card2 = input("Enter the Higher Card you have")
Suit2 = input("Enter your Higher Card's Suit")

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

#CHECKS
if(Value1 == Value2):
  Pair = True
if(Suit1 == Suit2):
  Suit = True


#EVALUATING PAIRS
if(Pair == True):
  for row in data:
    i = row[0]
    j = row[1]
    ni = CardCount[i]
    nj = CardCount[j]
    #Optimization, pair beats most things, check for only other pairs
    if(i==j):
      if(Value1 < i):
        Loss_Prob += (ni/Total)*((ni - 1)/(Total - 1)) #Usual Formula ONLY
      if(Value1 == i):
        Draw_Prob += (ni/Total)*((ni - 1)/(Total - 1)) #Suits play no role !!VERIFY!!
    Win_Prob = 1 - (Loss_Prob + Draw_Prob)

#!!VERIFY FEELS TOO EASY!!
if(Suit == True):
  for row in data:
    i = row[0]
    j = row[1]
    ni = CardCount[i]
    nj = CardCount[j]



    #Caclulating Losing from Pairs
    if(i==j):
      Loss_Prob += (ni/Total)*((ni - 1)/(Total - 1)) #SAME FORMULA

    #Calculating Losing From Non Pairs, Colours
    if(i!=j):

      #Suits probability
      ni = CardCount[i]
      nj = CardCount[j]
      Determiner = min(ni,nj)

      s = (Determiner)/(ni*nj)

      if(j > Value2):
        Loss_Prob += 2*(ni/Total)*(nj/(Total - 1))*s #Conditions flipped since we are calculating Loss Probability
      if(j == Value2):
        if(i > Value1):
          Loss_Prob += 2*(ni/Total)*(nj/(Total - 1))*s
        if(i == Value1):
          Draw_Prob += 2*(ni/Total)*(nj/(Total - 1))*s
      else:
        continue
  Win_Prob = 1 - (Loss_Prob + Draw_Prob)


#Algo for Non Pairs Non Suited
if(Pair == False and Suit == False):
  for row in data:
    i = row[0] #Lower Card
    j = row[1] #Higher Card

    #Non Suits probability !!VERIFY LOGICAL ACCURACY!!
    ni = CardCount[i]
    nj = CardCount[j]
    Determiner = min(ni,nj)

    s = ((ni*nj) - Determiner)/(ni*nj)

    #Optimization, Non Pairs only beats Non Pairs
    if(i!=j):
      if(j < Value2):
        Win_Prob += 2*(ni/Total)*(nj/(Total - 1))*s #The ONLY CHANGE is 's', that calculates the probability of getting a non suited card depending on what card it is
      if(j == Value2):                              #Like the P(i,j) + P(j,i) problem, the order matters here so direct multiplication
        if(i < Value1):
          Win_Prob += 2*(ni/Total)*(nj/(Total - 1))*s
        if(i == Value1):
          Draw_Prob += 2*(ni/Total)*(nj/(Total - 1))*s
      else:
        continue
  Loss_Prob = 1 - (Win_Prob + Draw_Prob)

print(Pair)
print(Suit)

print("Win:",Win_Prob)
print("Loss:",Loss_Prob)
print("Draw",Draw_Prob)

#SOLVED.
