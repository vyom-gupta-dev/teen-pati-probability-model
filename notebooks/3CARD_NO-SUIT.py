#3 CARDS NO SUIT
import math

#Data is of form [Higher,Middle,Lower]
data = [[2, 2, 2],
        [3, 2, 2], [3, 3, 2], [3, 3, 3],
        [4, 2, 2], [4, 3, 2], [4, 3, 3], [4, 4, 2], [4, 4, 3], [4, 4, 4],
        [5, 2, 2], [5, 3, 2], [5, 3, 3], [5, 4, 2], [5, 4, 3], [5, 4, 4], [5, 5, 2], [5, 5, 3], [5, 5, 4], [5, 5, 5],
        [6, 2, 2], [6, 3, 2], [6, 3, 3], [6, 4, 2], [6, 4, 3], [6, 4, 4], [6, 5, 2], [6, 5, 3], [6, 5, 4], [6, 5, 5], [6, 6, 2], [6, 6, 3], [6, 6, 4], [6, 6, 5], [6, 6, 6],
        [7, 2, 2], [7, 3, 2], [7, 3, 3], [7, 4, 2], [7, 4, 3], [7, 4, 4], [7, 5, 2], [7, 5, 3], [7, 5, 4], [7, 5, 5], [7, 6, 2], [7, 6, 3], [7, 6, 4], [7, 6, 5], [7, 6, 6], [7, 7, 2], [7, 7, 3], [7, 7, 4], [7, 7, 5], [7, 7, 6], [7, 7, 7],
        [8, 2, 2], [8, 3, 2], [8, 3, 3], [8, 4, 2], [8, 4, 3], [8, 4, 4], [8, 5, 2], [8, 5, 3], [8, 5, 4], [8, 5, 5], [8, 6, 2], [8, 6, 3], [8, 6, 4], [8, 6, 5], [8, 6, 6], [8, 7, 2], [8, 7, 3], [8, 7, 4], [8, 7, 5], [8, 7, 6], [8, 7, 7], [8, 8, 2], [8, 8, 3], [8, 8, 4], [8, 8, 5], [8, 8, 6], [8, 8, 7], [8, 8, 8],
        [9, 2, 2], [9, 3, 2], [9, 3, 3], [9, 4, 2], [9, 4, 3], [9, 4, 4], [9, 5, 2], [9, 5, 3], [9, 5, 4], [9, 5, 5], [9, 6, 2], [9, 6, 3], [9, 6, 4], [9, 6, 5], [9, 6, 6], [9, 7, 2], [9, 7, 3], [9, 7, 4], [9, 7, 5], [9, 7, 6], [9, 7, 7], [9, 8, 2], [9, 8, 3], [9, 8, 4], [9, 8, 5], [9, 8, 6], [9, 8, 7], [9, 8, 8], [9, 9, 2], [9, 9, 3], [9, 9, 4], [9, 9, 5], [9, 9, 6], [9, 9, 7], [9, 9, 8], [9, 9, 9],
        [10, 2, 2], [10, 3, 2], [10, 3, 3], [10, 4, 2], [10, 4, 3], [10, 4, 4], [10, 5, 2], [10, 5, 3], [10, 5, 4], [10, 5, 5], [10, 6, 2], [10, 6, 3], [10, 6, 4], [10, 6, 5], [10, 6, 6], [10, 7, 2], [10, 7, 3], [10, 7, 4], [10, 7, 5], [10, 7, 6], [10, 7, 7], [10, 8, 2], [10, 8, 3], [10, 8, 4], [10, 8, 5], [10, 8, 6], [10, 8, 7], [10, 8, 8], [10, 9, 2], [10, 9, 3], [10, 9, 4], [10, 9, 5], [10, 9, 6], [10, 9, 7], [10, 9, 8], [10, 9, 9], [10, 10, 2], [10, 10, 3], [10, 10, 4], [10, 10, 5], [10, 10, 6], [10, 10, 7], [10, 10, 8], [10, 10, 9], [10, 10, 10],
        [11, 2, 2], [11, 3, 2], [11, 3, 3], [11, 4, 2], [11, 4, 3], [11, 4, 4], [11, 5, 2], [11, 5, 3], [11, 5, 4], [11, 5, 5], [11, 6, 2], [11, 6, 3], [11, 6, 4], [11, 6, 5], [11, 6, 6], [11, 7, 2], [11, 7, 3], [11, 7, 4], [11, 7, 5], [11, 7, 6], [11, 7, 7], [11, 8, 2], [11, 8, 3], [11, 8, 4], [11, 8, 5], [11, 8, 6], [11, 8, 7], [11, 8, 8], [11, 9, 2], [11, 9, 3], [11, 9, 4], [11, 9, 5], [11, 9, 6], [11, 9, 7], [11, 9, 8], [11, 9, 9], [11, 10, 2], [11, 10, 3], [11, 10, 4], [11, 10, 5], [11, 10, 6], [11, 10, 7], [11, 10, 8], [11, 10, 9], [11, 10, 10], [11, 11, 2], [11, 11, 3], [11, 11, 4], [11, 11, 5], [11, 11, 6], [11, 11, 7], [11, 11, 8], [11, 11, 9], [11, 11, 10], [11, 11, 11],
        [12, 2, 2], [12, 3, 2], [12, 3, 3], [12, 4, 2], [12, 4, 3], [12, 4, 4], [12, 5, 2], [12, 5, 3], [12, 5, 4], [12, 5, 5], [12, 6, 2], [12, 6, 3], [12, 6, 4], [12, 6, 5], [12, 6, 6], [12, 7, 2], [12, 7, 3], [12, 7, 4], [12, 7, 5], [12, 7, 6], [12, 7, 7], [12, 8, 2], [12, 8, 3], [12, 8, 4], [12, 8, 5], [12, 8, 6], [12, 8, 7], [12, 8, 8], [12, 9, 2], [12, 9, 3], [12, 9, 4], [12, 9, 5], [12, 9, 6], [12, 9, 7], [12, 9, 8], [12, 9, 9], [12, 10, 2], [12, 10, 3], [12, 10, 4], [12, 10, 5], [12, 10, 6], [12, 10, 7], [12, 10, 8], [12, 10, 9], [12, 10, 10], [12, 11, 2], [12, 11, 3], [12, 11, 4], [12, 11, 5], [12, 11, 6], [12, 11, 7], [12, 11, 8], [12, 11, 9], [12, 11, 10], [12, 11, 11], [12, 12, 2], [12, 12, 3], [12, 12, 4], [12, 12, 5], [12, 12, 6], [12, 12, 7], [12, 12, 8], [12, 12, 9], [12, 12, 10], [12, 12, 11], [12, 12, 12],
        [13, 2, 2], [13, 3, 2], [13, 3, 3], [13, 4, 2], [13, 4, 3], [13, 4, 4], [13, 5, 2], [13, 5, 3], [13, 5, 4], [13, 5, 5], [13, 6, 2], [13, 6, 3], [13, 6, 4], [13, 6, 5], [13, 6, 6], [13, 7, 2], [13, 7, 3], [13, 7, 4], [13, 7, 5], [13, 7, 6], [13, 7, 7], [13, 8, 2], [13, 8, 3], [13, 8, 4], [13, 8, 5], [13, 8, 6], [13, 8, 7], [13, 8, 8], [13, 9, 2], [13, 9, 3], [13, 9, 4], [13, 9, 5], [13, 9, 6], [13, 9, 7], [13, 9, 8], [13, 9, 9], [13, 10, 2], [13, 10, 3], [13, 10, 4], [13, 10, 5], [13, 10, 6], [13, 10, 7], [13, 10, 8], [13, 10, 9], [13, 10, 10], [13, 11, 2], [13, 11, 3], [13, 11, 4], [13, 11, 5], [13, 11, 6], [13, 11, 7], [13, 11, 8], [13, 11, 9], [13, 11, 10], [13, 11, 11], [13, 12, 2], [13, 12, 3], [13, 12, 4], [13, 12, 5], [13, 12, 6], [13, 12, 7], [13, 12, 8], [13, 12, 9], [13, 12, 10], [13, 12, 11], [13, 12, 12], [13, 13, 2], [13, 13, 3], [13, 13, 4], [13, 13, 5], [13, 13, 6], [13, 13, 7], [13, 13, 8], [13, 13, 9], [13, 13, 10], [13, 13, 11], [13, 13, 12], [13, 13, 13],
        [14, 2, 2], [14, 3, 2], [14, 3, 3], [14, 4, 2], [14, 4, 3], [14, 4, 4], [14, 5, 2], [14, 5, 3], [14, 5, 4], [14, 5, 5], [14, 6, 2], [14, 6, 3], [14, 6, 4], [14, 6, 5], [14, 6, 6], [14, 7, 2], [14, 7, 3], [14, 7, 4], [14, 7, 5], [14, 7, 6], [14, 7, 7], [14, 8, 2], [14, 8, 3], [14, 8, 4], [14, 8, 5], [14, 8, 6], [14, 8, 7], [14, 8, 8], [14, 9, 2], [14, 9, 3], [14, 9, 4], [14, 9, 5], [14, 9, 6], [14, 9, 7], [14, 9, 8], [14, 9, 9], [14, 10, 2], [14, 10, 3], [14, 10, 4], [14, 10, 5], [14, 10, 6], [14, 10, 7], [14, 10, 8], [14, 10, 9], [14, 10, 10], [14, 11, 2], [14, 11, 3], [14, 11, 4], [14, 11, 5], [14, 11, 6], [14, 11, 7], [14, 11, 8], [14, 11, 9], [14, 11, 10], [14, 11, 11], [14, 12, 2], [14, 12, 3], [14, 12, 4], [14, 12, 5], [14, 12, 6], [14, 12, 7], [14, 12, 8], [14, 12, 9], [14, 12, 10], [14, 12, 11], [14, 12, 12], [14, 13, 2], [14, 13, 3], [14, 13, 4], [14, 13, 5], [14, 13, 6], [14, 13, 7], [14, 13, 8], [14, 13, 9], [14, 13, 10], [14, 13, 11], [14, 13, 12], [14, 13, 13], [14, 14, 2], [14, 14, 3], [14, 14, 4], [14, 14, 5], [14, 14, 6], [14, 14, 7], [14, 14, 8], [14, 14, 9], [14, 14, 10], [14, 14, 11], [14, 14, 12], [14, 14, 13], [14, 14, 14]]

