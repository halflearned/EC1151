# HW5 - Solutions 

## Q2 - Brooklyn Coffee Shop

a. The $i^{th}$ customer's arrival is a random yes/no event, which can be mapped to $\{0,1\}$ and therefore modelled as $X_{i} \sim Bernoulli(p)$. Here, where $p$ is the probability that the customer arrives at the store (the "yes" event). By the problem setup, $p = 0.4$.

b. Let $Y$ be a random variable that denotes the number of customers that arrive at the shop on a given day. We can relate this number to 

$$Y = X_{1} + X_2 + \cdots + X_n$$ 

because summing the $X_i$'s up is equivalent to counting the number of customer arrivals in $n$ customers. Or, to use more general terminology, it's the **number of "successes" in $n$ "trials"**.

So, is $Y  \sim Binomial(n,p)$? Not yet! Suppose that the first customer is very popular. Everyone else only comes to the store if they can meet her. So either everyone comes (because Ms. One is there), or no one does (because Ms. One is absent). Then actually the pmf of $Y$ will be 

$$Y = \begin{cases}
n \qquad \text{with prob. } 0.4 \\\
0 \qquad \text{with prob. } 0.6 \\\
\end{cases}$$

which is definitely *not* $Binomial$. What went wrong? We haven't assumed **independence** yet. If each $X_i$ is independent from $X_j$, then the scenario above cannot occur, and we finally get that $Y \sim Binomial(n, p)$.


c. The probability of exactly five customers

<img src="binom1.png">

d. The probability of at most three customers

<img src="binom2.png">

The answer is the sum of these probabilities.



## Q3 - Geometric babies

a. The sample space is the **set of all possible outcomes**. So the answer had better be a set. 

In this question, you could define each outcome however you wanted, but let me denote the outcome, say, "three girls and a boy" by the string $GGGB$, and similarly for any other outcome. Then the set is

$$\{B, GB, GGB, GGGB, GGGGB, \cdots \}$$

Note the set is infinite!

<font size=1>Some of you used the word "indefinite" to explain this. It's infinite, surely, but not indefinite. Let's make sure we are using the proper words here.</font>


<b>b) Son is first or second child.</b>

$P(\{B\}) = \frac{1}{2}$ (one "success")
$P(\{GB\}) = \frac{1}{2}\cdot\frac{1}{2}$ (one "failure" followed by one "success")

Since these two events do not overlap, we can just sum up their probabilities

$P(\{B\} \cup \{GB\}) = P(\{B\}) + P(\{GB\}) = \frac{3}{4}$

<b>c) Son is fourth child or later child.</b>

PRO TIP: Problems that involve computing probabilities of "something or later", "something or more", or "at least something" are usually more easily solved by computing the probability of the complementary event first. 

Let $A$ be the event "the son is the first, second or third child". The probability of that is 

$P(A) = \frac{1}{2} + \frac{1}{2^2} + \frac{1}{2^3} = \frac{7}{8}$

So the event we're looking for is 

$P(A^c) = 1 - P(A) = \frac{1}{8}$

What? You want to solve this by actually computing the infinite sum? You nerd. Here we go. 

$P(\{GGGB\} \cup \{GGGGB\} \cup \cdots)$ 

$\qquad = P(\{GGGB\}) + P(\{GGGGB\}) + \cdots$ 

$\qquad = \frac{1}{2^4} + \frac{1}{2^5} + \frac{1}{2^6} + \cdots $ 

First factor out the common $\frac{1}{2^4}$

$\qquad = \frac{1}{2^4}\left(1 + \frac{1}{2} + \frac{1}{2^2} + \cdots \right)$ 

Now use what you know about <a href="https://en.wikipedia.org/wiki/Geometric_series">geometric series</a> to evaluate the expression in parenthesis.

$\qquad = \frac{1}{2^4}2$

$\qquad = \frac{1}{8}$ 

What again? The thing about geometric series went over your head? Ok, stare at this instead

<img src="series2.png">

*See how the total area is 2?*

By the way, this geometric series thing is where the Geometric distribution gets its name.

## Q5 - Lady Tasting Tea

<b>Probability of a coincidence</b>

The probability that the lady gets any cup right is $p = 0.5$ (why?). Since each trial is independent from the previous one, the number of correct trials is $X \sim Bernoulli(10, \frac{1}{2})$. We just have to consult the probability table, or compute it ourselves, to see that the probability of this extreme result is 0.0439.


<b>Do you believe it?</b>

It's funny that half of you would require a much higher number of trials and successes. The truth is that 8 out of 10 trials is already almost publishable evidence in many fields of science, including economics! I'll have (much) more to say about this later, when we talk about hypothesis testing. 


----

## Programming

### Q9 - Divisible integers

```python
for i in range(101):
    if i % 3 == 0 and i % 5 != 0:
        print(i)
```

By the way, this was a variation on the <a href="https://en.wikipedia.org/wiki/Fizz_buzz#Programming_interviews">FizzBuzz</a> problem, which is a (now in)famous job interview question. Well done solving it!



