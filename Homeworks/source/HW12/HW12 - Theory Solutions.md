# HW12 - Solutions

<font size=1>This is our last homework 🎉 Note the deadline is longer than usual</font>

There is no separate programming section for this homework, but you're free to use Python however you like in these exercises.

### GPS Error

Every output of a GPS system is affected by many factors, so that they can never pinpoint the position of their target with complete accuracy. However, let's imagine that a company called BestGPS advertises that they have the most accurate system. You decide to put that claim to a test.

Measurement errors can be represented by random variables $X_1, X_2, \cdots, X_n \sim Normal(0, \sigma^2)$. You know that BestGPS's competitors' measurement errors have mean zero and variance 9 units. Therefore, you'd like to know whether the variance of BestGPS's measurement error is at most units.

1) Formalize an appropriate pair of null and alternative hypotheses given the setup above.
<font color="blue">
$$H_0: \sigma^2 = 0 \qquad H_a: \sigma^2 < 9$$
</font>

2) Find a MOM estimator for $\sigma^2$, and then compute an estimate using the following data.

| | $X_1 $ | $X_2$| $X_3$| $X_4$| $X_5$| $X_6$ | $X_{7}$ | $X_{8}$ | $X_{9}$ |
|:---: |:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Data | 1.85 | 3.43 | 0.05 | -1.02 | 1.11 | 1.69 | 2.42 | 2.54 | -1.77 | 

<font color="blue">
The method of moments <b>estimator</b> is
$$\sigma_{MOM}^2 = \frac{1}{n}\sum_i \left(X_i - \frac{X_1 + \cdots + X_n}{n} \right)^2$$

Using the data above, we get the **estimate***

$$\sigma_{MOM}^2 = 2.66$$
</font>

3) The estimator $\sigma^2_{MOM}$ you found above has the following property:

$$\frac{n}{\sigma^2}\sigma_{MOM}^2 \sim \chi^2_{n-1}$$

where $\sigma^2$ is the true variance. Using this information, check whether you would reject the null or not at a 5% level of significance.


<font color="blue">
$\text{p-value} = P(\sigma_{MOM}^2 \leq 2.66)$
$\qquad  \ \  \ = P(\frac{9}{9}\sigma_{MOM}^2 \leq \frac{9}{9}2.66)$
$\qquad  \ \  \ \approx 0.024$
</font>

### Mean Sleep Time

You have the following data on students' sleep time $T_{1}, \cdots, T_{16}$. 

Let's denote the true mean $E[T_i]$ by $\mu$, and you have an estimate $\mu_{MOM} = 7.5$.

1. Assume the data is Normal, and you know for sure that $\sigma^2 = 4$. Find a 98% confidence interval for $\mu$.

<font color="blue">
As done in class:
$$\left [7.5 - 2.33\sqrt{\frac{4}{16}}, 7.5 + 2.33\sqrt{\frac{4}{16}} \right]$$
</font>

2. Assume the data is Normal, and you only have an estimate $\sigma_{MOM} = 4$. Find a 98% confidence interval for $\mu$.

<font color="blue">
As done in class:
$$\left [7.5 - 2.60\sqrt{\frac{4}{16}}, 7.5 + 2.60\sqrt{\frac{4}{16}} \right]$$

Where the value $2.60$ is the 0.99-quantile of the $t_{15}$ distribution.
</font>

### Seat belt usage

In a certain high school, 800 out of 1000 female 12th graders said they always use a seatbelt when driving. Construct a 95% confidence interval for the *proportion* who always use a seatbelt when driving.

<b>Hint</b> Begin by modelling this scenario as the outcome of $Bernoulli(p)$ random variables. You are being asked to provide a 95% confidence interval for $p$.

<font color="blue">
Since we are plugging an estimate of the variance, we technically should use the $t_{999}$ distribution to find the critical values. But for $n = 1000$, the Normal and Student-t critical values are so similar that it doesn't matter. Either way we will end up with the following confidence interval.
$$\left [0.8 - 1.96\sqrt{\frac{0.8(0.2)}{1000}}, 0.8 + 1.96\sqrt{\frac{0.8(0.2)}{1000}} \right]$$
</font>


