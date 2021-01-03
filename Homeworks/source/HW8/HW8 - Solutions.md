# HW8 Theory - Solutions

### Q1) Basic definitions

Compute the mean, median, variance and standard deviation of the objects below *without* `scipy.stats` or probability tables.

1. $X \sim Binomial(5, \frac{1}{3})$. 

<font color="blue">
It's often easiest to rewrite Binomials in terms of sum of independent Bernoullis. So let's make

$$X = B_1 + B_2 + B_3 + B_4 + B_5 \qquad B_i \sim Bernoulli\left(\frac{1}{3} \right)$$


Now, for the mean and variance (I'll leave some questions for your to fill in):

$\begin{align}
E[X] 
&= E[B_1 + B_2 + B_3 + B_4 + B_5] \\\
&= E[B_1] + E[B_2] + E[B_3] + E[B_4] + E[B_5]  \qquad \text{Linearity}\\\
&= 5E[B_1] \qquad\qquad\qquad\qquad \text{All expectations are the same}\\\
&= 5\frac{1}{3} \qquad\qquad\qquad\qquad \text{Expectation of Bernoulli (right?!)}
\end{align}$

$\begin{align}
Var[X] 
&= Var[B_1 + B_2 + B_3 + B_4 + B_5] \\\
&= Var[B_1] + Var[B_2] + Var[B_3] + Var[B_4] + Var[B_5]  \qquad \text{Not linearity! (then why?)}\\\
&= 5Var[B_1] \qquad\qquad\qquad\qquad \text{All variances are the same}\\\
&= 5\frac{1}{3}\frac{2}{3} \qquad\qquad\qquad\qquad \text{Variance of Bernoulli (why?)}
\end{align}$

The standard deviation is the square root of that, hence

$SD[X] = \sqrt{\frac{10}{9}}$

The median will be the first outcome whose cumulative probability crosses 0.5.

| Outcome | Probability | Cumulative |
|-------|------|-------|
| 0 | $\dbinom{5}{0}(\frac{1}{3})^0(\frac{1}{3})^5 = 0.132$ | 0.132 | 
| 1 | $\dbinom{5}{1}(\frac{1}{3})^1(\frac{1}{3})^4 = 0.329$ | 0.461 | 
| 2 | $\dbinom{5}{2}(\frac{1}{3})^2(\frac{1}{3})^3 = 0.329$ | 0.79 | 
| 3 | $\dbinom{5}{3}(\frac{1}{3})^3(\frac{1}{3})^2 = 0.165$ | 0.955 | 
| 4 | $\dbinom{5}{4}(\frac{1}{3})^4(\frac{1}{3})^1 = 0.041$ | 0.996 | 
| 5 | $\dbinom{5}{5}(\frac{1}{3})^5(\frac{1}{3})^0 = 0.004$ | 1.0 | 

Hence $Med[X] = 2$.
</font>
 
2) $Y \sim Uniform(0, 2)$ 
<font color="blue">

Make sure you know how to evaluate the integrals!

$E[Y] = \int_0^2 y \frac{1}{2} dy = 1$

$Var[Y] = \int_0^2 (y - 1)^2 \frac{1}{2} dy = \frac{4}{12}$

$SD[Y] = \sqrt{\frac{4}{12}}$

$Med[Y] = 1$ (Half of the probability is to the left of 1, half to its right)

</font>

3) The list of numbers $1,2,3,4,5,5,10$
<font color="blue">
The best way to deal with lists of numbers is to treat relative frequencies as probabilities. As if we had a random variable $W$ with the following PMF:

| Outcomes ($w$) | 1 | 2 | 3 | 4 | 5| 10 | 
|---|---|---|---|---|---|---|---|---|
| Probabilities $P(W = w)$ | $\frac{1}{7}$ | $\frac{1}{7}$ | $\frac{1}{7}$ | $\frac{1}{7}$ | $\frac{2}{7}$ | $\frac{1}{7}$ 

Now we just proceed as in part 1.

$Mean = E[W] = \frac{1}{7}1 + \frac{1}{7}2 + \cdots + \frac{1}{7}10 = \frac{30}{7}$

$Variance = Var[W] = \frac{1}{7}(1 - \frac{30}{7})^2 + \cdots + \frac{1}{7}(10 - \frac{30}{7})^2 \approx 7.346938$

$Standard Deviation = SD[W] \approx \sqrt{7.346938}$

$Median = 4$ (The first number whose cumulative probability crossses 0.5) [*]


[*] For discrete random variables, the median isn't really well-defined. Sometimes there will be multiple numbers that could be called "median". In that case, you can take their average, or choose the smallest one. Taking the average is what you're usually taught in AP stats, but for mathy purposes, taking the smallest such number makes the most sense. (i.e., it makes proofs about the median easier).
</font>


