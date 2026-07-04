# teen-pati-probability-model
An analytical probability engine that has been designed to calculate the probability of winning, losing or drawing in the  Indian Card Game - Teen Patti based on the principles of combinatorics and conditional probability.

This repository contains an analytical probability engine that computes the probabilities of winning, losing, or drawing in a two-player game of Teen Patti using combinatorics and conditional probability.

## What is Teen Patti
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
