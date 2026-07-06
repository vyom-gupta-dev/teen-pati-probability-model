#3CARDS + SUITS

import math
Win = 0
Loss = 0
Draw = 0
Total = 49 #A constant that will be used later on

#Check module to check different hands
def Unbox(ls):
  i = ls[0]
  j = ls[1]
  k = ls[2]

  return i,j,k

def CheckTriple(ls):
  i,j,k = Unbox(ls)

  if(i==j and j==k):
    return True
  else:
    return False

def CheckSeq(ls):
  i,j,k = Unbox(ls)

  if(i-j == 1 and j-k == 1):
    return True
  else:
    return False

def CheckSeqAce(ls):
  i,j,k = Unbox(ls)

  if(i == 14 and j == 3 and k ==2):
    return True
  else:
    return False

def CheckPairHigh(ls):
  i,j,k = Unbox(ls)

  if(i==j):
    return True
  else:
    return False

def CheckPairLow(ls):
  i,j,k = Unbox(ls)

  if(j==k):
    return True
  else:
    return False

def CheckNonPair(ls):
  i,j,k = Unbox(ls)

  if(i != j and j != k):
    return True
  else:
    return False

def CheckSuit(ls):
  s1,s2,s3 = Unbox(ls)
  if(s1==s2 and s2 ==s3):
    return True
  else:
    return False

#Calc module is used to calculate probabilities for various cases,
def Find(i,j,k):
  ni = CardCount[i]
  nj = CardCount[j]
  nk = CardCount[k]

  return ni,nj,nk

#When all cards of hand are same
def CalcTriple(ls):

  #Unbox for cards
  i,j,k = Unbox(ls)
  #Find number of cards
  ni,nj,nk = Find(i,j,k)

  #Probability Formula
  Probability = (ni/Total)*((ni-1)/(Total-1))*((ni-2)/(Total-2))

  return Probability

#When j==k and i is the kicker
def CalcPairLow(ls):
  i,j,k = Unbox(ls)
  ni,nj,nk = Find(i,j,k)
  Probability = 3*((ni/Total)*(nj/(Total-1))*((nj-1)/(Total-2)))

  return Probability

#When i == j and k is the kicker
def CalcPairHigh(ls):
  i,j,k = Unbox(ls)
  ni,nj,nk = Find(i,j,k)
  Probability = 3*((ni/Total)*((ni-1)/(Total-1))*(nk/(Total-2)))

  return Probability
#When i!=j!=k
def CalcDiff(ls):
  i,j,k = Unbox(ls)
  ni,nj,nk = Find(i,j,k)
  Probability = 6*((ni/Total)*(nj/(Total-1))*(nk/(Total-2)))

  return Probability

#Master Function
def P(hand):

    if CheckTriple(hand):
        return CalcTriple(hand)

    elif CheckPairHigh(hand):
        return CalcPairHigh(hand)

    elif CheckPairLow(hand):
        return CalcPairLow(hand)

    elif CheckNonPair(hand):
        return CalcDiff(hand)

#Eliminates those suit colours which are not possible because of our hand
def EdgeCorrection(Hand,SuitHand,row):
  ls_row = []
  ls_SuitHand = []
  ls_SortedRow = [] #Sorted Row without duplicates

  for i in row:
    if(i not in ls_SortedRow):
      ls_SortedRow.append(i)
    else:
      continue


  for i in ls_SortedRow:
    for j in range(0,3):
      if (i==Hand[j]):
        ls_row.append(j)

  for i in ls_row:
    if(SuitHand[i] not in ls_SuitHand):
      ls_SuitHand.append(SuitHand[i])
    else:
      continue

  FreeSuits = 4 - len(ls_SuitHand)
  return FreeSuits

#Function to find the probability of obtaining a colour
def ColourWeight(Hand,SuitHand,Row):
  suits = EdgeCorrection(Hand,SuitHand,Row)
  i,j,k = Unbox(Row)
  ni, nj, nk = Find(i,j,k)

  Probability = suits / (ni*nj*nk)
  return Probability

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

print("RUBRIC - VALUE INPUTTING")
print("Press A for Ace")
print("Press K for King")
print("Press Q for Queen")
print("Press J for Jack")
print("For Numbered Card, enter the number \n")

print("RUBRIC - SUIT INPUTTING")
print("Press C for Clubs")
print("Press S for Spades")
print("Press H for Hearts")
print("Press D for Diamonds \n")

print("INPUTS:")


