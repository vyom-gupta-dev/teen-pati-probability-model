11/06/26 - 2 CARDS + SUITS -

ADDITIONAL ASSUMPTION

- Cards with same suit > Cards with different suits
- Pairs > Suits

->Separate sample data into 2 domains, Suits and Non Suits,

->Ultimately, the comparision algo is the same as 2 CARDS NO SUITS,

->But, WEIGHTED PROBABILITY comes into play,

HIGHLIGHT OF ALGO:

Probability calculation changes -

Total, 16 Suits pairs are possible -

4 Suits pairs have the same suits (Suited)

12 Suits pairs have different suits (Non Suited) [Consider [6C,3S] is distinct from [6S,3C]] !!LOGIC!!

---
Thus, the Probability calculation for [i,j,s] =

(2*P(i)*P(j)*P(s)) [If i!=j]

(P(i)*P(j)*P(s)) [If i==j]

---
Now,

EDGE CASES-

Problem - Our Cards, are not replaced, so there might be some combinations that are not possible,

for example - 6 Spades + 2 Diamonds,

It is not possible for the pair - [6,3]

To have suits with Spades (Since 6 of Spades is gone)

Thus, If encountering cases where a card is gone, P(s) actually depends on the number of the less occurring cards

(In this case there are only 3 cards for 6 and therefore only 3 suited pairs are possible and 9 non suits, total = 3*4)


(Similiarly in [6,2] case, Only 3 suited pairs are possible and 6 non suited pairs are possible, total = 3*3 = 9) - FOLLOW THIS ALGO FOR DETERMINING IDEAL AND NON IDEAL CASES

OPTIMIZATIONS:

-> For Pairs, no change in algo, losing for other pairs

-> For Suited, only compare Suits (Probability formula for P(s) adds here) + Calculate Pairs also [A pain] (losing chances)

-> For Non Suits, only compare wining for other non suits

- *This project additionally brought with it the MOST important section with it that were the Edge Cases, it is also where I see the effects of how our hand blocks the opponent from receiving certain hands*
- *Addiitionally, the formulation of suits as a kind of probabilistic weight allowed me to further reduce compleixty and the extent of data I would have to go through, this optimization would be vital in the final project*
