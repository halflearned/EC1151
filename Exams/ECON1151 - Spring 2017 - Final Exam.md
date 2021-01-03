# ECON1151 - Spring 2017 - Final Exam


### Q1 [5 points each] Basic concepts 

Answer each of the following questions *in no more than one paragraph*. If you find it easier, feel free to include real life examples or graphs in your explanation, but try to be as mathematically precise as you can.


<b>Independence</b> If two events $A$ and $B$ are independent, then their probabilities multiply:

 $$P(A \cap B) = P(A)P(B)$$ 
 
Where is this formula coming from? 

<b>CLT</b> The central limit theorem states that if a random variable $Y$ is the sum of many independent and identically distributed random variables, then $Y$ is approximately Normal. What is the intuition behing this result? (e.g., why would the sum of many independent Uniform random variables not be Uniform, for example?)

<b>Linearity</b> The expectation operator has the *linearity* property, that says that, for random variables $X,Y$ and constant $c$, the following holds.

$$E[X + Y] = E[X] + E[Y] \qquad E[cX] = cE[X]$$ 

Please explain the second linearity property: $E[cX] = cE[X]$. Why can we "take the constants out"?

<b>Correlations</b> Why do we observe such a high *estimated* correlation between the two variables below? Give at least one reason.

<center>
<img src="correlations.png" width = 400>
</center>

<div style="page-break-after: always;"></div>

### Q2 [10 points] Shiny Eyed Bayes

In a hat there are eleven coins, numbered 0 to 10. Each coin has a different probability of landing Heads, so that coin 1 has probability $0.1$, coin 2 has probability $0.2$, coin 7 has probability $0.7$, and so on, with coin $n$ having probability $0.1n$ of landing Heads. This also means that coin 0 is double-tailed and coin 10 is double-headed.

In a moment, I will pick one coin at random, flip it once, and tell you the outcome. But first, let's define the following events.

+ $A_n$: Event that I pick the $n^{th}$ coin (for $n = 0,\cdots, 10$)
+ $B$:  Event that the coin lands Heads.

Okay, so I flipped the coin once and $B$ happened. Given that, find a general expression for $P(A_n | B)$ in terms of $n$.

<b>Hint</b> For partial points, find pieces of the answer like $P(B|A_0), \cdots, P(B|A_{10})$, $P(A_n)$, $P(B)$, and explain how these pieces fit together.

--

### Q3 [10 points] Transformations and relationships

You are given the following independent random variables.

+ $Z_1, Z_2, Z_3, Z_4 \sim Normal(0,1)$ 
+ $U \sim Uniform[0,1]$ 

Please compute the following.

1. If $W = U^3$, then what is $P\left(W \leq \frac{1}{27}\right)$?
2. If $Y = 4Z_1 + 1$, then what is $P(Y \leq 2)$?
3. If $X = Z_1^2 + Z_2^2 + Z_3^2 + Z_4^2$, then what is $P(X \leq 0.3)$?


<div style="page-break-after: always;"></div>

### Q4 [15 points] Book length 

The number of pages in a young adult novel can be modeled by a $Normal(\mu, \sigma^2)$ distribution. You would like to estimate the value of $\mu$, so, as an experiment, you randomly click on books of this genre in the Amazon website and check their description[*]. 

The average of the first sixteen books you sampled was 250 pages.

1. Derive the method of moments estimator $\mu_{MOM}$ for the parameter $\mu$. Show all the steps in the derivation. Remember to define any variables that you may use.

2. What is the distribution of $\mu_{MOM}$, and why? Is that distribution exact or approximate?

3. Assume for a moment that you know that the variance of the number of pages equals 625. Derive a 95% confidence interval for the true value of $\mu$. Show all the steps in your derivation.

4. Redo the previous question, but now assuming that 625 is only an estimate of the variance. That is, it's the variance of the first sixteen books you happened to sample, but need not equal the true value of $\sigma^2$.

