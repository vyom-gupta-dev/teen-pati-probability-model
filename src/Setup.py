from src.Utils import *
from src.Check import *
from src.Hand_Evaluation import *

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

#This is where the program begins
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

  Hand = [Card1,Card2,Card3]
  SuitHand = [Suit1,Suit2,Suit3]

  Get_Hands(Hand,SuitHand)

#Finding Values of the Cards
def Get_Hands(Hand,SuitHand):
  Card1,Card2,Card3 = Unbox(Hand)
  Suit1,Suit2,Suit3 = Unbox(SuitHand)

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

  #Obtains Hand
  Hand = [Value1,Value2,Value3]
  #Sorts Hand
  Hand.sort(reverse = True)

  print("\nSUMMARY:")
  print("1st Card:",Card1,"|Suit:",Suit1,"|Value:",Value1)
  print("2nd Card:",Card2,"|Suit:",Suit2,"|Value:",Value2)
  print("3rd Card:",Card3,"|Suit:",Suit3,"|Value:",Value3,"\n")

  State(Hand)
  Compare(Hand,SuitHand)

  return Hand

#Updates the Deck
def State(ls):
  #Obtain Highm Middle and Low again
  High,Mid,Low = Unbox(ls)
  #Updates Deck
  CardCount[High] -= 1
  CardCount[Mid] -= 1
  CardCount[Low] -= 1

#Classifies what kind of Hand it is
def Compare(Hand,SuitHand):
  Colour = False

  HighVal,MidVal,LowVal = Unbox(Hand)

  TripleVal = 0
  SeqVal = 0
  PairVal = 0
  Kicker = 0

  Colour = CheckSuit(SuitHand)

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
    Sequence_Probability(SeqVal,Colour,Hand,SuitHand)

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

  elif(CheckNonPair(Hand)):
    print("-> Non-Pair")
    print("-> Colour? :", Colour)
    NonPair_Probability(Colour,Hand,SuitHand)

  else:
    print("DETECTING ERROR!")
    print("ENDING PROGRAM...")
    exit()
    
Start()
