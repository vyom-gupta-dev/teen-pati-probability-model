# Mathematical Model

## Recap:
<details>
  <summary>
    
    This section is a recap of the essential context for the problem which is also present in the READE file
    
  </summary>

### Problem Statement

Problem Statement:

**FIRST**, You are given your cards,

**THEN**, your opponent gets their cards,

Following the rules of Teen Pati-

A) Find the hands that can beat or lose to your hand,

B) Additionally find the probability of obtaining those cards

*Note: The Cards you posses are not replaced.*

### Situation

Situation:
- 52 Cards
- 13 - Spade
- 13 - Club
- 13 - Heart
- 13 - Diamond
- Aces high, 2's low,

- ACE (A) - 14
- KING (K) - 13
- QUEEN (Q) - 12
- JACK (J) - 11
- 2 - 10 = Respective Value

### Notation:

- Probability of any event = Instances of that Event/ Total Instances
- P(A) Denotes the probability of an event A occuring
- P(A') Denotes the probability of an event A ***NOT*** occuring
- P(A*B) Denotes the probability that both events A and B occur ***together***
- P(A|B) Denotes the probability of an event A occuring, **While B has already occured**
- U denotes the Universal Set, P(U) = 1, **Always**
  
### Mathematical Fundamentals:
This project is based on the following few theorems and axioms of probability theory:
- **Conditional Probability** - It states that to compute the condiitonal probability,

**P(A|B) = P(A*B) / P(B)**

- **Mututally Exclusive Events** Two events A,B are said to be mutually exclusive if,

P(A*B) = 0

If A and B are the only events that Occur in the Universal Set U,

**P(A) + P(B) = 1**

Corollary:

P(A') = 1 - P(A) [P(A*A') = 0]

- **Independent Events** These are 2 events where the occurence of one does not affect the other:

(*For example, the events, If I flip a coin and then roll a dice, the result of one does not affect the other, Thus, these are independent events*)

For an Independent event,

**P(A*B) = P(A) * P(B)**
</details>

---

## Explanation

### Hand Probability - 

