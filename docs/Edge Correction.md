# Edge Correction

## Problem

<details>
  <Summary>
    This section contains the reason what problem does this document exactly address
  </Summary>

  As we have discussed in the Mathematical Model, the problem arises from how our cards blocks our opponents from attaining certain colours. Due to this, we must     find what colours have been blocked for our cards and whether for the opponents hands does it even affect it 

    In our previous document we took,
    Opponent's hand: [2,5,6]
    Our hand: [5,5,5]

    Here we clearly block the 5 cards and therefore, only colour is possible for our opponent's hand

  However,
  
    Opponent's Hand: [3,7,8]
    Our hand: [6,9,10]
    
    Here there is no blocking effect seen.

  Even the amount colours are blocked depends on our Suit hand, 
  Take for example,

    Opponent hand: [4,5,9]
    Our Hand: [4(spades) ,5(spades) ,9(spades)]
    In this case the opponent can get 3 colours: clubs, diamond, hearts
    
    If Our hand is: [4(clubs),5(spades),9(spades)]
    In this case, the opponent can get 2 colours: diamonds, hearts

    If our hand is: [4(spades),5(clubs),9(hearts)]
    In this case, the opponent can get only a single colour: hearts

  In each case the different card with different suits change different colours,
  
  But they only block it, if the opponents hands have the same cards as ours

    Take for example,
    Opponent Hand:[4,5,10]
    Our Hand: [4(spades),5(clubs),9(hearts)]

    Our opponent can have 2 colours!
    Since the 9 of hearts do not block anything for our opponent.

  **Thus, our result changes on this:**
  - How many cards of our opponent is affected by our cards?
  - For those cards, what colours are eliminated.

  *Note: The reason we have taken such a long detour is to find Colour probability, for which we need the number of Colours possible*
</details>

## Code
<details>
  <summary>
    This section covers how the code covers the problem
  </summary>

  For reference, I have pasted screenshots of the code for you to crossreference,

  ![Data](teen-pati-probability-model/images/Data.png)

  For reference, what each variable means here is as follows,

  row - Opponents hand, Passes in data

  ls_SortedRow - The distinct cards in the opponents hand (If hand is [K,K,Q] ls_SortedRow is [K,Q], stores what are the cards of the opponent

  ls_Row - This stores the which position of the cards match in ls_SortedRow (For example, 1st card and 2nd card or only 3rd card)

  ls_SuitHand - This stores what colours have been blocked.

  ![Distinct Row](teen-pati-probability-model/images/duplicate.png)

  This for loop runs through the opponents Hands and finds the distinct cards that are present in the opponents hands, (this allows us the comparision process that occurs later to proceed more smoothly)

  ![Find](teen-pati-probability-model/images/match.png)

  This for loop compares the sorted opponent hand and our hand and stores the position where OUR cards match

  ![End](teen-pati-probability-model/images/free.png)

  This code finds what suits get blocked by our hand and returns the free suits, <br>
  4 represents the total number of seats and len(ls_SuitHand) represents the number of blocked suits
  
</details>