def Start():
  #Inputting required information on the hand
  Card1 = input("Enter first Card: ").upper()
  Suit1 = input("Enter suit for first card: ").upper()

  Card2 = input("Enter second card: ").upper()
  Suit2 = input("Enter suit for second card: ").upper()

  Card3 = input("Enter third card: ").upper()
  Suit3 = input("Enter suit for third card: ").upper()

  #In case of any mistake, the program rests
  if (not Confirm()):
    Start()
    return


  #Finding Values of the Cards
  if(Card1.isdigit() == True):
    Value1 = int(Card1)
  else:
    Value1 = CardValues[Card1]

  if(Card2.isdigit() == True):
    Value2 = int(Card2)
  else:
    Value2 = CardValues[Card2]

  if(Card3.isdigit() == True):
    Value3 = int(Card3)
  else:
    Value3 = CardValues[Card3]

  #Obtains Highest, Middle Most, Lowest Values
  ls = [Value1,Value2,Value3]
  ls.sort()

  High = ls[2]
  Mid = ls[1]
  Low = ls[0]


  print("\nSUMMARY:")
  print("1st Card:",Card1,"|Suit:",Suit1,"|Value:",Value1)
  print("2nd Card:",Card2,"|Suit:",Suit2,"|Value:",Value2)
  print("3rd Card:",Card3,"|Suit:",Suit3,"|Value:",Value3,"\n")

  print("Highest Value: ",High)
  print("Middle Value: ",Mid)
  print("Lowest Value: ",Low,"\n")

  Hand = [High,Mid,Low]
  SuitHand = [Suit1,Suit2,Suit3]

  State(Hand)
  Compare(Hand,SuitHand)

#Updates the Deck
def State(ls):
  #Obtain Highm Middle and Low again
  High,Mid,Low = Unbox(ls)
  #Updates Deck
  CardCount[High] -= 1
  CardCount[Mid] -= 1
  CardCount[Low] -= 1

  print(CardCount,"\n")

#Classifies what kind of Hand it is
def Compare(Hand,SuitHand):
  Colour = False

  HighVal,MidVal,LowVal = Unbox(Hand)

  TripleVal = 0
  SeqVal = 0
  PairVal = 0
  Kicker = 0

  Colour =

  print("TYPE OF HAND")
  if(CheckTriple(Hand)):
    print("-> Triple of",HighVal)
    TripleVal = HighVal
    Triple_Probability(TripleVal)

  elif(CheckSeq(Hand)):
    print("-> Sequence with Value",LowVal)
    print("-> Flush:",Colour)
    SeqVal = LowVal

    Sequence_Probability(SeqVal,Colour,Hand,SuitHand)
  elif(CheckSeqAce(Hand)):
    print("-> Sequence with Value 1")
    print("-> Flush:",Colour)
    SeqVal = 1

    Sequence_Probability(SeqVal,Colour)
  elif(CheckPairLow(Hand)):
    print("-> Pair value is",LowVal)
    print("-> Kicker value ",HighVal)

    PairVal = LowVal
    Kicker = HighVal

    Pair_Probability(PairVal,Kicker,Hand,SuitHand)

  elif(CheckPairHigh(Hand)):
    print("-> Pair value is",HighVal)
    print("-> Kicker value ",LowVal)

    PairVal = HighVal
    Kicker = LowVal

    Pair_Probability(PairVal,Kicker,Hand,SuitHand)

  else:
    print("-> Non-Pair")
    print("-> Colour? :", Colour)
    NonPair_Probability(row,Colour,Hand,SuitHand)

#A Separate Function to Confirm User Input
def Confirm():
  chr = input("\nCONFIRM? (Y/N)").upper()

  if(chr == 'Y'):
    print("Proceeding...\n")
    return True
  elif(chr == 'N'):
    print("Restarting...\n")
    return False
  else:
    print("ERROR! Restarting...\n")
    return False

def Triple_Probability(TripleVal):
  for row in data:
    global Win,Draw,Loss
    i,j,k = Unbox(row)
    #Since i = j = k, Triple value is simply i,
    if(CheckTriple(row)):
      if(i > TripleVal): #If row triple value is higher, then our hand looses
        Loss += P(row)
      elif(i == TripleVal): #If it is equal, then it wins
        Draw += P(row)
  Win = 1 - (Loss + Draw)
  Output(Win,Loss,Draw)