#Making Data
#for i in range (2,15):
  #for j in range (2,i+1):
    #for k in range (2,j+1):
      #row = [i,j,k]
      #data.append(row)

Triple = False
Sequence = False
Pair = False

TripleVal = 0
SeqVal = 0
PairVal = 0
Kicker = 0

Win_Prob = 0
Draw_Prob = 0
Loss_Prob = 0

#Inputting Cards
High = input("Enter your highest Card")
Mid = input("Enter your 2nd highest Card")
Low = input("Enter your 3rd highest card")

#Find numeric Values
CardValues = {
    'A' : 14,
    'K' : 13,
    'Q' : 12,
    'J' : 11
}

#Getting Card Values
if(High.isdigit() == True):
  HighVal = int(High)
else:
  HighVal = CardValues[High]

if(Mid.isdigit() == True):
  MidVal = int(Mid)
else:
  MidVal = CardValues[Mid]

if(Low.isdigit() == True):
  LowVal = int(Low)
else:
  LowVal = CardValues[Low]

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
#Update
CardCount[HighVal] -= 1
CardCount[MidVal] -= 1
CardCount[LowVal] -= 1
Total = 49

print(High,": ",HighVal)
print(Mid,": ",MidVal)
print(Low,": ",LowVal)
print(CardCount)

