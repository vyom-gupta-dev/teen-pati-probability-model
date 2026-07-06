-> In our previous processes we went astray to the actual problem,
So we calculated, Pairs which can beat us
The question demands, Probability of obtaining those pairs + The pairs themselves

3/6/26: ATTEMPT 2 - 2 CARDS NO SUITS

-> **CARD COUNTING** - The single constraint in this problem is that we know the exact number of cards
-> Thus, We create a database which stores each card (ignoring suits for now)
-> **FIXED POSSIBILITIES** - Create an organized database that has all the possible pairs, store the data.
-> Use the data and use it actively

-> Applicable Rules:
Pairs Beat Non Pairs-
If Pairs, compare which number pair it is, higher number, more preffered,
if not, tie

If Non Pairs,
compare highest cards, higher number, more preffered,
if tie, then compare next card, higher number, more preffered,
if equal, then tie

-> Possible Outcomes, Win + Ties

Algorithm:

->Using our previous attempt at this question, we copy the algorithm, rather the matrix and sets of values and categorize them
->Then evaluate probability for obtaining each pair using our hashmap
-> Find total win probability by simple addition (mutual exclusive events)
-> Do the same for the draw set.

Plan of Action:
First do it for 4
Then expand to 13

RESULTS/PRECAUTIONS:
-> Data being ordered - [Higher, Lower] - aids in code implementation (oppMax, myMin segement of the code can be simplified knowing this)
-> Precaution, In comparing non pairs, First Higher, if TRUE, THEN compare lower
-> Precaution, order of distributing cards matter, even if result is the same (reason why in the initial testing non pairs had a low chance of winning, off BY A FACTOR OF 2)
-> Optimize comparisions and choose Winning/Losing cases whichever are less, results in less code

- *This project was perhaps the most important milestone in the development cycle as it firmly established the key cornerstones and algorithms whciht the project built upon*
- *Additionally, and more importantly, the results and precautions proved to be pivotal in shortening the development time as I prevented myself from being lost in the abstraction and making a mistake*
- *The order of distribution explains why in the Calc Modules numbers like 6 or 3 appear as they represent the various final states the hand could achieve, that idea started from here*
- *Additionally other optimization techniques originate from this project*
