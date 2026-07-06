15/06/26 - 3 CARDS NO SUITS

We keep the same problem statement and constraints,

Problem Statement:
**FIRST**, You are given your cards, <br>
**THEN**, your opponent gets their cards, <br>
Following the rules of Teen Pati- <br>

A) Find the hands that can beat or lose to your hand, <br>
B) Additionally find the probability of obtaining those cards <br>
Note: The Cards you posses are not replaced. <br>

Rules (modified for the problem):

Trail/Trio (Three of a Kind): Three cards of the same rank; Aces are highest <br>
Sequence (Straight): Three consecutive cards of mixed suits (IF BOTH SEQ, FIND HIGHER LOWER CARD) <br>
Pair (Two of a Kind): Two cards of the same rank; compare the pair first, then the kicker <br>
High Card: None of the above; compare highest → middle → lowest card <br>

Methodology, <br>
-> Card Counting - Keep track of cards <br>
-> Fixed possibilities - Data arranged - We generate all the hands in the order of [Lowest, Middle, Highest] <br>
-> Optimizing - Minimizing the need to compare all the hands, <br>

Direction: First 4 then 13, However, may be skipped, Use of AI for verification and calulcation,

Algo: Resemblance with 2 cards in structure,

-> Trios compared ONLY with other Trios (Losing) - Same algo for Pairs in 2 Cards <br>
-> Sequences = Trio Possibility (fixed) + Sequence possibility (Losing) - Condition for Seq + Comparing Lower Card <br>
-> Pairs = Other Pairs + All Non Pairs [A pain, Alternative is Beating Pairs + Seq + Trio] - See if Pair, if Pair equal then Kicker (complicated condition to find Pair value and Kicker) <br>
-> Non Pairs = Only Non Pairs [3 nested ifs] <br>
-> Probability Calculation Have caution of Order mattering despite End State as in the P(i,j) problem <br>

Note: For sanity, obtain cards directly in highest, middle, lowest order <br>

- *The most important development here is the beggining of the CANONICAL HAND REPRESENTATION*
- *This allowed me to easily compare hands and simplify the code, this technique carries over into the final project*
