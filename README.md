# teen-pati-probability-model
An analytical probability engine that has been designed to calculate the probability of winning, losing or drawing in the  Indian Card Game - Teen Patti based on the principles of combinatorics and conditional probability.

This repository contains an analytical probability engine that computes the probabilities of winning, losing, or drawing in a two-player game of Teen Patti using combinatorics and conditional probability.

## What is Teen Patti:
Teen Patti is a card game that is commonly played in India where each player receives three cards or Teen Patti and based on the strength of their hand they decide how much money they decide to bet. Whoever has the highest hand wins. 

## Strength of Hands in Teen Patti:
1. Trail/Trio (Three of a Kind): Three cards of the same rank; Aces are highest

2. Pure Sequence (Straight Flush): Three consecutive cards of the same suit. Example: A-K-Q of diamonds ****

3. Sequence (Straight): Three consecutive cards of mixed suits

4. Color (Flush): Three cards of the same suit, not in sequence. Compare highest card first ***

5. Pair (Two of a Kind): Two cards of the same rank; compare the pair first, then the kicker

6. High Card: None of the above; compare highest → middle → lowest card

## Goal:
This project was designed as a summer project into applying probability theory to the game of Teen Patti.

In real life, professionals try to keep track of cards that may be present in the deck (**Card Counting**) and make intuitive guesses on what the other players may have. However, it is tedious and lengthy to determine an *exact probability* because of the numerous cases one must consider.

However with a systematic procedure to the computation we can work through numerous possibilities by **following the same algorithm and the same fundamental theorems of probability.**

Thus, this project's main goal is to be a probability model designed to find the probability of winning, tying and losing in a round between 2 players by optimizing this calculation based on the *rules of the game* and the *maths behind the probability*.

# Methodology
<details>
<summary>
  
*Note: This section contains the basic axioms of probability and notation that is used in the algorithm, if you are familiar with them, then it is suggestable for you to skip this section*

</summary>
  
## Notation:

