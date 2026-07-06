27/06/26 - 3 CARDS + SUIT - THE FINALE <br>

Combine 3 Cards No Suits + 2 Cards with Suit <br>
Problem statement is the same <br>

Rules: <br>
Trail/Trio (Three of a Kind): Three cards of the same rank; Aces are highest <br>
Pure Sequence (Straight Flush): Three consecutive cards of the same suit. Example: A-K-Q of diamonds **** <br>
Sequence (Straight): Three consecutive cards of mixed suits <br>
Color (Flush): Three cards of the same suit, not in sequence. Compare highest card first *** <br>
Pair (Two of a Kind): Two cards of the same rank; compare the pair first, then the kicker <br>
High Card: None of the above; compare highest → middle → lowest card <br>

Methodology, <br>
-> Card Counting - Keep track of cards <br>
-> Fixed possibilities - Data arranged - We generate all the hands in the order of [Lowest, Middle, Highest] <br>
-> Optimizing - Minimizing the need to compare all the hands <br>
-> Weighted Probability - Easier to obtain non suits than Suits so P(s) changes <br>
			- Suit triples = 4 /64 <br>
			- Non Suit triples = 60 / 64 <br>
EDGE CASES- <br>

If all our 3 cards are differently suited for example: <br>
[As,Kc,Jd] <br>
Then for the Colour: [A,K,J] there is only one possibility: <br>
[Ad,Kd,Jd] <br>

Therefor for every matching card in the data triplet, the number of colours reduce. <br>

Thus, we have to check for every matching card and among those cards see how many suits are eliminated <br>

Algo: Keep copy pasting code from previous sections + adding s, even within different hands calculation just keep calculating losing and draw probabilities only, lesser calculation <br>
->Trios compared only with trios (P(s) = 1) <br>
->Flush compared with trios + other flushes (P(s) = 1/16 for all suit hands) <br>
->Unsuited Sequence compared with Trios (P(s) = 1) + Higher Sequences (P(s) = 1) + Lower Sequences (P(s) = 1/16) <br>
->Color compared with trios (P(s) = 1) + Sequences (P(s) = 1) + Other Colors (Non Pair Algo + P(s) = 1/16) <br>
->Pair compared with other Pairs (P(s) = 1) + Non Pairs (P(s) = 15/16) [Winning And Drawing Prob] <br>
->Non Pair compared with other Non Pairs (P(s) = 15/16) <br>

Challenge: Do everything in functions <br>

->Input() - Takes in the cards and sorts them -> <br>
->State() - Updates the card deck. <br>
->Type() - Classifies what type of hand it is -> <br>
->Compare() - Mother function: <br>
->Triple() - Compares for all triples <br>
->Sequence() - Compares for all Sequences <br>
->Pairs() - Compares for Pairs <br>
->Non Pairs() - Compares for Non Pairs <br>

---

->Suits() - Does Suit Calculation <br>
->Main() - User Interface + Holds Win, Loss and Draw Probability + Outputs everything <br>

Modules: For Convenience these functions have been deployed, <br>

CheckTriple() - Checks whether it is a triple or not <br>
CheckSequence() - Checks whether it is a sequence or not <br>
CheckSequenceAce() - Check whether it is special sequence A23 <br>
CheckPairHigh() - Indicated whether top 2 cards make a pair <br>
CheckPairLow() - Indicated whether bottom 2 cards make a pair <br>

- *Note: This was an approximate idea of how I would have developed the arhcitecture design in the respoitory*
- *More importantly, the part on **Edge Corrections** is arguable the most intresting and challenging part of the project to reliaze, which I have again expanded upon in the docs folder*
