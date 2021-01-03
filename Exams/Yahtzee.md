 Yahtzee

The cell entries indicate the probability of going from the current to the next state. For example, the entry in cell $$(1,5)$$ is the probability of a Yahtzee right at the beginning of the game; the entry $$(4,4)$$ represents the probability of starting the round with 4 dice, and rolling the last die but not succeeding to get a Yahtzee.

<center>

| | 1 | 2 | 3 | 4 | 5  |
|:---:|:--:|:--:|:--:|:--:|:--:|:--:|
|1 | $$\frac{120}{6^4}$$ | $$\frac{900}{6^4}$$ | $$\frac{250}{6^4}$$ | $$\frac{25}{6^4}$$ | $$\frac{1}{6^4}$$ |
|2 | 0 | $$\frac{120}{6^3}$$ | $$\frac{80}{6^3}$$ | $$\frac{15}{6^3}$$| $$\frac{1}{6^3}$$  |
|3 | 0 | 0 | $$\frac{25}{6^2}$$ | $$\frac{10}{6^2}$$  | $$\frac{1}{6^2}$$  |
|4 |  0 | 0 | 0 |$$\frac{5}{6}$$ | $$\frac{1}{6}$$ |
|5 | 0 | 0 | 0 | 0 | 1 |

</center>

 Numerator explanations

 From state 1

To 1: All different, and also different from what we're currently keeping $$5 \cdot 4 \cdot 3 \cdot 2$$

To 2: Several cases:

+ One dice out of four matches current, other 3 are all different
$${4 \choose 1}1\cdot 5 \cdot 4 \cdot 3$$

+ One dice out of four matches current, other 3 form one other pair
$${4 \choose 1}{3 \choose 2}1\cdot 5 \cdot 4$$

+ No dice matches our current dice, but one new pair is formed
$${4 \choose 2}5 \cdot 4 \cdot 3$$

+ No dice matches our current dice, but two new pairs are formed
$${4 \choose 2}{5 \choose 2}$$

To 3: 

+ Three-of-a-kind, different from what we're keeping 
$${4 \choose 3}5$$
+ Two match what we're keeping, others anything but that
$${4 \choose 2} 1\cdot 5\cdot 5$$

To 4:

+ Pair matching what we're keeping, other different $${4 \choose 2}1\cdot 5 \cdot 5$$
+ Three of a kind matching what we're keeping, last one different $${4 \choose 3}1 \cdot 5$$
+ Four of a kind, different from what we're keeping $$5$$


To 5:

Four-of-a-kind matching what we're keeping: $$1$$

 From state 2

To 2:

+ All different, and different from what we have: $$5 \cdot 4 \cdot 3$$
+ Pair, different from what we have: $${3 \choose 2}5\cdot 1 \cdot 4$$

To 3:

+ Three of a kind, different from what we have: $$5$$
+ One matches what we're keeping, other different: $${3 \choose 1}1\cdot 5 \cdot 5$$

To 4:

+ Pair matching what we're keeping: $${3 \choose  2}1\cdot 1\cdot 5$$

To 5:

+ Three-of-a-kind matching the pair we have: $$1$$

 From state 3

To 3:

+ No new dice matches our triple: $$5 \cdot 5$$

To 4:

+ One of the new dice matches our triple, the other doesn't: $${2 \choose 1}1 \cdot 5$$

To 5:

+ Pair matching the triple we have: $$1$$

 From state 4

To 4:

+ New die is different from what we have: $$5$$

To 5:

+ New die matches what we have: $$1$$




