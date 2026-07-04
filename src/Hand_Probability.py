from src.Utils import *
from src.data import *

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

