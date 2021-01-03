# HW10 - Theory - Due April 19th (Wed)


### Q1 CLT review

Let's warm up by reminding ourselves of what the Central Limit Theorem (CLT) tells us. Throughout, we will suppose we have independent random variables $X_1, X_2, \cdots, X_n \sim Dist(\theta)$, where $Dist$ is some distribution (not necessarily Normal!), with some parameter $\theta$. 

1) In terms of $E[X_1]$ and $Var[X_1]$, what does the CLT tell us about the following random variable?

$$S = X_1 + \cdots + X_n$$

<font color="blue">

The CLT says that $S \sim Normal(E[S], Var[S])$. Note that it does **not** say what $E[S]$ and $Var[S]$ are. For that, we must further compute
<br>
<br>

$\begin{align}
E[S] &= E[X_1 + \cdots + X_n] \qquad \qquad \text{Def of }\lambda_{MOM}\\\
&= E[X_1] + \cdots + E[X_n] \qquad \qquad \text{Linearity} \\\
&= E[X_1] + \cdots + E[X_n] \qquad \qquad \text{Identical distributions} \\\
&= nE[X_1] \qquad \qquad \text{} \\\
\end{align}$

Similarly, 

$\begin{align}
Var[S] &= Var[X_1 + \cdots + X_n] \qquad \qquad \text{Def of S} \\\
&= Var[X_1] + \cdots + Var[X_n] \qquad \qquad \text{Independence (!)} \\\
&= Var[X_1] + \cdots + Var[X_n] \qquad \qquad \text{Identical distributions} \\\
&= nVar[X_1] \qquad \qquad \text{} \\\
\end{align}$


<b>Remark</b> Many of you skipped several steps in the calculation above. You're missing out on a chance of having me check your logic and your understanding. I'll accept a shorter answer instead of a longer one, but remember you just wasted a great opportunity.
</font>

2) In terms of $E[X_1]$ and $Var[X_1]$, what does the CLT tell us about the following random variable?

$$W = \frac{X_1 + \cdots + X_n}{n}$$

<font color="blue">
The CLT says that $W \sim Normal(E[W], Var[W])$. Note that it does **not** say what $E[W]$ and $Var[W]$ are. For that, we must further compute
<br>
<br>

$\begin{align}
E[W] &= E[\frac{X_1 + \cdots + X_n}{n}] \qquad \qquad \text{Def of S} \\\
&= \frac{1}{n}E[\frac{X_1 + \cdots + X_n}{n}] \qquad \qquad \text{Linearity} \\\
&= \frac{1}{n}\left(E[X_1] + \cdots + E[X_n]\right) \qquad \qquad \text{Linearity} \\\
&= \frac{1}{n}\left(E[X_1] + \cdots + E[X_1]\right)\qquad \qquad \text{Identical distributions} \\\
&= \frac{1}{n}nE[X_1] \qquad \qquad \text{} \\\
&= E[X_1] \qquad \qquad \text{} \\\
\end{align}$

Similarly, 

$\begin{align}
Var[W] &= Var[\frac{X_1 + \cdots + X_n}{n}] \qquad \qquad \text{Def of S} \\\
&= \frac{1}{n^2}Var[\frac{X_1 + \cdots + X_n}{n}] \qquad \qquad Var[aX] = a^2Var[X] \\\
&= \frac{1}{n^2}\left(Var[X_1] + \cdots + Var[X_n]\right) \qquad \qquad \text{Independence} \\\
&= \frac{1}{n^2}\left(Var[X_1] + \cdots + Var[X_1]\right)\qquad \qquad \text{Identical distributions} \\\
&= \frac{1}{n^2}nVar[X_1]  \\\
&= \frac{Var[X_1]}{n}
\end{align}$
</font>


3) Using your answer to part 2, explain why we can say that the Law of Large Numbers is a corollary of the Central Limit Theorem.

<font color="blue">
Using the CLT just found out that (1)

$$\frac{X_1 + \cdots + X_n}{n} \sim^a Normal\left(E[X_1], \  \frac{Var[X_1]}{n}\right)$$

