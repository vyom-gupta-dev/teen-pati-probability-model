#ONE CARD

Card = input("Enter the Card you have")
CardValues = {
    'A' : 14,
    'K' : 13,
    'Q' : 12,
    'J' : 11
}

if(Card.isdigit() == True):
  Value = int(Card)
else:
  Value = CardValues[Card]

print(Card,":",Value)

def Prob(V):
  Win_Prob = (int) (((V - 2)/13) * 100)
  print("Winning Probability:", Win_Prob)

  Draw_Prob = int (100/13)
  print("Drawing Probability:",Draw_Prob)

  Loss_Prob = 100 - (Win_Prob + Draw_Prob)
  print("Loosing Probability:",Loss_Prob)

Prob(Value)
