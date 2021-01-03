# HW8 Theory - Due Apr 5th (Wed) with PP7

### Q1) Basic definitions

Compute the mean, median, variance and standard deviation of the objects below *without* `scipy.stats` or probability tables.

1. $X \sim Binomial(5, \frac{1}{3})$.  
2. $Y \sim Uniform(0, 2)$ 
3. The list of numbers $1,2,3,4,5,5,10$


### Q2) Properties of the variance

Let $X$ be any random variable with finite variance, and let $a$ be a constant. Using the definition of variance and what you know about expectation, prove the following.

1. $Var[aX] = a^2Var[X]$
1. $Var[X + a] = Var[X]$
2. $Var[X] = E[X^2] - E[X]^2$

<b>Hint</b> Whenever you're asked to *prove* something, try this for a start.

\#1 Copy the left-hand side of what you want to prove.

$Var[aX]$

\#2 Expand whatever definitions you know.

$Var[aX] = E[((aX) - E[aX])^2]$

Now think: Does this look like something that will lead to the right-hand side? Are there any properties of expectation that you can use here? Maybe you can do the same with the right-hand side, so you get a better idea of what you want to get at.

In the end, your proof should look more or less like this.

$\begin{align}
Var[aX] &= E[((aX) - E[aX])^2] \ \ \text{Using def of variance} \\\
&= \cdots \qquad  \qquad \qquad \qquad  \text{Using...}  \\\
&= \cdots \qquad \qquad\qquad \qquad  \text{From the....} \\\
&= \cdots \qquad\qquad\qquad \qquad  \text{Invoking the ... theorem} \\\
&= \cdots \qquad \qquad\qquad  \qquad \text{Since 2+2 = 4} \\\
&= a^2 Var[X] \\\
\end{align}$

<font size=2>(The explanations to the right of each equality are just placeholders. Your explanations will be different. It might also take more or fewer lines.)</font>



### Q3) The standard Normal distribution

When $Z \sim Normal(0,1)$ (ie., a random variable that is Normally distributed with mean $0$ and *variance* $1$), we say that $Z$ has the **standard Normal** distribution. 

Suppose you are working with such $Z$ variable, and you'd like to know what is $P(Z \leq 0.35)$. One way to find that out is to look at probability tables just like the ones you saw when you first learned about the Binomial. In the file `standard_normal_table.pdf`, you'll find one such table. Reading it is pretty easy:

<img src="standard_normal_table_example.png">
<br><br>

That is, if you want to know the value of the CDF at $0.35$, look at row $0.3$ and column $0.05$. Here, $P(Z \leq 0.35) \approx 0.6368$.

Using the table, find out:

1) $P(Z \leq 0)$
2) $P(Z > 3)$
3) $P(-1 \leq Z \leq 1)$
4) The 0.9-quantile of $Z$ [i.e., the number $c$ so that $P(X \leq c) = 0.9$]
4) The 0.1-quantile of $Z$ [i.e., the number $c$ so that $P(X \leq c) = 0.1$]

Now let's introduce a small twist. Suppose you were working in a certain problem with a Normally distributed random variable $X \sim Normal(3, 4)$. That is, $E[X] = 3$ and $Var[X] = 4$, so even though $X$ has the Normal distribution, it does not have the *standard* Normal distribution. Can we still use the table above to query the probabilities of $X$?

The answer is *yes*, and here's how. Suppose we want to know $P(X \leq 1)$.

First, we will rewrite $X$ in terms of a random variable $Z \sim Normal(0,1)$, so that $X = aZ + b$. The trick will be to choose these $a$ and $b$ parameters *smartly*.

Assuming we have $a,b$, we can perform the following computation.

$\begin{align}
P(X \leq 1) &= P(aZ + b \leq 1) \\\
\qquad &= P \left(Z \leq \frac{1 - b}{a} \right)
\end{align}$

That is, if we want to know the probability that $X$ is smaller than 1, we can check the table for the probability that $Z$ is smaller than $\frac{1-b}{a}$, because they're the same!

Now answer the following.

6) If $Var[X] = 4$, what number $a$ will make $Var[aX] = 1$?
7) If $E[X] = 3$, what number $b$ will make $E[X + b] = 0$?

Using the two numbers above, we can write $X = aZ + b$.

8) Find out $P(X \leq 1)$

<font size=1>By the way, in the Programming Practice you'll learn how to query these probabilities without going through these shenanigans.</font>


### Q4) Waiting for good dollars

You'd like to sell your car, and decide to sell it to the first person to offer at least $5000$ for it. Let's call such offers *acceptable*.

Each offer is a random variable: $X_1$ is the first offer you receive, $X_2$ is the second, and so on.  Assume each one comes from the same distribution, $Normal(4000, 10^6)$ [that's mean $4000$ and *variance* a million] and that they are all independent of each other. 

1) What's the probability that any offer is *acceptable*?

2) What is the expected number of offers you will receive before an acceptable one comes along?

3) Suppose you know that an offer is acceptable. What is the probability that this (already known to be acceptable) offer is larger than $6000$ dollars?

<b>Hint</b> Last question in the midterm

4) Find the number $c$ so that $90\%$ of the offer probabilities will fall within the interval $[4000 - c, 4000 + c]$.

<b>Hint</b> Think about quantiles.

----

##### A possibly humorous but not entirely untrue personal remark

Because undergraduate textbooks often use $Z$ exclusively for standard Normal random variables, some people end up calling the standard Normal distribution *the $Z$ distribution*. Likewise, the standard Normal probability table is called the *$Z$-table* by such people. And (as you'll see later) tests that involve the standard normal distribution are called *$Z$-tests*. 

But look, you shouldn't do that.

For whatever reason, I've never seen a reputable researcher use the expression "the Z distribution". This also shows up in zero of the advanced textbooks that I've read. So if someone says "the Z distribution" to me, I immediately think that the person probably got a bad grade in statistics.

I don't why this happens, but it does - and I'm not the only one. So keep that in mind if you are ever asked about the *standard Normal* in a job interview and such.

And since we're here: avoid at all costs the expression *bell curve* unless you're specifically describing about the shape of the distribution. Every time someone says "the bell curve distribution", I nod and smile politely while silently judging the person for their lack of statistical street smarts.