#Checks
if(HighVal == MidVal and MidVal == LowVal):
  Triple = True
  TripleVal = HighVal
elif(((HighVal-MidVal) == 1 and (MidVal - LowVal) == 1)):
  Sequence = True
  SeqVal = LowVal
elif(HighVal == 14 and MidVal == 3 and LowVal == 2):
  Sequence = True
  SeqVal = 1
elif(HighVal == MidVal):
  Pair = True
  PairVal = MidVal
  Kicker = LowVal
elif(MidVal == LowVal):
  Pair = True
  PairVal = MidVal
  Kicker = HighVal

print("Triple:",Triple,":",TripleVal)
print("Sequence:",Sequence,":",SeqVal)
print("Pair:",Pair,":",PairVal)
print("Kicker: ",Kicker)

#Probability Calculation


#Triple Algo
if(Triple == True):
  for row in data:
    i = row[0]
    j = row[1]
    k = row[2]

    ni = CardCount[i]
    nj = CardCount[j]
    nk = CardCount[k]

    if(i == j and j == k):
      if(i > TripleVal):
        Loss_Prob += (ni/Total)*((ni-1)/(Total-1))*((ni-2)/(Total-2)) #Pretty Standard
    else:
      continue
  Win_Prob = 1 - Loss_Prob