### Q2) Properties of the variance

Let $X$ be any random variable with finite variance, and let $a$ be a constant. Using the definition of variance and what you know about expectation, prove the following.

1. $Var[aX] = a^2Var[X]$
1. $Var[X + a] = Var[X]$
2. $Var[X] = E[X^2] - E[X]^2$

<font color="blue">
1) $Var[aX] = a^2 Var[X]$

$\begin{align}
Var[aX] 
&= E[(aX - E[aX])^2] \qquad \text{Definition of Var} \\\
&= E[(aX - aE[X])^2] \qquad \text{Linearity of inner E} \\\
&= E[a^2(X - E[X])^2] \qquad \text{Pulling a out of the square} \\\
&= a^2E[(X - E[X])^2] \qquad \text{Linearity of outer E} \\\
&= a^2Var[X] \qquad \ \ \  \ \qquad \text{Definition of Var} \\\
\end{align}$

<br><br>

2) $Var[X + a] = Var[X]$

This says that if you shift the whole distribution by $a$, that doesn't change how spread out it is.

$\begin{align}
Var[X + a] 
&= E[(X + a - E[X + a])^2] \qquad \text{Definition of Var} \\\
&= E[(X + a - E[X] - a)^2] \qquad \text{Linearity of inner E} \\\
&= E[(X - E[X])^2] \qquad \ \ \ \ \qquad a\text{'s cancel out} \\\
&= Var[X] \qquad \qquad \qquad \qquad \text{Definition of Var} \\\
\end{align}$


2) $Var[X] = E[X^2] - E[X]^2$

<b>Remark</b> Some of you clearly googled the answer to this one. That's very disappointing, because the solution was totally within your reach. You lost a valuable chance to get some practice with variances and expectations, but --  more importantly -- you lost a chance of learning how to write a proof and think logically. You should feel very bad about chickening out of this relatively minor challenge. <a href="https://www.youtube.com/watch?v=SrDSqODtEFM">Shame</a>.

$\begin{align}
Var[X] 
&= E[(X - E[X])^2] \qquad \qquad \qquad  \text{Definition of Var} \\\
&= E[X^2 - 2XE[X] + E[X]^2] \qquad \text{Expanding the square} \\\
&= E[X^2] - E[2XE[X]] + E[E[X]^2] \qquad \text{Linearity of outer E} \\\
&= E[X^2] - 2E[X]E[X] + E[E[X]^2] \qquad \text{Linearity of middle E: (2E[X] is a constant)} \\\
&= E[X^2] - 2E[X]E[X] + E[X]^2 \qquad \text{Linearity of rightmost E: E[X]^2 is a constant, pops out} \\\
&= E[X^2] - 2E[X]^2 + E[X]^2 \qquad \text{E[X]E[X] = E[X]^2} \\\
&= E[X^2] - E[X]^2 \qquad \qquad \qquad \text{Simplifying} \\\
\end{align}$

</font>

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

1) $P(Z \leq 0)$ <font color="blue"> 0.5 </font>

2) $P(Z > 3)$ <font color="blue"> 0.0013 </font>
3) $P(-1 \leq Z \leq 1)$ <font color="blue"> About 1.68 </font>
4) The 0.9-quantile of $Z$ [i.e., the number $c$ so that $P(X \leq c) = 0.9$] <font color="blue"> About 1.65 </font>
5) The 0.1-quantile of $Z$ [i.e., the number $c$ so that $P(X \leq c) = 0.1$] <font color="blue"> About -1.65 </font>

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

<font color="red"><b>🚨CANCELLED🚨</b>

There was a typo in the question. I warned about it on <a href="https://piazza.com/class/ixrnw1uhjtdyi?cid=141">Piazza</a> but I believe not everyone got to see that in time. The solutions below refer to the corrected version.
</font>

<font color="blue">
6-7 FIXED) We want choose $a$ and $b$ smartly so that $X = aZ + b$.

+ What is $E[X]$ as a function of $a$ and $b$?
+ What is $Var[X]$ as function $a$ and $b$?
+ You know that $E[X] = 3$ and $Var[X] = 4$. What must $a$ and $b$ be for this to be true?

<b>Answers</b>
$E[X] = aE[Z] + b = a\cdot 0 + b = b$
$Var[X] = a^2Var[Z] = a^2\cdot 1 = a^2$
Therefore $b = 3$ and $a = 2$.
</font>

8) Find out $P(X \leq 1)$

<font color="blue">
$
\begin{align}
P(X \leq 1) 
&= P(2Z + 3 \leq 1) \\\
&= P\left(Z \leq \frac{1 - 3}{2}\right) \\\
&= P(Z \leq -1) 
\end{align}$