<details>
  <summary>
    This section explains the mathematical formulas used in Calc module.
  </summary>
  <br>
  Starting from the deck situation after we have recieved our cards, <br>
  There are 49 cards in the deck (52 - 3 = 49, From the deck of 52 cards, our 3 cards have been removed) <br>
  Additionally, not all the Card Values (Ace,King,Queen, 10,5 etc.) have the same number of cards (May max be 4 or minimum once, depending on our hand) <br>
  <br>
  Fundamentally, the probability of attaining any of these cards at first is, <br>

    P(Obtaining Jack) = No. of Jacks in the deck / 49

  For example,

    Our hand is [J,J,Q]
    Number of Jacks = 4 - 2 = 2 (Removing our Jacks from the deck) 
    Probability of obtaining Jack = 2/49

  Now, building upon this, lets say you want to obtain the probability of obtaining a Jack AND another Queen <br>
  <br>
  This can be mathematically represented as,
    
    Our Hand = [J,J,Q]
    P(J*Q) = P(J) * P(Q|J) [Dervied from, P(A|B) = P(A*B) / P(B)
    That is, 
    P(J) is the probability of obtaining Jack, which is 2/49
    P(Q|J) represents the probability of obtaining Q after obtaining our Jack

  *Note: After we have received our Jack, there are not 49 - 1 = 48 cards left in the deck, therefore, P(Q|J) != P(Q)*

    Thus, P(Q|J) = 3/48 in our example, as in the remining 48 cards there are only 3 Queen (4 - 1 (from our deck))
    We would then condlude that,
    P(J*Q) = (2/49) * (3/48)

  Similiarly, we would conclude,
  
    P(Q*J) = P(Q) * P(J|Q)

    Where,
    P(Q) = 3/49
    P(J|Q) = 2/48

  Our first approach represents this situation: <br>
  I **first get Jack**, and **then Queen**.<br>
  <br>
  Or second approach represents this, <br>
  I **first get Queen**, and **then Jack**. <br>
  <br>
  Now, what would be our final net probability? Simply the addition of both <br>
  **AS**, at the end, we **only require a Jack and a Queen.** <br>
  **The order of receiving does not affect the final state**, Thus, <br>

    Net = P(J*Q) +  P(Q*J)

  *Note: The reason we can directly add is because both events are mutually exclusive, or there is no possibility where BOTH occur at the same time (I receive Jack first AND Queen first), clearly that is a logical contradiction and thus, such an event is impossible.* <br>
  <br>
  Surprisingly, both the cases give the same numerical value: 6/2352 <br>
  Thus, we can also write this as, simply, <br>

    Net = 2 * P(J) * P(Q|J) OR Net = 2 * P(Q) * P(J|Q)

  The reason of this symmetry is becase the **end state is the same**, What changed was the direction of reaching them.

    For 1 Queen and 1 Jack,
    We can get: QJ 
    OR: JQ

    Total possibilities = 2! = 2.
    See topic on Arrangements, as to why this is the case.

  Thus, let us say for three cards,

    Hand = [A,A,A]

    Probability of finding KQJ is,
    Net = (3!) * P(K) * P(Q|K) * P(J|(Q|K))

    Or for KKA,
    Net = (3!/2!) * P(K) * P(K|K) * P(A|(K|K))

    And for JJJ,
    Net = (3!/3!) * P(J) * P(J|J) * P(J|(J|J))

  Thus, by the use of Arrangements and Conditional Probability, we have been able to derive the formulaes for the various Hand types that are possible (Excluding Suit). <br>
  These formulas have been exactly applied in the Calc.py module in the src folder for exactly the same folder.
</details>

### Suit Probability

<details>
  <summary>
    This section deals with obtaining the probability of a hand being coloured [ColourWeight()]
  </summary>

  As explained in the README ideas, Instead treating every possible suit arrangement as a unique hand, we separate the rank configuration from the suit configuration and treat "being a Colour" as an independent state evaluated afterwards.

  The maths behind this idea is as follows,

    P(Hand*Suit) = P(Hand|Suit) * P(Suit)
    Where P(Hand|Suit) represents the probability of obtaining the hand for a given suit (As discussed in Hand Porbability)
    and P(Suit*Hand) represents the probability of obtaining that particular hand in that particular condition of whether it is not a colour

  Even within the different possiblities of suit hands possibles (Like [Club,Club,Spade] or [Spade,Heart,Club] which are just a few examples]

  We are only intrested in one special set - Colour = {[Club,Club,Club] , [Spade,Spade,Spade] , [Diamond,Diamond,Diamond] , [Heart,Heart,Heart]}

  This is because we only care about one state - That is, all the suits are of the same type which constitutes a colour, all the remaining combinations are irrelevant to us. 

  Thus, P(Suit*Hand) is simply

    P(Suit) = P(Colour) if we want the hand to be a colour
    P(Suit) = P'(Colour) if we DO NOT want it to be a colour, 

    Where P'(Colour) = 1 - P(Colour)

  Now to compute P(suit) we must know,
  - What elements in colour are possible to be formed (This is handled in the EdgeCorrections() function that is explored in the doc Edge Correction)
  - What are total possibilities

  For the total possibilities, we extract the total number of cards for each constituent element in the Hand,

  The number of these cards tells us what possible suits that element can have,

    If there are 4 cards of 2 in the deck then the 2 can be:
    A 2 of hearts
    A 2 of diamonds
    A 2 of clubs
    A 2 of spades

    Now if lets say in our hand we have the 3 of spades,
    Then the number of cards of 3 in the deck are: 3,
    3 of clubs
    3 of diamonds
    3 of hearts

  Now the total possibilities is simply the combination of all these suits,

  Which, is simply:

    No. of Suits of Card 1 * No. of Suits for Card 2* No. of Suits for Card 3
    For example:
    We require total suit hand possibilities for [2,5,6]
    While we posses [5(Diamonds),5(Clubs),5(Hearts)]

    So for,
    2 - 4 Cards (All suits)
    6 - 4 cards (All suits)
    5 - 1 card (Only Spades)

    So total possibilities is just = 4*1*4 = 16

  The remaining challenge lies in determining which Colour states are still feasible.

  This is because of how our hand, **Blocks certain colours from being possible**

    Take the same example,
    You might think that there might be 4 colours possible for [2,5,6] since there are 4 cards for 2 and 4 cards for 5,
    But in reality, only one colour is possible - 2 of Spades, 5 of Spades and 6 of Spades.
    The other colours like hearts, diamonds and clubs are blocked because of the cards in our hand.
    Which have been removed from the deck and thus, such colours are impossible to be formed.

  The exact algorithm of how we determine this using code is explored more deeply in the Edge Corrections document.

  The implementation of this feasibility check is contained within EdgeCorrections(), which determines which Colour states remain possible after accounting for the cards removed from the deck.
</details>

---

## Limitations

There are, clearly, many limitations to this project:

- **Order of Distribution**

  This model assumes that our cards are dealt before the opponent's cards. Consequently, our cards are first removed from the deck, altering the remaining card     distribution available to the opponent. If the dealing order changes, the blocking effect changes as well, and the probability model derived in this project is   no longer valid without modification.

- **Multiplayer**

  This model is limited to two players. Extending it to multiple opponents substantially increases the number of possible outcomes and greatly complicates the      probability calculations, requiring a different analytical approach.
  
- **Duplicate Cards**

  The model assumes a standard 52-card deck containing one copy of each card. Variants with duplicated cards require modifying the deck state (CardCount) and the   corresponding probability calculations.
  
- **Cheating**

  The model assumes an unbiased dealer and a fair distribution of cards. It does not account for cheating, card manipulation, or intentional deviations from        random dealing. Under such conditions, the predicted probabilities no longer accurately reflect the game state.

- **Analytical Model**

  This project implements an analytical probability model rather than an exhaustive enumeration of every possible game state. While this significantly reduces      computational complexity, the correctness of the results depends on the validity of the mathematical derivations and assumptions presented throughout the         documentation.
