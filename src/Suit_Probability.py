#This module contains those functions that are necessary to determine the probability of attaining a Colour (All 3 cards have the same suit)

from src.Utils import *

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
