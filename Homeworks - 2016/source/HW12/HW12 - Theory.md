# HW12 - Due May 5th, Friday

<font size=1>This is our last homework 🎉 Note the deadline is longer than usual</font>

There is no separate programming section for this homework, but you're free to use Python however you like in these exercises.

### GPS Error

Every output of a GPS system is affected by many factors, so that they can never pinpoint the position of their target with complete accuracy. However, let's imagine that a company called BestGPS advertises that they have the most accurate system. You decide to put that claim to a test.

Measurement errors can be represented by random variables $X_1, X_2, \cdots, X_n \sim Normal(0, \sigma^2)$. You know that BestGPS's competitors' measurement errors have mean zero and variance 9 units. Therefore, you'd like to know whether the variance of BestGPS's measurement error is at most units.

1) Formalize an appropriate pair of null and alternative hypotheses given the setup above.

2) Find a MOM estimator for $\sigma^2$, and then compute an estimate using the following data.

| | $X_1 $ | $X_2$| $X_3$| $X_4$| $X_5$| $X_6$ | $X_{7}$ | $X_{8}$ | $X_{9}$ |
|:---: |:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Data | 1.85 | 3.43 | 0.05 | -1.02 | 1.11 | 1.69 | 2.42 | 2.54 | -1.77 | 

3) The estimator $\sigma^2_{MOM}$ you found above has the following property:

$$\frac{n}{\sigma^2}\sigma_{MOM}^2 \sim \chi^2_{n-1}$$

where $\sigma^2$ is the true variance. Using this information, check whether you would reject the null or not at a 5% level of significance.


### Mean Sleep Time

You have the following data on students' sleep time $T_{1}, \cdots, T_{16}$. 

Let's denote the true mean $E[T_i]$ by $\mu$, and you have an estimate $\mu_{MOM} = 7.5$.

1. Assume the data is Normal, and you know for sure that $\sigma^2 = 4$. Find a 98% confidence interval for $\mu$.

2. Assume the data is Normal, and you only have an estimate $\sigma_{MOM} = 4$. Find a 98% confidence interval for $\mu$.



### Seat belt usage

In a certain high school, 800 out of 1000 female 12th graders said they always use a seatbelt when driving. Construct a 95% confidence interval for the *proportion* who always use a seatbelt when driving.

<b>Hint</b> Begin by modelling this scenario as the outcome of $Bernoulli(p)$ random variables. You are being asked to provide a 95% confidence interval for $p$.



### Basic concepts about joints and conditionals

Given the following discrete joint distribution

<center>
<img src="table3.png" width=250>
</center>


1) Find the PMF of $X$

2) Find the conditional PMFs of $Y$ given $X = 1, 2, 3$. 

3) Find value of the joint CDF at $X = 3$ and $Y = 1$

4) Find $Cov(X,Y)$

5) Find $Corr(X,Y)$

6) Find $Var(X + Y)$

7) Find $Var(X - Y)$

8) Plot the function $E[Y|X=x]$ for $x = 1, 2, 3$.



### Joint Uniform

<center>
<img src="joint_uniform_2.jpg" height = 250>
</center>

$$f_{XY}(x,y) = 
\begin{cases}
\frac{1}{???} \qquad \text{ if } -1 \leq x \leq 2 \text { and } 0 \leq y \leq 10 \\\
0 \qquad \text{otherwise}  
\end{cases}$$

<br>

1) Find the value of "???" that makes $f_{XY}$ a valid probability distribution.

2) If we draw a pair of numbers $X,Y$ from this distribution, what is the probability that $X \geq 0$ and $Y \leq 5$?


### Customer spending

Suppose that the number of people entering a department store on a given day is a random variable $N$ with $E[N]=100$. Suppose further that the amount of money spent by these customers are independent random variables $X_1, \cdots, X_N$ with a common expectation $E[X_i] = 10$. Suppose also that the amount of money spent by a customer is independent of $N$. *Using the law of iterated expectations*, find the expected amount of money spent in the store on a given day.


### Causality and Correlation

<font size=1>If you take Econometrics, you'll be doing a lot of thought experiments like the one below!</font>

[Open-ended  but not optional] Imagine the company that you work for often holds weekend workshops for their employees. Any employee can register to these programs for free and get extra training on, say, interpersonal skills, or advanced Excel, or accounting, etc. 

However, these workshops cost the company a lot of money, and it's not clear whether these workshops really improve the employees' overall productivity. You're asked to test whether that's true or not.

1. If you could perform *any* experiment, what kind of experiment would you perform in order to test the efficacy of weekend workshops?
2. Suppose you analyze data on "hours in workshops" and "employee output". These are historical data that did not come from any sort of formal experiment. You find a positive correlation between output and workshop training. Would you say that establishes that job training makes workers more productive? Explain why or why not.