Querying the table, we see that the answer is approximately $0.1586$.
</font>

<font size=1>By the way, in the Programming Practice you'll learn how to query these probabilities without going through these shenanigans.</font>

<font color="blue">
By which I meant:

```python
dist = ss.norm(3, 2)  
prob = dist.cdf(1)
print(prob)
```

which prints out

```python
0.158655253931
```
</font>
### Q4) Waiting for good dollars

You'd like to sell your car, and decide to sell it to the first person to offer at least $5000$ for it. Let's call such offers *acceptable*.

Each offer is a random variable: $X_1$ is the first offer you receive, $X_2$ is the second, and so on.  Assume each one comes from the same distribution, $Normal(4000, 10^6)$ [that's mean $4000$ and *variance* a million] and that they are all independent of each other. 

1) What's the probability that any offer is *acceptable*?
<font color="blue">
Once again we need to rewrite $X$ in terms of a standard Normal random variable. Following the procedure above we see that

$X = 1000Z + 4000$

The answer is

$P(X \geq 5000) = P(Z \geq \frac{5000 - 4000}{1000}) = P(Z \geq 1) = 0.1586$
</font>

2) What is the expected number of offers you will receive until an acceptable one comes along?

<font color="blue">
Since we're looking for *number of trials before a success*, you should be thinking about Geometric random variables.

Let $W$ count the number of offers you'll receive until an acceptable one comes along (including the successful one). Then $W \sim Geometric(0.1586)$, and $E[W] = \frac{1}{0.1586}$.
</font>


3) Suppose you know that an offer is acceptable. What is the probability that this (already known to be acceptable) offer is larger than $6000$ dollars?

<b>Hint</b> Last question in the midterm

<font color="blue">
Define these two events. 

A: Offer is larger than 6000 dollars
B: Offer is acceptable

In terms of these events, we're looking for $P(A|B)$. From the conditional probability formula,

$P(A|B) = \frac{P(A \cap B)}{P(B)} = \frac{P(A)}{P(B)} = \frac{P(X > 6000)}{P(X > 5000)}$

Rewriting in terms of $Z$, consult the table, and we've got that

$P(A|B) = \frac{0.0227}{0.1586}$
</font>

4) Find the number $c$ so that $90\%$ of the offer probabilities will fall within the interval $[4000 - c, 4000 + c]$.

<b>Hint</b> Think about quantiles.



<font color="blue">
Following the <a href="https://piazza.com/class/ixrnw1uhjtdyi?cid=146">hints on Piazza</a>.

> There are two pieces in this puzzle.

> 1) Since we will end up checking out a probability in a standard Normal probability table, we must rewrite $X \sim Normal(4000, 10^6)$ in terms of a standard Normal random variable, say $Z \sim Normal(0, 1)$.

> We can rewrite $X$ as $X = aZ + b$, since to get $X$ we're shifting $Z$ by $b$ and then rescaling it $a$.

As above: $X = 10^3Z + b$.

> 2) Since we want the middle 90% chunk of the probability, we're in fact looking for the 0.05 and 0.95 quantiles of the distribution. That is, we're looking for the $c$ that satisfies

> $P(X \leq 4000 - c) = 0.05$ and $P(X \leq 4000 + c) = 0.95$

We can solve either one of the two equations above. Choosing the rightmost one:

$\begin{align}
0.95 
&= P(X \leq 4000 + c) \\\
&= P(10^3Z + 4000 \leq 4000 + c) \\\
&= P\left(Z \leq \frac{c}{10^3} \right) \\\
\end{align}$

Querying the table, we see that the $c$ we're looking for must satisfy $\frac{c}{10^3} = 1.645$, or $c = 1645$.


</font>

----

##### A possibly humorous but not entirely untrue personal remark

Because undergraduate textbooks often use $Z$ exclusively for standard Normal random variables, some people end up calling the standard Normal distribution *the $Z$ distribution*. Likewise, the standard Normal probability table is called the *$Z$-table* by such people. And (as you'll see later) tests that involve the standard normal distribution are called *$Z$-tests*. 

But look, you shouldn't do that.

For whatever reason, I've never seen a reputable researcher use the expression "the Z distribution". This also shows up in zero of the advanced textbooks that I've read. So if someone says "the Z distribution" to me, I immediately think that the person probably got a bad grade in statistics.

I don't why this happens, but it does - and I'm not the only one. So keep that in mind if you are ever asked about the *standard Normal* in a job interview and such.

And since we're here: avoid at all costs the expression *bell curve* unless you're specifically describing about the shape of the distribution. Every time someone says "the bell curve distribution", I nod and smile politely while silently judging the person for their lack of statistical street smarts.


