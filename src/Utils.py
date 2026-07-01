#Unbox is used to extract cards from a given hand
def Unbox(ls):
  i = ls[0]
  j = ls[1]
  k = ls[2]

  return i,j,k
#Find is used to find the number of occurences of a card in the deck
def Find(i,j,k):
  ni = CardCount[i]
  nj = CardCount[j]
  nk = CardCount[k]

  return ni,nj,nk

