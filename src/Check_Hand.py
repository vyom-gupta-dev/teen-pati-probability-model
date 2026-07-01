#Check module to check different hands

from src.utils import Unbox

#Used to check whether the hand is a triple (222, 333etc.)
def CheckTriple(ls):
  i,j,k = Unbox(ls)

  if(i==j and j==k):
    return True
  else:
    return False

#Used to check whether a hand is a sequence (234,345...)
def CheckSeq(ls):
  i,j,k = Unbox(ls)

  if(i-j == 1 and j-k == 1):
    return True
  else:
    return False

#Checks whether the hand is a special sequence (A23)
def CheckSeqAce(ls):
  i,j,k = Unbox(ls)

  if(i == 14 and j == 3 and k ==2):
    return True
  else:
    return False

#Checks whether a hand is a particular kind of pair(552, 775...)
def CheckPairHigh(ls):
  i,j,k = Unbox(ls)

  if(i==j):
    return True
  else:
    return False

#Checks whether a hand is particular kind of pair(522,755...)
def CheckPairLow(ls):
  i,j,k = Unbox(ls)

  if(j==k):
    return True
  else:
    return False

#Checks whether all the cards are different (235, 568...)
def CheckNonPair(ls):
  i,j,k = Unbox(ls)

  if(i != j and j != k):
    return True
  else:
    return False

#Checks whether all the cards have the same suits (Called as a Colour)
def CheckSuit(ls):
  s1,s2,s3 = Unbox(ls)
  if(s1==s2 and s2 ==s3):
    return True
  else:
    return False