### Basic concepts about joints and conditionals

Given the following discrete joint distribution

<center>
<img src="table3.png" width=250>
</center>


1) Find the PMF of $X$
<font color="blue">
$p_X(x) =
\begin{cases}
0.3 \qquad \text{if }x = 1 \\\
0.3 \qquad \text{if }x = 2 \\\
0.4 \qquad \text{if }x = 3 \\\
0 \qquad \text{otherwise}
\end{cases}
$
</font>

2) Find the conditional PMFs of $Y$ given $X = 1, 2, 3$. 

<font color="blue">
$p_{Y|X}(y|1) =
\begin{cases}
\frac{1}{6} \qquad \text{if }y = 0 \\\
\frac{1}{6} \qquad \text{if }y = 1 \\\
\frac{2}{3} \qquad \text{if }y = 2 \\\
0 \qquad \text{otherwise}
\end{cases}
$

$p_{Y|X}(y|2) =
\begin{cases}
\frac{1}{6} \qquad \text{if }y = 0 \\\
\frac{1}{3} \qquad \text{if }y = 1 \\\
\frac{1}{2} \qquad \text{if }y = 2 \\\
0 \qquad \text{otherwise}
\end{cases}
$

$p_{Y|X}(y|3) =
\begin{cases}
\frac{1}{2} \qquad \text{if }y = 0 \\\
\frac{1}{4} \qquad \text{if }y = 1 \\\
\frac{1}{4} \qquad \text{if }y = 2 \\\
0 \qquad \text{otherwise}
\end{cases}
$
</font>


3) Find value of the joint CDF at $X = 3$ and $Y = 1$
<font color="blue">
$F_{XY}(3,1) = 0.55$
</font>

4) Find $Cov(X,Y)$
<font color="blue">
$\begin{align}
Cov(X,Y) 
&= 0.05 \times( 0 - 1.15 ) \times( 1 - 2.1 ) \\\
&+ 0.05 \times( 0 - 1.15 ) \times( 2 - 2.1 ) \\\
&+ 0.2 \times( 0 - 1.15 ) \times( 3 - 2.1 ) \\\
&+ 0.05 \times( 1 - 1.15 ) \times( 1 - 2.1 ) \\\
&+ 0.1 \times( 1 - 1.15 ) \times( 2 - 2.1 ) \\\
&+ 0.1 \times( 1 - 1.15 ) \times( 3 - 2.1 ) \\\
&+ 0.2 \times( 2 - 1.15 ) \times( 1 - 2.1 ) \\\
&+ 0.15 \times( 2 - 1.15 ) \times( 2 - 2.1 ) \\\
&+ 0.1 \times( 2 - 1.15 ) \times( 3 - 2.1 ) \\\
& = -0.2675
\end{align}$
</font>

5) Find $Corr(X,Y)$
<font color="blue">
First, we have that
$\begin{align}
Var(X) &= 0.3\times (1 - 2.1)^2 + 0.3\times (2 - 2.1)^2 + 0.4\times (3- 2.1)^2 = 0.69 \\\
Var(Y) &= 0.3\times (0 - 1.15)^2 + 0.3\times (1 - 1.15)^2 + 0.4\times (2- 1.15)^2 = 0.7275
\end{align}$

Plugging those values into the covariance formula
$\begin{align}
Corr(X,Y) = \frac{-0.2675}{\sqrt{0.69\times 0.7275}}
\end{align}$
</font>

6) Find $Var(X + Y)$
<font color="blue">
$Var(X + Y) = Var(X) + Var(Y) + 2Cov(X,Y) = 0.69 + 0.7275 - 2\times 0.2675$
</font>

7) Find $Var(X - Y)$
<font color="blue">
$Var(X - Y) = Var(X) + Var(Y) + 2Cov(X,Y) = 0.69 + 0.7275 + 2\times 0.2675$
</font>