- Probability of any event = Instances of that Event/ Total Instances
- P(A) Denotes the probability of an event A occuring
- P(A') Denotes the probability of an event A ***NOT*** occuring
- P(A*B) Denotes the probability that both events A and B occur ***together***
- P(A|B) Denotes the probability of an event A occuring, **While B has already occured**
- U denotes the Universal Set, P(U) = 1, **Always**
  
## Mathematical Fundamentals:
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

## Ideas Used
<details>

Based on these mathematical principles, the main algorithms behind this project have been made:

- **Card Counting** - The remaining composition of the deck is tracked after the player's known cards are removed. Every probability calculation is then performed on this updated deck, ensuring that all probabilities are conditional on the information already known.
  
-  **Canonical Hand Representation** - We store all the possible cards (**Hands**) that our opponent can possibly have, however each possibility must be **distinct** and each possibility is in the format of: **[Highest,Middle,Lowest]**
  
-  **Use of Mutually Exclusive Events** - Since a Win, a Loss and a Draw are all **Mutually exclusive** we only must compute any two of them and with that knowledge we can calculate the remaining data,

For exaple: P(Loss) = 1 - [P(Win) + P(Draw)] OR P(Win) = 1 - [P(Loss) + P(Draw)]

- **Suits determined by Conditional Probability** - Rather than enumerating every possible suit assignment for every hand, the probability is decomposed into the probability of obtaining the required suit configuration and the probability of obtaining the hand under that configuration,

This can be simply done as,

P(Hand) = P(Hand|Suit) * P(Suit)

*Note: For more information on the use of these ideas and their connection to the mathematics, refer to the docs folder*

</details>

# Algorithm and Architecture

## Algorithm at a glance

The algorithm of the entire program follows this flow sequentially;
- First, the user inputs their cards
- Secondly, the program updates the deck and removes the users cards
- Then, the program classifies what type of hand the user has (Whether it is a flush or a pair or any other combination)
- After this, the program evaluates the hand based on different algorithms for each type of hand
- Before commencing the calculation, the program displays the users hand, what is has classified as and confirms the user's input before proceeding
---
<details> <summary> This part contains what each of the algorithms for each type of hand does </summary>
- If the user has a trio/triple, then the program compares it only with other trios/triples and calculated the losing probability
- If the user has a flush (colour = sequence) it compares it only with trios/triples or other flushes and calculates losing and drawing probability
- Similarly if the user has just a sequence, it compares it with trios/triples, higher sequences and lower flushes that beat or draw with the hand
- If the user has a colour (3 cards of same suit) it compares it with trios/triples + sequences + other colours
- For a hand which only has a pair, the program compares it with trios/triples + sequences + other pairs + colours
- Lastly, if the user has any other hand (also called as a Non-Pair hand) it compares it only with other similiar Non-Pair hands and calculates **winning** and drawing probabilities
</details>

---

- At the end, the remaining probability (be it winning or drawing) can be easily determined since each winning, drawing and losing are mutually exclusive
- These probabilities are then displayed and from there, the user can further terminate the program.

## Functions Used
<details>
<summary> This section contains all the functions used in the program </summary>

The main functions that are used in this program are as follows:
- Start() - This function inputs the users hand and the suits of those cards and stores it as Hand and SuitHand respectively,
- Get_Hand(Hand, SuitHand) - This function obtains the users hand in a numeric format and sorts it, for example, if the user inputs [K,Q,A] (K is King, Q is Queen, A is Ace) the funciton sorts the User's hand as [14,13,12] (The numeric values of those cards in my program)
- State(ls) - This function updates the state of the deck and removes the user's cards from it
- Compare(Hand,SuitHand) - This function obtains what type of Hand the user has (triple,sequence or colour etc.) and then displays it, then, it calls the appropriate evaluating function for each type of hand
- Triple_Probability(TripleVal) - This function calculates probability for trio/triple hands
- Sequence_Probability(SeqVal,Colour,Hand,SuitHand) - This function calculates probability for flushes and normal sequences
- Pair_Probability(PairVal,Kicker,Hand,SuitHand) - This function calculates probability for pairs
- NonPair_Probability(Colour,Hand,SuitHand) - This function calculates probability for colours and non pairs

Other than these main functions there are various Utility functions that have been used,
- Output(Win,Loss,Draw) - This function outputs the winning, loosing and drawing probabilities, it has been made to avoid the repetition of the same print statements after each evaluator function is done processing
- Unbox(ls) - As the name suggests it unboxes a hand to give the respective cards which are there in that hand, this is used for finding the users cards from the users hands or for obtaining the different cards in different possible hands our opponent may have
- Find(i,j,k) - This function is used to find the number of occurences of each card, i,j,k in the deck

The following modules also have been used to improve code readability:
- Check Module - This includes functions like CheckTriple(ls), CheckSeq(ls), CheckPairHigh(ls) and CheckPairLow(ls) which are used to find whether the passed hand are either a triple or sequence or a particular kind of pair (so it can also check what card in i,j,k is a kicker)
- Calc Module - This incldues functions like CalcTriple(ls), CalcPairLow(ls) and CalcPairHigh(ls) and CalcDiff(ls) which are used to calculate the probability of attaining that particular hand
- P(Hand) is a wrapper class that combines the functions of Check Module and Calc Module so that given whatever hand, it shall classify what type it is and then calculate probability for it, so the user can use it blindly the calculate the probability of attaining the hand


For finding the Suit Probability, separate functions have been used such as:
- ColourWeight(Hand,SuitHand,Row) - This function finds the probability of a hand being suited or having the same suits (colour)
- EdgeCorrection(Hand,SuitHand,row) - This function handles the edge cases that are brought upon by the removal of our cards (certain colours become impossible to obtain, this function is explained more in the docs folder)
</details>

## Example

