# Midterm - Spring 2017

1. Explain your reasoning as clearly and precisely as you can. 

2. Write legibly. If I can't read what you wrote, you get *zero* points.

1. Don't waste too much time simplifying fractions, exponents, binomial coefficients or factorials; don't round your answers

1. When drawing graphs, make sure to label your axes.


### Chain rule [10pts]

In *one* paragraph, explain the "chain rule" of probability

$$P(A∩B)=P(A|B)P(B)$$ 

as intuitively as you can. If it's easier, you can also use a graph (like a tree, or a Venn diagram), or  reason by an example (like the male/female execs in a company).

### Grades and Effort [10pts]

The table below tabular the probability of a student simultaneously putting high (H) or low (L) effort in a course and getting a correspoding grade (A, B and C).

| | H | L |
|---|:-----:|:-----:|
| <b>A</b> | .4 | .1 |
| <b>B</b> | .15 | .1 |
| <b>C</b> | .05 | .2 |

First, compute the following.

1. $P(H \cap A)$ <font color="blue">$P(A\cap H) = .4$</font>
1. $P(A)$ <font color="blue">$P(A) = P(A\cap H) + P(A \cap L) = 0.1 + 0.4 = 0.5$</font>
1. $P(H|A)$ <font color="blue">$P(H |A)  = \frac{P(A\cap H)}{P(A)} = 0.8$</font>

Also answer these questions.

1. Are $H$ and $L$ independent events? <font color="blue">No: $0 = P(H\cap L) \neq P(H)P(L) = .6 \times .4$</font>. 
2. Are $A$ and $H$ independent events? <font color="blue">No: $0.4 = P(H\cap L) \neq P(A)P(H) = .5 \times .6 = 0.3$</font>. 


### Compulsive liars [10pts]

SnakeOil Jack is a compulsive liar. Every statement he says has a $\frac{3}{4}$ probability of being a lie. He sees the outcome of a *fair* coin flip, and tells you the outcome is Heads. What is the probability of the coin actually having landed Heads?

<font color="blue">
Let $A$ the events "Jack says Heads", and let $H$ be the event of "Heads".

We know $P(A|H) = \frac{1}{4}$ (he'd be telling the truth) and $P(A|H^c) = \frac{3}{4}$ (hd'd be telling a lie). Moreover, since the coin is fair, we also know $P(H) = P(H^c) = \frac{1}{2}$.

From Bayes:
 $P(H|A) = \frac{P(A|H)P(H)}{P(A|H)P(H) + P(A|H^c)P(H^c)} = \frac{1}{4}$</font>. 


### Deck of cards [15pts]

A deck of cards contains 52 cards, divided in 4 *suits*, namely diamonds $♦$, clubs ♧, spades ♤ and hearts ♥, as well as 13 *ranks* {A,2,3,...,10,J,Q,K}. There are no jokers.   

1) In how many ways can we shuffle this deck of 52 cards?
<font color="blue">52!</font>

For the next three questions, let's call a set of five different cards a *hand*. The order of the cards in a hand does not matter.

2) How many possible *hands* are there?
<font color="blue">$\binom{52}{5}$</font>


3) What is the probability that of drawing a hand where every card is of a different *kind*? 
Example: (5, ♤), (6, ♤), (10, $♦$), (A, ♥), (K, ♥)
<font color="blue">$\binom{13}{5}\frac{4^5}{\binom{52}{5}}$</font>


4) What is the probability that of drawing a hand where all four cards are of the same *suit*?
Example: (5, ♤), (6, ♤), (7, ♤), (A, ♤), (K, ♤)
<font color="blue">$13\frac{\binom{13}{5}}{\binom{52}{5}}$</font>


### Binomial and Uniform [15pts]

1) Let $X \sim Binomial(3, \frac{1}{3})$.

a. Draw the PMF of $X$
b. Draw the CDF of $X$
c. Compute $E[X]$
d. Compute $E[X^2]$

2) Let $X \sim Uniform[0, 2]$ -- that is, any *real* number between 0 and 2 has equal probability density (so 1.323 and 0.4555 are possible outcomes).

a. Draw the PDF of $X$
b. Draw the CDF of $X$



### Airlines again [15pts]

Suppose that each passenger who reserves a seat in a flight shows up with probability $\frac{6}{10}$, independently of the other passengers. 

1) Teeny-Weeny Airlines always sells 10 tickes for their 9-seat airplane, while Tiny-Miny Airlines always sells 20 tickets for their 18-seat aeroplane. Which company has a larger probability of an overbooking conflict?

2) What is the maximum number of tickets that Tiny-Miny Airlines can sell while still keeping the probability of an overbooking conflict below $10\%$?


### Time to finish [15pts]
 
Suppose the time a student takes to finish a certain midterm problem, in minutes, can be modeled as $T \sim Uniform[0, 20]$ (that is, any *real* number between zero and 20 is possible).
1) What is the probability that a student will take at least 12 minutes to finish the problem?2) Suppose that the student has already spent $5$ minutes in the problem. Given this information, what is the probability that it will take his or her more than $10$ minutes in total? 

<b>Hint</b> Carefully define the relevant events, and remember that if $A \subset B$, then $P(A \cap B) = P(A)$.

3) Number the $22$ students in our class from $1$ to $22$, and let $T_1$, $T_2$, $\cdots$, $T_{22}$ be the time that each student takes to finish the problem. These random variables are all independent. 

What is the probability that *all* students will finish the problem in $15$ minutes or less?