8) Plot the function $E[Y|X=x]$ for $x = 1, 2, 3$.

<img src="sol.png" height = 200>


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
<font color="blue">
$30$
</font>

2) If we draw a pair of numbers $X,Y$ from this distribution, what is the probability that $X \geq 0$ and $Y \leq 5$?
<font color="blue">
$P(X \geq 0, Y \leq 5) = \frac{1}{3}\times2\times 5 $
</font>

### Customer spending

Suppose that the number of people entering a department store on a given day is a random variable $N$ with $E[N]=100$. Suppose further that the amount of money spent by these customers are independent random variables $X_1, \cdots, X_N$ with a common expectation $E[X_i] = 10$. Suppose also that the amount of money spent by a customer is independent of $N$. *Using the law of iterated expectations*, find the expected amount of money spent in the store on a given day.

<font color="blue">
Before pluging into the computation, let's think about the problem. Intuitively, since on average there are 100 customers, and each customer spends on average 10 dollars, we'd expect the total amount of store revenue to be $10 \times 100 = 1000$.

Now, let $Y = X_1 + \cdots + X_N$. This is the total amount spent by all $n$ customers. We are looking for $E[Y]$. Here's how we can think about this problem.

+ Sometimes we receive only one customer. Conditional on receiving only one customer, the average revenue is $E[Y|N=1] = E[X_1] = 10$

+ Sometimes we receive two customers. Conditional on receiving two customers, the average revenue is $E[Y|N=2] = E[X_1 + X_2] = 20$

+ Sometimes we receive three customers. Conditional on receiving three customers, the average revenue is $E[Y|N=3] = E[X_1 + X_2 + X_3] = 30$

+ And so on$\cdots$

+ In general, *given that* receive $N$ customers, the average revenue will be $E[Y|N] = 10N$. 

Now we can take the expectation again, this time over all possible values of $N$:

$$E[Y] = E[E[Y|N]] = E[10N] = 10E[N] = 1000$$

See how we took one expectation (over $X_i$) and then another (over $N$) to get an average-average? This is the idea behind the law of *iterated* expectations.
</font>

### Causality and Correlation

<font size=1>If you take Econometrics, you'll be doing a lot of thought experiments like the one below!</font>

[Open-ended  but not optional] Imagine the company that you work for often holds weekend workshops for their employees. Any employee can register to these programs for free and get extra training on, say, interpersonal skills, or advanced Excel, or accounting, etc. 

However, these workshops cost the company a lot of money, and it's not clear whether these workshops really improve the employees' overall productivity. You're asked to test whether that's true or not.

1. If you could perform *any* experiment, what kind of experiment would you perform in order to test the efficacy of weekend workshops?
2. Suppose you analyze data on "hours in workshops" and "employee output". These are historical data that did not come from any sort of formal experiment. You find a positive correlation between output and workshop training. Would you say that establishes that job training makes workers more productive? Explain why or why not.

<font color="blue">
[There is more than one answer to this question. This is mine.]

One concern in job training programs is *self-selection*: it's more common for highly motivated indiviuals to attend the training. When we have no measure of motivation or ability, this causes problems for anyone trying to analyze the *causal effect* of job training on productivity, because motivated and able individuals are more likely to be more productive *regardless* of attending any kind of workshop. 

One way to break away from this problem would be to randomize and enforce job training. Think about the scenario where each worker draws from a lottery, and the winners *must* attend the job training program. In that case, selection into the program really has nothing to do with the workers' motivation or abiliity, so if we see an increase in productivity, we can ascribe this effect to the program, and not to some unobserved ability that the workers already had.

Of course, this system might not be always ethical, and even when it is, it's not perfectly enforceable!

--

Obviously, this was a silly example, but we can think of many other situtations where an unobserved *confounding factor* could prevent us from determining the exact causal effect of a variable of interest. Common economic examples include: does financial openness cause economic development? Does education increase income? Does a decline in fertility promote education? Etc. In Econometrics, you'll learn how to deal with several of these problems.
</font>






