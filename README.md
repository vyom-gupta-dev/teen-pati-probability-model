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
*Note: This section contains the basic axioms of probability and notation that is used in the algorithm, if you are familiar with them, then it is suggestable for you to skip this section*

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

## Ideas Used

Based on these mathematical principles, the main algorithms behind this project have been made:

- **Card Counting** - The remaining composition of the deck is tracked after the player's known cards are removed. Every probability calculation is then performed on this updated deck, ensuring that all probabilities are conditional on the information already known.
  
-  **Canonical Hand Representation** - We store all the possible cards (**Hands**) that our opponent can possibly have, however each possibility must be **distinct** and each possibility is in the format of: **[Highest,Middle,Lowest]**
  
-  **Use of Mutually Exclusive Events** - Since a Win, a Loss and a Draw are all **Mutually exclusive** we only must compute any two of them and with that knowledge we can calculate the remaining data,

For exaple: P(Loss) = 1 - [P(Win) + P(Draw)] OR P(Win) = 1 - [P(Loss) + P(Draw)]

- **Suits determined by Conditional Probability** - Rather than enumerating every possible suit assignment for every hand, the probability is decomposed into the probability of obtaining the required suit configuration and the probability of obtaining the hand under that configuration,

This can be simply done as,

P(Hand) = P(Hand|Suit) * P(Suit)
