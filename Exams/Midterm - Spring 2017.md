# <center>Midterm - Spring 2017 - Solutions</center>


### Chain rule [10pts]

In *one* paragraph, explain the "chain rule" of probability

$$P(A∩B)=P(A|B)P(B)$$ 

as intuitively as you can. If it's easier, you can also use a graph (like a tree, or a Venn diagram), or  reason by an example (like the male/female execs in a company).

<font color="blue">
This was purely definitional. If you wrote something reasonably coherent, you should have gotten 8-10 points.
</font>

### Grades and effort [10pts]

The table below presents the probability of a student simultaneously putting high (H) or low (L) effort into a course and getting a correspoding grade (A, B or C).

<center>

| | H | L |
|---|:-----:|:-----:|
| <b>A</b> | .4 | .1 |
| <b>B</b> | .15 | .1 |
| <b>C</b> | .05 | .2 |

</center>

First, compute the following.

1) $P(H \cap A)$ <font color="blue">$P(A\cap H) = .4$</font>
1) $P(A)$ <font color="blue">$P(A) = P(A\cap H) + P(A \cap L) = 0.1 + 0.4 = 0.5$</font>
1) $P(H|A)$ <font color="blue">$P(H |A)  = \frac{P(A\cap H)}{P(A)} = 0.8$</font>

Also answer these questions.

1 Are $H$ and $L$ independent events? <font color="blue">No: $0 = P(H\cap L) \neq P(H)P(L) = .6 \times .4$</font>. 
2. Are $A$ and $H$ independent events? <font color="blue">No: $0.4 = P(H\cap L) \neq P(A)P(H) = .5 \times .6 = 0.3$</font>. 


### Compulsive liars [10pts]

SnakeOil Jack is a compulsive liar. Every statement he says has a $\frac{3}{4}$ probability of being a lie. SnakeOil Jack sees the outcome of a *fair* coin flip, and tells you the outcome is Heads. What is the probability of the coin having actually landed Heads?



<font color="blue">
Events:
$A$: SnakeOil Jack says "Heads"
$H$: The actual outcome was Heads

We know $P(A|H) = \frac{1}{4}$ (he'd be telling the truth) and $P(A|H^c) = \frac{3}{4}$ (he'd be telling a lie). Moreover, since the coin is fair, we also know $P(H) = P(H^c) = \frac{1}{2}$.

From Bayes:
 $P(H|A) = \frac{P(A|H)P(H)}{P(A|H)P(H) + P(A|H^c)P(H^c)} = \frac{1}{4}$
 
 <b>Remark</b> Many of you tried to condition on the event "Jack is telling the truth". That's not the right approach: we can only condition on what we know to be certain. In this problem, we are certain that Jack *said* the outcome was Heads, so this is what we can condition on.
 
 </font>. 




### Deck of cards [20pts]

A deck of cards contains 52 cards, divided in 4 *suits*, namely diamonds $♦$, clubs ♧, spades ♤ and hearts ♥, as well as 13 *ranks* {A,2,3,...,10,J,Q,K}. There are no jokers.   

1) In how many ways can we shuffle this deck of 52 cards?
<font color="blue">52!</font>

For the next three questions: a *hand* is set of five cards drawn from the deck without replacement. The order of the cards in a hand does not matter.

2) How many possible *hands* are there?
<font color="blue">$\binom{52}{5}$</font>

3) What is the probability that of drawing a hand where every card is of a different *rank*? 

Example: (<u>5</u>, ♤), (<u>6</u>, ♤), (<u>10</u>, $♦$), (<u>A</u>, ♥), (<u>K</u>, ♥)
<font color="blue">$4^5\frac{\binom{13}{5}}{{\binom{52}{5}}}$ or $
\frac{52\times 48 \times 44 \times 40 \times 38}{52\times 51\times 50 \times 49 \times 48}$</font>

4) What is the probability that of drawing a hand where all four cards are of the same *suit*?

Example: (5, <u>♤</u>), (6, <u>♤</u>), (7, <u>♤</u>), (A, <u>♤</u>), (K, <u>♤</u>)
<font color="blue">$4\frac{\binom{13}{5}}{\binom{52}{5}}$ or $\frac{52\times 12 \times 11 \times 10 \times 9}{52\times 51\times 50 \times 49 \times 48}$</font>

### Graphs, transformations and expectations [15pts]

