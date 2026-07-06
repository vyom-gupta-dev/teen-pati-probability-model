#2 CARD
import math

Win_Prob = 0
Loss_Prob = 0
Draw_Prob = 0
Positive = 0

def Prob(V,n):
  Win_Prob = (int) (((V - 2)/n) * 100)
  print("Winning Probability:", Win_Prob)

  Draw_Prob = int (100/n)
  print("Drawing Probability:",Draw_Prob)

  Loss_Prob = 100 - (Win_Prob + Draw_Prob)
  print("Loosing Probability:",Loss_Prob)


Card1 = input("Enter the Card you have")
Card2 = input("Enter the Card you have")
n = int(input("Enter number"))

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

FinalVal = max(Value1,Value2)
Total = (n*(n-1))/2
Pairs = n-1
Non_Pairs = ((n-1)*(n-2))/2

print("Total: ",Total)
print("Pairs: ",Pairs)
print("Non_Pairs: ",Non_Pairs)

#Pair
if(Card1 == Card2):
  Win_Prob =  ((((FinalVal - 2) + Non_Pairs) /Total) * 100)
  Draw_Prob = ((1/Total) * 100)
  Loss_Prob = 100 - (Win_Prob + Draw_Prob)

#Non Pair
else:
  for i in range(2,FinalVal):
    Positive += i-2
  Win_Prob =  ((Positive / Total) * 100)
  Draw_Prob =  (((FinalVal-2)/Total) * 100)
  Loss_Prob = 100 - (Win_Prob + Draw_Prob)

print("Winning Probability:", Win_Prob)
print("Drawing Probability:",Draw_Prob)
print("Loosing Probability:",Loss_Prob)