def Sequence_Probability(SeqVal,Colour,Hand,SuitHand):
  global Win,Draw,Loss
  if(Colour):
    for row in data:
      #Triples beat Coloured Flushes
      if(CheckTriple(row)):
        Loss += P(row)
      #Higher Coloured Flushes beat lower Coloured Flushes
      elif(CheckSeq(row)):
        i,j,k = Unbox(row)
        S = ColourWeight(Hand,SuitHand,row)
        if(k > SeqVal):
          Loss += P(row) * S
        elif(k ==SeqVal):
          Draw += P(row) * S
      elif(CheckSeqAce(row)):
        i,j,k = Unbox(row)
        S = ColourWeight(Hand,SuitHand,row)
        if(SeqVal == 1):
          Draw += P(row) * S
  else:
    for row in data:
      #Triples beat Coloured Flushes
      if(CheckTriple(row)):
        Loss += P(row)
      #Higher Coloured Flushes beat lower Coloured Flushes
      elif(CheckSeq(row)):
        i,j,k = Unbox(row)
        S = ColourWeight(Hand,SuitHand,row)
        if(k > SeqVal):
          Loss += P(row) * 1 #Coloured or Non Coloured wins, suit does not matter
        elif(k ==SeqVal):
          Draw += P(row) * (1-S) #Only Uncoloured can Draw
          Loss += P(row) * S
        else:
          Loss += P(row) * S

      elif(CheckSeqAce(row)):
        i,j,k = Unbox(row)
        S = ColourWeight(Hand,SuitHand,row)
        #Always since this represents coloured
        Loss += P(row) * S    #!!IMP!!

        #Dependent on whether we get A23
        if(SeqVal == 1):
          Draw += P(row) * (1-S)
  Win = 1 - (Loss + Draw)
  Output(Win,Loss,Draw)

def Pair_Probability(PairVal,Kicker,Hand,SuitHand):
  global Win, Loss, Draw
  for row in data:
    i,j,k = Unbox(row)

    #Triples beat Pairs
    if(CheckTriple(row)):
      Loss += P(row)
    #All Sequences beat Pairs
    elif(CheckSeq(row) or CheckSeqAce(row)):
      Loss += P(row)

    #Only higher pairs with higher kicker beat our pair
    elif(CheckPairLow(row)): #Pair Value is j,k and kicker is i
      if(j > PairVal):
        Loss += P(row)
      elif(j == PairVal):
        if(i > Kicker):
          Loss += P(row)
        elif(i == Kicker):
          Draw += P(row)

    elif(CheckPairHigh(row)): #Pair Value is i,j and kicker is k
      if(j > PairVal):
        Loss += P(row)
      elif(j == PairVal):
        if(k > Kicker):
          Loss += P(row)
        elif(k == Kicker):
          Draw += P(row)
    #Pairs lose to colours
    elif(CheckNonPair(row)):
      S = ColourWeight(Hand,SuitHand,row)
      Loss += P(row) * S

  Win = 1 - (Loss + Draw)
  Output(Win,Loss,Draw)

def NonPair_Probability(row,Colour,Hand,SuitHand):
  global Loss,Win,Draw

  High,Mid,Low = Unbox(Hand)
  if(Colour):
    for row in data:
      S = ColourWeight(Hand,SuitHand,row)
      i,j,k = Unbox(row)
      #Triples beat Colours
      if(CheckTriple(row)):
        Loss += P(row)
      #All Sequences beat Colours
      elif(CheckSeq(row) or CheckSeqAce(row)):
        Loss += P(row)
      #Only Colours beat Colours
      elif(CheckNonPair(row)):
        if(i > High):
          Loss += P(row) * S
        elif(i == High):
          if(j > Mid):
            Loss += P(row) * S
          elif(j == Mid):
            if(k > Low):
              Loss += P(row) * S
            elif(k == Low):
              Draw += P(row) * S
    Win = 1 - (Loss + Draw)
  else:
    #Only Non Pairs are beaten by our Non Pairs
    for row in data:
      S = ColourWeight(Hand,SuitHand,row)
      i,j,k = Unbox(row)
      if(CheckNonPair(row)):
        if(i < High):
          Win += P(row) * (1-S) #Probability of obtaining Non Pair * Probability of it NOT being a Colour
        elif(i == High):
          if(j < Mid):
            Win += P(row) * (1-S)
          elif(j == Mid):
            if(k < Low):
              Win += P(row) * (1-S)
            elif(k == Low):
              Draw += P(row) * (1-S)
    Loss = 1 - (Win+Draw)
  Output(Win,Loss,Draw)


def Output(Win,Loss,Draw):
  print("\nRESULT")
  print("Probability of Winning: ",Win)
  print("Probability of Drawing: ",Draw)
  print("Probability of Losing: ",Loss)

Start()
