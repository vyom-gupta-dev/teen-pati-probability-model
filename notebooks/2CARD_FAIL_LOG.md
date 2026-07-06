HIGHER: 2 PLAYERS + 2 CARD -> NO SUITS
All Axioms apply

Same Setup: 52 Cards,
CARD 1+ CARD 2
NO REMOVAL OF CARDS

Sample Space for cards 2-4:

	(2,2)	(2,3)	(2,4)
		(3,3)	(3,4)
			(4,4)

Total: 4 * 3 /2 [n*n-1/2]
Pairs: 3 [n-1]
Non Pairs: 2 * 3/2 [n-1*n-2/2]

Cases: If Pair, then use algo for 1 CARD,
Win: Pair cases + Non Pair Cases / Total
Draw: 1/Total [Exactly that pair]
Loss: 1 - (Win + Draw)

If Non Pairs
Win: For loop,
example: (2,3)
=  -->  Essentially a for loop running from (max of cards, n+1) where win += i -1
(4-2) [Column 3] / Total

Draw: For loop,
example: (1,3)
= (3-2) [Column 3] / Total

Loss = 1 - (Win+Draw)

Note: For 3 cards, imagine it as a tetrahedron of a cube (1/6) of it and proceed.

*Note: The reason this was a failure was because it went astray to the problem, rather than calculating the probability, I had just counted the cases or hand which could beat my hand*
*The uses of matrices to represent different canonical hands also would be a practice that I would not continue for more complex problems like those including 3 cards since it becomes very hard to think and directly get the result*
*However, this development did finally allow me to settle on a proper problem statement for the project*
