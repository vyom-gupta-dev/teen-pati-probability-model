# teen-pati-probability-model
An analytical probability engine that has been designed to calculate the probability of winning, losing or drawing in the  Indian Card Game - Teen Patti based on the principles of combinatorics and conditional probability.

# What is Teen Patti
Teen Patti is a card game that is commonly played in India where each player recieves three cards or Teen Patti and based on the strength of their hand they decide how much money they decide to bet. Whoever has the highest hand wins. 

# Strength of Hands in Teen Patti:
Trail/Trio (Three of a Kind): Three cards of the same rank; Aces are highest
Pure Sequence (Straight Flush): Three consecutive cards of the same suit. Example: A-K-Q of diamonds ****
Sequence (Straight): Three consecutive cards of mixed suits
Color (Flush): Three cards of the same suit, not in sequence. Compare highest card first ***
Pair (Two of a Kind): Two cards of the same rank; compare the pair first, then the kicker
High Card: None of the above; compare highest → middle → lowest card

# The goal of this project:
This project was designed as a summer project into applying probability to be able to determine the chance of winning a hand between 2 players given my cards. In real life, proffessionals try to keep track of cards that may be present in the deck (Card Counting) and you make intuitional guesses on what the other players may have. However, these are guesses at the end of the day, it is becomes humanly impossible to have an exact idea of the probability as whether you shall win. 
Moreover, the calculation behind such a problem is lengthy, long and prone to mistakes due to the various cases possible. 
This limitation is easily overcome by the use of computation as though the cases are numerous, the ultimate algorithm follows the basic principles of probability. Additionally, the deck is constrained to only 52 cards with a set composition of occurences in the deck. 
Thus, this project was originally designed as a probability engine that analytically optimizes the calculation.