elif(Sequence == True):
    for row in data:
      i = row[0]
      j = row[1]
      k = row[2]

      ni = CardCount[i]
      nj = CardCount[j]
      nk = CardCount[k]
      #Check for Triple
      if(i == j and j == k):
        Loss_Prob += (ni/Total)*((ni-1)/(Total-1))*((ni-2)/(Total-2)) #Pretty Standard (Permutations are 3!/3!)
      #Check for Sequence
      elif(((i-j) == 1 and (j-k) == 1)):
        if(SeqVal < k):
          Loss_Prob += 6*((ni/Total)*(nj/(Total-1))*(nk/(Total-2))) #Why 6? Cause the order of distribution can be, 3!
        elif(SeqVal == k):
          Draw_Prob += 6*((ni/Total)*(nj/(Total-1))*(nk/(Total-2)))
      elif(i == 14 and j == 3 and k == 2):
        if(SeqVal == 1):
          Draw_Prob += 6*((ni/Total)*(nj/(Total-1))*(nk/(Total-2)))

    Win_Prob = 1 - (Loss_Prob + Draw_Prob)

elif(Pair == True):
  for row in data:
    i = row[0]
    j = row[1]
    k = row[2]

    ni = CardCount[i]
    nj = CardCount[j]
    nk = CardCount[k]
    #Check for Triple
    if(i == j and j == k):
      Loss_Prob += (ni/Total)*((ni-1)/(Total-1))*((ni-2)/(Total-2))
    #Check for Sequence
    elif((i-j) == 1 and (j-k) == 1) or (i == 14 and j == 3 and k == 2):
      Loss_Prob += 6*((ni/Total)*(nj/(Total-1))*(nk/(Total-2)))

    #Check for Other Pairs
    elif(i == j): #Pairs are weird
      if(PairVal < i):
        Loss_Prob += 3*((ni/Total)*((ni-1)/(Total-1))*(nk/(Total-2)))
      elif(PairVal == i):
        if(k > Kicker):
          Loss_Prob += 3*((ni/Total)*((ni-1)/(Total-1))*(nk/(Total-2))) #Arrangements: 3!/2!
        elif(k == Kicker):
          Draw_Prob += 3*((ni/Total)*((ni-1)/(Total-1))*(nk/(Total-2)))
    elif(j == k): #The disadvantage of my data
      if(PairVal < j):
        Loss_Prob += 3*((ni/Total)*(nj/(Total-1))*((nj-1)/(Total-2)))
      elif(PairVal == j):
        if(i > Kicker):
          Loss_Prob += 3*((ni/Total)*(nj/(Total-1))*((nj-1)/(Total-2))) #Arrangements: 3!/2!
        elif(i == Kicker):
          Draw_Prob += 3*((ni/Total)*(nj/(Total-1))*((nj-1)/(Total-2)))
  Win_Prob = 1 - (Loss_Prob + Draw_Prob)

else:
  for row in data:
    i = row[0]
    j = row[1]
    k = row[2]

    ni = CardCount[i]
    nj = CardCount[j]
    nk = CardCount[k]

    #Check for Triple
    if(i == j and j == k):
      Loss_Prob += (ni/Total)*((ni-1)/(Total-1))*((ni-2)/(Total-2))
    #Check for Sequence
    elif(((i-j) == 1 and (j-k) == 1) or (i == 14 and j == 3 and k == 2)):
      Loss_Prob += 6*((ni/Total)*(nj/(Total-1))*(nk/(Total-2)))
    #Check for Pairs
    elif(i == j):
      Loss_Prob += 3*((ni/Total)*((ni-1)/(Total-1))*(nk/(Total-2)))
    elif(j==k):
      Loss_Prob += 3*((ni/Total)*(nj/(Total-1))*((nj-1)/(Total-2)))

    #Check for Non Pairs
    else:
      if(i>HighVal):
        Loss_Prob += 6*((ni/Total)*(nj/(Total-1))*(nk/(Total-2)))
      elif(i == HighVal):
        if(j > MidVal):
          Loss_Prob += 6*((ni/Total)*(nj/(Total-1))*(nk/(Total-2)))
        elif(j == MidVal):
          if(k > LowVal):
            Loss_Prob += 6*((ni/Total)*(nj/(Total-1))*(nk/(Total-2)))
          elif(k == LowVal):
            Draw_Prob += 6*((ni/Total)*(nj/(Total-1))*(nk/(Total-2)))
  Win_Prob = 1 - (Loss_Prob + Draw_Prob)






print("Win:",Win_Prob)
print("Draw:",Draw_Prob)
print("Loss:",Loss_Prob)

