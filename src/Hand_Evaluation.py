#This module is used for storing the procedures for computing the winning, loosing and drawing probabilities for different hands

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