5. The *width* of a confidence interval is the total length between its lower and upper boundaries (e.g, the confidence interval $[1,5]$ has *width* 4). At least how many books $n$ would you have to sample if you wanted your 95%-confidence interval to have width at most 1? (Your answer should be a number, or an expression involving only numbers).


<font size=1>[*] After all, physical bookstores don't really exist anymore.</font>


<div style="page-break-after: always;"></div>
 
### Q5 [15 points] Trash 

The average amount of trash produced by $n$ households in the USA can be described by random variables $X_1, \cdots, X_n \sim Normal(\mu, \sigma^2)$. Both $\mu$ and $\sigma^2$ are unknown. 

You start collecting data. The first four points you collect are

<center>

| Household | $X_1$ | $X_2$ | $X_3$ | $X_4$ |  
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Data | 3 | 4 | 6 | 7 |

</center>

1) Find the method of moments estimators for $\mu$ and $\sigma^2$, and then compute the estimates using the data above.

2) Test at the 5% significance level
$$H_0: \mu = 1.4 \qquad H_a: \mu \neq 1.4$$

2) Test at the 10% significance level
$$H_0: \sigma^2 \geq 10 \qquad H_a: \sigma < 10$$

<b>Hints</b> Two useful facts. 

+ $\frac{n}{\sigma^2}\sigma^2_{MOM} \sim \chi^2_{n-1}$

+ $\sqrt{2.5} \approx 1.6$ 

--

### Q6 [10 points] Extreme trash

Using the exact same setup and data as the *Trash* question, find a 90%-confidence interval for the parameter $\sigma^2$.

<b>Hint</b> We have not constructed confidence intervals for $\sigma^2$ in any of the homeworks or question bank problems. But you can still do it if you follow the usual steps, using the fact that

$$\frac{n}{\sigma^2}\sigma^2_{MOM} \sim \chi^2_{n-1}$$

If you are totally blanking right now, then just leave this question for after you finish most of the rest.

<div style="page-break-after: always;"></div>

### Q7 [10 points] Joint distributions

The outcomes of two coin tosses can be represented by a pair of independent random variables $X_1, X_2 \sim Bernoulli(\frac{1}{2})$. Recall that each one of them can only be 0 or 1!

From these two independent random variables, let's construct two more:

+ $Y = \max\{X_1, X_2\}$ (e.g., if $X_1 = 0$ and $X_2 = 1$, then $Y = 1$)
+ $Z = \min\{X_1, X_2\}$ (e.g., if $X_1 = 0$ and $X_2 = 1$, then $Z = 0$)

1) Fill in a joint probability distribution table like the one below with the appropriate probabilities of $Y$ and $Z$.

<center>

|  | $Y = 0$ | $Y = 1$|  
|:--:|:--:|:--:|:--:|
| $Z = 0$ |   |  |  
| $Z = 1$ |  |   | 

</center>

2) Compute the marginal probability distribution of $Y$.
3) Compute the conditional probability of $Y$ given $Z = 1$.
4) Are $Z$ and $Y$ independent? Answer using the mathematical definition of independence.
5) Compute $Cov[Z,Y]$. (Answer is a number or a simple mathematical expression)
6) Compute $E[Y | Z = 1]$ (Answer is a number or a simple mathematical expression)

--

### Q8 [10 points] Simulations

Several times this semester we used simulations to compute approximate probabilities. Explain why and how that worked as rigorously as you can.

<b>Note</b> You're *not* being asked to write code, but to explain the mathematical machinery that allowed us to compute probabilities via simulations. You answer should mention one of the limit theorems we learned.


<div style="page-break-after: always;"></div>

## Standard Normal table

<img src="normal1.png">

<img src="normal_examples.png">

<div style="page-break-after: always;"></div>

## Student-t table

<img src="t1.png">

<img src="t_examples.png">

<div style="page-break-after: always;"></div>

## Chi-squared table

<img src="chi21.png">


<img src="chi2_examples.png">


