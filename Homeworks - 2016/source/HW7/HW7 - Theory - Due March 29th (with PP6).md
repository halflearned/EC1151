<font face="times">
# HW7 - Theory - Solutions

### Minimizer of Squared Distances

Let's start this problem working with numbers, not random variables. 

Suppose we're given the following list of *numbers*,
 
$$2,2,2,4,5,5,7,8,10$$

and the initially vague task of saying "something useful" about it. What would you say? Perhaps you'd say something like
 
+ "$7$ is the third largest number"
+ "There are six unique numbers"
+ "The sum of the numbers is 52"
+ "No number is larger than 29"

And so on. Each of these statements contains information about some aspect of the list, but it's hard to say, a priori, which statement is more informative.

So let's make the problem more precise. First, we'll come up with a *criterion* for what are the relevant aspects of the number list we want to summarize, and then find the number that satisfies that criterion. For example, if in our application we were interested in choosing "the most common number", the answer would be "2". (This is called the *mode*, as we'll see later in the course).

It turns out that one of the most common criteria is this: *choose a number $c$ such that the total squared distance between $c$ and all numbers in the list is as small as possible*.

What? I know it sounds weird, but bear with me here. Let's scatter our numbers are scattered on the real line like below, and for example let's see how well the number '$1$' does under the criterion above.

<img src="ruler2.png">

The squared distance between $2$ and $1$ is $(2-1)^2 = 1$, the squared distance between $7$ and $1$ is $(7-1)^2 = 36$, etc. If we sum it all up, we've got

$$TotalDistanceSquared = 1+1+1+9+16+16+36+49+81=210$$

Well, is this good or bad? We don't know yet, because we haven't tried any other number. So here's the first practice problem.

<b>Q1)</b> Compute the sum of squared distances between the numbers in the list and the number $3$ and $6$.

Ok, now we've got the hang of it, let's see how to solve this without trial-and-error. We want to find an *optimal* number, right? Luckily, you did a lot of optimization in Calc 1, so let's make use of that. 

<b>Q2)</b> Given this following "sum of squared distances" function,

$$f(c ) = 3(2 - c)^2 + (4 - c)^2 + 2(5-c)^2 + (7 - c)^2 + (8 - c)^2 + (10 - c)^2$$

use calculus to find the number $c$ that minimizes $f$. (Show your work). 

<b>Q3)</b> Stare at the number you found for a little bit, and answer: how do we normally call that number?

<font color="blue">We usually call that number the **mean**! 

The purpose of this exercise is to provide motivation for using the mean as a summary of data (or, in the case of random variables, a summary of random outcomes). Namely: *the mean is the number that minimizes squared distances between itself and the data*.

In the 21st Century, we totally take for granted the idea of taking the mean of numbers, but in the 1700s this was definitely not the case. In fact, there was actually a debate (!) in the scientific community about what would be the best way to reconcile several measurements into a single number. Just take a look at this letter written by Thomas Simpson in 1755. It's an excerpt of his treatise *On the Advantage of Taking a Mean of a Number of Observations in practical Astronomy*:

<img src="history.png">


<font size=1>Source: Stigler (1990). *The History of Statistics: The Measurement of Uncertainty before 1900*, Belknap Press, p.90.
</font>

Simpson is saying that some "persons of considerable notice" had been suggesting that one single measurement is as good as the mean of several measurements. Pretty crazy, isn't it? 

At the same time other mathematicians, scientists and proto-statisticians were proposing other measures, like the median, the "absolute distances from the mean", the range (maximum number minus minimum number), the interquartile range, the midpoint, the mean absolute difference between all pairs of numbers, and even weirder stuff. 

Luckily, the argument became more or less settled in the early 1800s, when Carl Friedrich Gauss simultaneously did two things: he derived a sensible probability distribution for measurement errors (that would later become known as the Normal distribution!), and came up with the "squared distances" criterion above. He then wrote several treatises explaining that, if measurement errors are roughly distributed in the bell-shaped distribution he posited, then the mean is would provably be best possible summarizer.


