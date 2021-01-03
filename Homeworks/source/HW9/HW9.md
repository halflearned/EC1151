# HW9 Theory - Due Wed Apr 12th 


<font size=1>To find out the probabilities in these questions, feel free to either use probability tables or query the CDFs, PMF/PDFs and PPFs in `scipy.stats`. However, you are **not** to use simulations this time. Also, expectations and variances should be computed by hand, using sums and integrals and such. You can still check your work in Python, but you must show your derivations.</font>


### Q1 Sleep time

In a certain town, the time teenagers sleep every night can be described by a random variable $T_{i} \sim Uniform[6,10]$.

1) What is $E[T_{i}]$?

2) What is $Var[T_{i}]$?

3) Suppose that in that town there are 20 teenagers. Use the Central Limit Theorem to find an approximation to $P(T_{1} + T_{2} + \cdots + T_{20} > 160)$.

    
    
### Q2 Sodium content 

For this question, you should learn the following fact:

> <b>Fact</b> The sum of independent Normally distributed random variables is Normal: if

> $$X \sim Normal(m_1, v_1) \qquad Y \sim Normal(m_2, v_2)$$

> and $X$ and $Y$ are independent, then 

> $$X + Y \sim Normal(m_1 + m_2, v_1 + v_2)$$

> So the distribution is the same, and the parameters just add. Easy!
> 
> <b>Remark</b> No other distribution you learned in our class has this property! Sum of Bernoullis becomes Binomial (not Bernoulli), and sum of two Uniforms is Triangle (not Uniform), etc. Also, by the Central Limit Theorem, the sum of many independent rvs, regardless of their distribution, is approximately Normal!


Due to small variations in the ratio of ingredients used, the sodium content in each soup can produced by a certain food factory can be described by a $Normal(480, 10^2)$ random variable. Suppose you collected 200 such soup cans, and you're about to check their sodium level. Let $X_1, X_2, \cdots, X_{200}$ be the sodium level in each can.

1) Let $S$ be the *sum* of all sodium content in these 200 cans:
    
$$S = X_{1} + X_{2} + \cdots + X_{200}$$
    
What is the exact probability distribution of $S$? Give the name of the distribution and the numerical value of its parameters.
    
2) What is the exact probability that $P(S < 95800)$?
    
3) Let $Z$ be the *average* of all sodium content in these 200 cans:
    
$$Z = \frac{X_{1} + X_{2} + \cdots + X_{200}}{200}$$

What is the *exact* distribution of $Z$? Give its name and the numerical value of its parameters.
    
4) Find out a number $c$ such that the $P(480 - c < Z < 480 + c) = 0.90$
    
<b>Hint</b> Think about quantiles. A similar question has been asked in HW8.
    
5) Would your answers to parts 1-4 change in any way if I told you that $E[X_{i}] = 480$, $Var[X_{i}] = 10^2$, but $X$ is *not* Normally distributed? If so, how?

6) If you had sampled a larger number of cans, say $1000$ instead of $200$, would the number $c$ you would have found in part 3 be larger, smaller or equal to the number $c$ you found with $200$ cans? Explain your reasoning.

<b>Hint</b> You don't have to recompute $c$. What happens to the variance of averages as $n \rightarrow \infty$?
    
    
### Q3 BC Cafeteria 

You're about to poll 120 BC undergraduates on whether or not they agree that the BC cafeteria food is too expensive. Let $X_{1}, X_{2}, \cdots, X_{120}$ be $Bernoulli\left(\frac{9}{10}\right)$ random variables, where $X_{i} = 1$ if the $i^{th}$ student agrees, and $0$ otherwise.

1) Let $Y$ be the *total* number of students who agree with the statement above. What is the exact distribution of $Y$? Give its name and the numerical value of its parameters.

2) Find out $E[Y]$ and $Var[Y]$.

<b>Hint</b> For the variance, use the fact that the variance of the sum of *independent* random variances equals the sum of the individual variances.

3) *Using the Central Limit Theorem*, find out an *approximate* probability that 117 students or more will agree that the food is way too expensive.

4) Let $Z$ be the *average* number of students who agreed, i.e.,

$$Z = \frac{X_1 + \cdots + X_{120}}{120}$$

What is the approximate probability distribution of $Z$? Give the name of the distribution and its parameters.

5) Using the approximation above, find out $P(Z > 0.975)$.

6) If you had polled $1200$ students instead of just $120$, would you answer to part $5$ be larger or smaller? 

<b>Hint</b> You don't have to recalculate the probabilities, only justify your answer using one of the limit theorems.

7) [Open ended] This time, let's suppose that you *did not know* the model that generated the random variables $X_{i}$s. Since the answers can be only yes or no, the distribution is obviously $Bernoulli(p)$, but the value of the parameter $p$ is unknown.

Now let's pretend that when you polled the 120 students, the number of students who answered they agree was only 100 out of the 120. Would you have guessed that $p = \frac{9}{10}$? 
If not: what would you have guessed for $p$? 
If so: how low would the number of students have to be so that you'd *stop* believing that $p = \frac{9}{10}$?

Take your time here, and try to justify your answer as formally as you can. Thinking hard about this question will prepare you for the next module.

### Q4 [Open-ended] Why do simulations work?

In PP7, we computed the area of a circle using simulations. Explain from scratch what you did, and why the whole process works. In particular, discuss of role of the law of large numbers and why more simulations lead to higher accuracy.

<b>Remark</b> Pretend that you're teaching the material to a friend who missed that class. You can explain the high-level idea intuitively, but also make sure to include enough formal detail that your friend would be able to follow the class slides, and answer a question or two about this in the final exam. Your answer can be as long or as short as you deem necessary (within reason!).

