# HW11 - Due April 21st (Wed)

### Q1 Basics

Explain the following expressions *in your own words*. You can also use illustrations or word examples if you want.

1) p-value
<font color="blue">
The pvalue is a measure of how much the null hypothesis agrees with the data. When the pvalue is small, the likelihood of the null hypothesis being true is small. 
</font>

2) Significance level
<font color="blue">
The significance level is threshold below which we reject the null hypothesis.
</font>


3) Reject the null hypothesis
<font color="blue">
When we *reject* the null hypothesis, we're actually saying that *given the data, the likelihood of the null hypothesis being true is very small*.
</font>

### Q2 Study Time

<font size=1>A variant of this question appeared in Fall 2016 final</font>


Let $T_1, \cdots, T_{n}$ be random variables encoding how much time a group of $n$ students spends studying for their final Theology exam, in minutes. Suppose that $T_i \sim Normal(\mu, 4)$. The number $\mu$ is a fixed, but unknown constant (i.e., not a random variable).

The random variable $M = \frac{T_1 + \cdots + T_{n}}{n}$ represents the average time that students studied.

<font color="blue">
<b>Remark</b> The solutions below are abridged. You must be able to derive these by yourself.
</font>

1) What is $E[M]$? (Your answer may be in terms of $\mu$ and $n$)
<font color="blue">
$E[M] = \mu$
</font>

2) What is $Var[M]$? (Your answer may be in terms of $\mu$ and $n$)
<font color="blue">
$Var[M] = \frac{4}{n}$
</font>



3) Note that we haven't introduced any data so far. Let's do that now: here are five data points corresponding for the study times of surveyed students.

<center>

| | $T_1$ | $T_2$ | $T_3$ | $T_4$ | $T_5$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Time | 9 | 11 | 10.5 | 12.5 | 7 |
</center>

Use this data to produce a guess for $\mu$.
<font color="blue">
$\mu_{MOM} = 10.0$
</font>

4) Given your guess above, compute the p-value associated with the one-tailed test *using only a standard Normal probability table*.

$$H_0: \mu = 11.5 \qquad H_a: \mu < 11.5$$
<font color="blue">
0.0465
</font>

5) At the 0.05 significance level, would you reject the null hypothesis?
<font color="blue">
Yes, since the pvalue (i.e., the likelihood of the null hypothesis being true) is smaller than our predetermined threshold of 5%.
</font>

6) Again given the guess you produced in part 3, compute the p-value associated with the two-tailed test *using only a standard Normal probability table*.

$$H_0: \mu = 11.5 \qquad H_a: \mu \neq 11.5$$
<font color="blue">
0.0930
</font>

7) At the 0.05 significance level, would you reject this null hypothesis?
<font color="blue">
No. 
</font>


8) Your answers to parts 4-7 have still been different if, instead of Normal, the $T_i$s were distributed as some other continuous distribution?
<font color="blue">
Yes, because by the CLT we have that $\mu_{MOM} \sim^a Normal(\mu, \frac{4}{n})$. 
</font>

### Q2 Coffee cups

You decide to study the lifestyle of a grad student at BC by checking how much coffee they drink per day. You survey 20 students, whose average daily coffee intake was 800ml. To make things easier, assume you know that coffee intake can be represented by $X_i \sim Normal(\mu, 100^2)$

1) What is the distribution of the MOM estimator for $\mu$? Is your answer the exact distribution, or an approximation?
<font color="blue">
$\mu_{MOM} \sim Normal(\mu, \frac{4}{n})$. 
</font>

2) Compute the p-value associated with the following hypothesis test *using only a standard Normal probability table*.

$$H_0: \mu = 1000 \qquad H_1: \mu \neq 1000$$
<font color="blue">
The pvalue is extremely small, very close to zero.
</font>


3) At the 10% significance level, do you reject the null hypothesis associated with the test above?
<font color="blue">
Yes. Having an extremely small pvalue means that the event of the null hypothesis being true is extremely unlikely.
</font>

### Q3 Exotic MOM

<font size=1>This one is a little harder, but it will really make sure you're on top of the material. If you get stuck, try reviewing PP8 first.</font>

Suppose that you have some data $X_1, \cdots, X_n$ that came from a certain exotic distribution $Dist(\theta)$, and you'd like to formulate a guess for the parameter $\theta$. Naturally, you'll want to use the Method of Moments we learned in the past weeks. By hand computation (or, more likely, by looking it up on Wikipedia), you learn that the first moment of the model is

$$E[X_i] = e^{\theta}$$

To make things a little easier, we'll assume that you already know that $Var[X_i] = 3$.

1) What would be the MOM estimator for the parameter $\theta$?
<font color="blue">
$\theta_{MOM} = \log\left( \frac{X_1 + \cdots + X_n}{n} \right)$
</font>

2) Is $\theta_{MOM}$ Normally distributed?
<font color="blue">
No. Even though, by the CLT, $\frac{X_1 + \cdots + X_n}{n}$ is Normally  distributed, once we take a nonlinear transformation of that (like the log, here), the resulting object is no longer Normal.
</font>

3) Using the data below, compute a MOM estimate for $\theta$.


| | $X_1$ | $X_2$ | $X_3$ | $X_4$ | $X_5$ | $X_6$ | $X_7$ | $X_8$ | $X_9$ | $X_{10}$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Time | 5 | 6 | 5.5 | 7 | 8 | 10 | 4 | 9 | 8 | 7 |
</center>
<font color="blue">
$\theta_{MOM} = \log(6.95) \approx 1.94$
</font>

4) Now suppose you have the following hypothesis.

$$H_{0}: \theta = 1.8 \qquad H_{1}: \theta > 1.8$$

Find out the p-value associated with that hypothesis *using only a standard Normal table*.
<font color="blue">
$pvalue = P(\theta_{MOM} > 1.94$<br>
$\qquad \ = P\left(\log(\frac{X_{1} + \cdots + X_{n}}{n}\right) > 1.94) \qquad \qquad \text{Using the definition of }\theta_{MOM}$<br>
$\qquad \ = P\left(\frac{X_{1} + \cdots + X_{n}}{n} > 6.95\right) \qquad \qquad \text{Taking the exponential of both sides}$<br>
$\qquad \ = 1 - P\left(\frac{X_{1} + \cdots + X_{n}}{n} \leq 6.95\right) \qquad \qquad \text{Taking the exponential of both sides}$

Now *this* is the time to invoke the CLT:

$$\frac{X_{1} + \cdots + X_{n}}{n} \sim^a Normal\left(e^{1.8}, \frac{3}{n}\right)$$

<font size=1>[Can you derive the mean and the variance above? Please make *absolutely* sure that you do]</font>

Now we can standardize and look up the value on the table as usual. Writing 

$$\frac{X_{1} + \cdots + X_{n}}{n} = \sqrt{\frac{3}{10}}Z + e^{1.8} \qquad with \qquad Z\sim Normal(0,1)$$

we have that
$P\left(\frac{X_{1} + \cdots + X_{n}}{n} \leq 6.95\right) = P\left(Z \leq \frac{6.95 - e^{1.8}}{\sqrt{\frac{3}{10}}}\right) \approx 0.9498$

and finally,

$pvalue \approx 1 - 0.9498 \approx 0.0501$
</font>

5) Would you reject the null hypothesis above at the 0.05 significance level? How about at the 0.01 significance level?
<font color="blue">
At the 0.05 significance level we do *not* reject the null hypothesis. It barely clears!

At the 0.01 significance level we also do not reject it.
</font>