For more info, see: H.A. David (1998) *Early Sample Measures of Variability*, Statistical Science, Vol. 13, No. 4 (Nov., 1998), pp. 368-377.

</font>


Now we can start working with random variables again. Suppose we have this quite simple rv.

$$
Y = 
\begin{cases}
3 \qquad \frac{1}{2} \\\
4 \qquad \frac{1}{6} \\\
6 \qquad \frac{1}{6} \\\
7 \qquad \frac{1}{6}
\end{cases}
$$

Here, once again, we'd like to summarize the random variable by a number $c$. Our criterion will be very similar: minimize the sum of squared distances from outcomes $y$ to $c$, but this time *weighted by the probabilities*. 

<b>Q4)</b> The function 

$$f(c ) = \frac{1}{2}(3 - c)^2 + \frac{1}{6}(4 - c)^2 + \frac{1}{6}(6 - c)^2 + \frac{1}{6}(7 - c)^2$$

outputs the value of $c$ given the criterion above. Once again, use calculus to find the value of $c$ that minimizes the function above.

<b>Q5)</b> In general, what is $c$ in terms of $Y$?

<font color="blue">c = E[Y]. That is, *the expectation is the number that minimizes the weighted squared distances between itself and the outcomes of the random variable.*</font>

--

### Limit Theorems Preview
 
<b>Q6)</b> Let's roll a die $n$ times, and denote $X_1$, $X_2$, $\cdots$, $X_n$ the outcome of each roll (so each $X_i$ will turn out to be an integer between 1 and 6).

1) What is $P(X_1 \geq 5)$?

<font color="blue">$P(X_1 \geq 5) = \frac{2}{6}$</font>

2) What is $P(\frac{X_1 + X_2}{2} \geq 5)$?

<font color="blue">$P(X_1 + X_2 \geq 10) = \frac{6}{36}$</font>

3). What is $P(\frac{X_1 + X_2 + X_3}{3} \geq 5)$?

<font color="blue">$P(X_1 + X_2 + X_3 \geq 15) = \frac{20}{216}$

By the way, here's how I figured out the numerator.


```python
counter = 0
for i in range(1,7):           # 1...6
    for j in range(1,7):       # 1...6
        for k in range(1,7):   # 1...6
            if i + j + k >= 15:
                print(i,j,k)
                counter = counter + 1
                
print("Total: ", counter)
```
Yielding

```
3 6 6
4 5 6
4 6 5
4 6 6
5 4 6
5 5 5
5 5 6
5 6 4
5 6 5
5 6 6
6 3 6
6 4 5
6 4 6
6 5 4
6 5 5
6 5 6
6 6 3
6 6 4
6 6 5
6 6 6
Total: 20
```

I guess I didn't say you *should* use Python for this answer. But I didn't say you *shouldn't* use it either. 😈

</font>

4) [Open-Ended] Do you notice any pattern? What do you think will happen to $P(\frac{X_1 + \cdots + X_n}{n} \geq 5)$ as we increase $n$? Give an intuitive explanation for this phenomenon.

<b>Hint</b>  $P(\frac{X_1 + X_2}{2} \geq 5)$ is the same as $P(X_1 + X_2 \geq 10)$

<font color="blue">The probabilities decrease, because the denominator grows *much* faster than the numerator. Here's the result for up to $6$ dice. 

<centeR><img src="growth.png"></center>
We'll get a better idea for why this happens in Module 8, but you're witnessing the **Law of Large Numbers** in action. Here's what it says, roughly.

Take the average of identical random variables, like this.

$$\frac{X_1 + X_2 + \cdots X_n}{n}$$

Now, this is still a *random* object, since each one of the $X_i$'s is a random variable. However, as $n$ increases, the randomness gets ever smaller, until -- at infinity -- there's no more randomness. 

What is even more surprising is that, not only does everything collapses to a constant, but that constant happens to be $E[X_1]$. In other words, as $n$ grows, the probability of getting a random result far from $E[X_1] = 3.5$ gets smaller and smaller and smaller, until that's the only result you ever get.
</font>