Let $X$ have the following PMF
$$
p_X(x) = 
\begin{cases}
\frac{1}{5} \qquad \text{if } \  x = -2, -1, 0, 1, \text{ or } 2 \\\
0 \qquad \text{otherwise}
\end{cases}
$$

Also, let $Y = |X|$ (i.e., the absolute value of $X$).

1. Draw the PMF of $Y$
2. Draw the CDF of $Y$
3. Compute $E[Y]$

<font color="blue">
$E[Y]= \frac{1}{5}0 + \frac{2}{5}1 + \frac{2}{5}2 = \frac{6}{5}$
</font>




### Passing an exam [15pts]

A student takes a multiple choice test with $10$ questions, each with $5$ choices (only one of which is correct). Suppose that the student blindly guesses the answer to each question, simply choosing one of the alternatives uniformly at random, and independently from the other choices. 

1) Let $X_1$ be a random variable that takes value $1$ if the student gets the first question correct, and $0$ otherwise. Give the name and the parameters of the distribution of $X_1$.
<font color="blue">
$X_1 \sim Bernoulli(\frac{1}{5})$
</font>

2) Let $Y$ be the number of questions the student guesses in total. What is the distribution of $Y$? Give its name and parameters.
<font color="blue">
$Y \sim Binomial(10, \frac{1}{5})$
</font>


3) Compute $E[Y]$.
<font color="blue">
$E[Y] = np = 10\frac{1}{5}$
</font>
4) To pass this exam, the student must get at least $6$ of the answers correct. What's the probability of that happening?
<font color="blue">
$P(Y \geq 6) = \sum_{k=6}^{10}p_Y(k) = 0.006 + 0.001 + 0 + 0 + 0= 0.007$
</font>

### Time to finish [20pts]
 
Suppose the time a student takes to finish a certain midterm problem, in minutes, can be modeled as $T \sim Uniform[0, 20]$ (that is, any *real* number between zero and 20 is possible).
1) What is the probability that a student will take at least 12 minutes to finish the problem?

<font color="blue">
$P(T \geq 12) = \int_{12}^{20}\frac{1}{20}dt = \frac{8}{20} = \frac{2}{5}$

<b>Remark</b> Looks like about half of you got confused and ended up computing $P(T \leq 12)$ instead. If reversing the inequality was your only mistake, and if you were consistent and clear about what you were answering, I ignored the mistake and did not deduct any points. 
</font>2) Suppose that the student has already spent $5$ minutes on the problem. Given this information, what is the probability that it will take him or her more than $10$ minutes in total? 

<b>Hint</b> Carefully define the relevant events, and use this fact: if $A \subset B$, then $P(A \cap B) = P(A)$.

<font color="blue">
Let
$A$: student takes 10 minutes or more
$B$: student takes 5 minutes or more
Then
$P(A|B) = \frac{P(A \cap B)}{P(B)} = \frac{P(A)}{P(B)} = 
\frac{\int_{10}^{20}\frac{1}{20}dt}{\int_{5}^{20}\frac{1}{20}dt} = \frac{0.50}{0.75} = \frac{1}{3}$
</font>
3) Number the $22$ students in our class from $1$ to $22$, and let $T_1$, $T_2$, $\cdots$, $T_{22}$ be the time that each student takes to finish the problem. These random variables are all independent. 

What is the probability that *all* students will finish the problem in $15$ minutes or less?

<font color="blue">
Let $A_i$ be the event that the $i^{th}$ student finishes in 15 minutes or less. Since these events are all independent, the probability of all of them happening together decomposes multiplicatively. We can write

$$P(A_1 \cap A_2 \cap \cdots \cap A_{22}) = P(A_1)\times P(A_2) \times \cdots \times P(A_{22})$$

Moreover, since all students' time to finish have the same distribution,

$$P(A_1) = P(A_2) = \cdots = P(A_{22})$$

Using the two pieces of information above, we have that

$$P(A_1 \cap A_2 \cap \cdots \cap A_{22}) = P(A_1)^{22}$$

All we need is to do is to compute this probability

$$P(A_1) = \int_{0}^{15}\frac{1}{20}dt = \frac{15}{20} = \frac{3}{4}$$

Putting it all together,

$$P(A_1 \cap A_2 \cap \cdots \cap A_{22}) = \left(\frac{3}{4}\right)^{22}$$
</font>






