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
