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