What happens at $n \rightarrow \infty$? The variance becomes increasingly smaller, until the average converges to a constant. That is precisely what the Law of Large Number says: 

$$\frac{X_1 + \cdots + X_n}{n} \rightarrow^p E[X_1]$$

where the $p$ indicates convergence *in probability*, i.e., for finite $n$, the average is still a random variable, but as $n$ increases, the probability that it is far from $E[X_1]$ gets smaller and smaller.
</font>


### Q2 Explaning MOM

[Open Ended] Explain in your own words:

1) What is an estimator?
<font color="blue">
Estimators are functions from data $X_1, \cdots, X_n$ to a guess about the parameter of interest.
</font>

2) What is the method of moments?

<font color="blue"> It a systematic <i>procedure to find estimators</i>. It involves equating the theoretical moments coming from our model to empirical moments coming from the data, until we have enough equations for solving for the unknown parameters.
</font>


3) Why are estimators random variables?
<font color="blue">
Because they are functions of the data, and the data is random!
</font>


4) Can we ever know true value of the parameters that generated our data?
<font color="blue">
Never!
</font>

Your answers can be as short or long as you find necessary -- within reason!

### Q3 Coin toss

<font color="blue">Done in class.</font>

I tossed one coin eight times, and here are the results I got, encoded as $1$ for Heads and $0$ for tails.

<centeR>

| <b>Toss </b> | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| <b>Value</b> | 1 | 0 | 1 |  1 | 1 | 1 | 0 | 0

</center>

Naturally, we can say that each value is 

$$X_i \sim Bernoulli(p)$$

for some value $p$.

1) Find the method of moments estimator for the parameter $p$ and compute an estimate using the data above.

2) What is the *approximate* distribution of the estimator? Give its name and parameters.

3) Suppose the coin was fair. *Using a probability table*, compute the probability of getting an estimate of $p_{MOM}$ at least as large as you got using the data above. Do *not* use Python.

<b>Remark</b> If you're confused by this question, remember that $p_{MOM}$ is a *random variable*, and the value you got is only one possible realization of that random variable. In other words, the question is saying this: 

> "Suppose you generated a *different* data set using the $Bernoulli(\frac{1}{2})$ distribution. Using this *different* data set, you'd get a *new* estimate. What is the probability that the *new* estimate is at least as large as the old one you got from *this* data set?

### Q4 Poisson bankruptcies


<font size=1>

This will be another example of another method of moments estimator that happens to be an average.</font>


The Poisson distribution is used to model the number of rare and independent events. One such use is the number of bankruptcies in a region during a certain period (assuming they are independent). 

<br>Suppose you have the following data on bankrupcties:

<img src="poisson.png" width = 700>

These data were generated by 

$$X_1, \cdots, X_{10} \sim Poisson(\lambda)$$

1) Find the method of moments estimator for the parameter $\lambda$ and compute an estimate using the data above.

<font color="blue">

Equating the model and data moments, the method of moment **estimator** is

$$\lambda_{MOM} = \frac{X_1 + \cdots + X_n}{n}$$

from which we get the **estimate**

$$\lambda_{MOM} = 4.8$$

</font>


2) What is the approximate distribution of the estimator? Give its name and parameters.

<font color="blue">

Looks like the estimator we found happens to be an average. That being the  case, we can invoke the CLT, so that

$$\lambda_{MOM} = Normal(E[\lambda_{MOM}], Var[\lambda_{MOM}])$$

Let's find out what $E[\lambda_{MOM}]$ and $Var[\lambda_{MOM}]$ are...

$\begin{align}
E[\lambda_{MOM}] &= E[\frac{X_1 + \cdots + X_n}{n}] \qquad \qquad \text{Def of S} \\\
&= \frac{1}{n}E[\frac{X_1 + \cdots + X_n}{n}] \qquad \qquad \text{Linearity} \\\
&= \frac{1}{n}\left(E[X_1] + \cdots + E[X_n]\right) \qquad \qquad \text{Linearity} \\\
&= \frac{1}{n}\left(E[X_1] + \cdots + E[X_1]\right)\qquad \qquad \text{Identical distributions} \\\
&= \frac{1}{n}nE[X_1] \qquad \qquad \text{} \\\
&= E[X_1] \qquad \qquad \text{}  \\\
&= \lambda \qquad \qquad \text{Expectation of a Poisson rv}\\\
\end{align}$

Similarly, 

$\begin{align}
Var[\lambda_{MOM}] &= Var[\frac{X_1 + \cdots + X_n}{n}] \qquad \qquad \text{Def of S} \\\
&= \frac{1}{n^2}Var[\frac{X_1 + \cdots + X_n}{n}] \qquad \qquad Var[aX] = a^2Var[X] \\\
&= \frac{1}{n^2}\left(Var[X_1] + \cdots + Var[X_n]\right) \qquad \qquad \text{Independence} \\\
&= \frac{1}{n^2}\left(Var[X_1] + \cdots + Var[X_1]\right)\qquad \qquad \text{Identical distributions} \\\
&= \frac{1}{n^2}nVar[X_1]  \\\
&= \frac{Var[X_1]}{n} \\\
&= \frac{\lambda}{n} \qquad \qquad \text{Variance of a Poisson rv}\\\
\end{align}$

Therefore

$$\lambda_{MOM} \sim Normal(\lambda, \frac{\lambda}{n})$$

</font>

3) Suppose the true value of $\lambda$ is 6. Compute $P(\lambda_{MOM} < 5)$ and $P(\lambda_{MOM} > 7)$ *using a probability table*.

<font color="blue">
Standardizing,

$$\lambda_{MOM} = \sqrt{\frac{6}{10}}Z + 6 \qquad $$

So that $P(\lambda_{MOM} < 5) = P(Z < \frac{5 - 6}{\sqrt{\frac{6}{10}}}) \approx 0.098$.

Similarly for the other probability.

</font>

### Q5 Normal MOM

The data below came from the $Normal(\mu, \sigma^2)$ distribution.

<center>

| <b>Individual</b> | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| <b>Value</b> |  6.11 |  -4.19 |   0.86 | -4.52 |   1.1 |  0.52 |  -0.71 |  10.09 | 0.28 |  2.5 |
 
</center>

1) Find the method of moments estimator for the parameters $\mu$ and $\sigma^2$ and compute estimates using the data above.

2) Explain why the method of moments estimator $\mu_{MOM}$ is Normally distributed.

<b>Hint</b> HW9Q2.

<font color="blue">Sum of Normals is again Normal!</font>

3) Suppose that in reality $\mu = 3$ and $\sigma^2 = 4$. Compute the probability that $\mu_{MOM}$ is at *most* what you got in part 1.

4) [Optional - Not for credit] It will turn out that, for large $n$, the estimator $\sigma_{MOM}^2$ you computed above will also be Normally distributed. However, proving this will require more complicated math than we currently have access to. But why can't we use the CLT as we learned in class? What assumption(s) of the theorem are being violated?

<font color="blue">

The estimator for $\sigma^2$ is

$$\sigma^2_{MOM}=\frac{1}{n}\sum_{i}(X_i - \mu_{MOM})^2$$

We'd like to use the CLT we learned because this is a sum of random variables, namely $(X_1 - \mu_{MOM})^2$, $(X_2 - \mu_{MOM})^2$, etc.

However, the CLT we learned requires that the variables be *independent*. This is not the case here, because all of these terms share the common $\mu_{MOM}$, so knowing something about $(X_1 - \mu_{MOM})^2$ *can* tell us something about $(X_2 - \mu_{MOM})^2$ [Really? How?].

Luckily, though, there are other versions of the CLT that end up working here. However, they involve way trickier assumptions, and the mathematical machinery required is beyond the scope of our course. For now, just keep in mind that the assumptions your know are sufficient, but not necessary, for some version of the CLT to hold!

 
</font>








