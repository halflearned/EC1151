<font face="times">
# HW6 - Theory - Due March 13th (with PP5)



<b>Q1)</b> Just a preliminary exercise to warm up. Let $X$ have the following PMF.

$$
X = 
\begin{cases}
-2 \qquad \text{ with probability } \qquad .10    \\\
-1 \qquad \text{ with probability } \qquad .15    \\\
0 \qquad \text{ with probability } \qquad  .50  \\\
1 \qquad \text{ with probability } \qquad .15   \\\
2 \qquad \text{ with probability } \qquad .10    \\\
\end{cases}
$$

1) Draw the PMF and CDF associated with this random variable.
2) Compute $E[X]$.
3) Let Y = X^2 . Draw the PMF and CDF associated with this random variable.
4) Compute $E[Y]$.

---

<b>Q2)</b> Recall that when we say $X \sim Bernoulli(p)$ we mean the following.

$$
X = 
\begin{cases}
0 \qquad \text{ with probability } \qquad 1-p    \\\
1 \qquad \text{with probability } \qquad  p     \\\
\end{cases}
$$

Compute the $E[X]$.

---

<b>Q3)</b> Now suppose that we have two $Bernoulli(p)$ random variables, $X_1$ and $X_2$, both with the same PMF and in the previous question. *Using linearity*, compute the expectation of 
$$Y = X_1 + X_2$$ 


---

<b>Q4)</b> I'd like to ask you to compute the expectation of a general $Binomial(n,p)$ random variable. However, remember that the PMF with arbitrary $n$ and $p$ is kind of a mess:

$$Y\sim Binomial(n,p) \qquad \text{has PMF} \qquad p_Y(k) = {n \choose k} p^{k}(1-p)^{n-k}$$

So to find the expectation we'd have to compute

$$E[X] = 0\cdot {n \choose 0} p^{0}(1-p)^{n} + 
        1\cdot {n \choose 1} p^{1}(1-p)^{n-1} + \cdots +
        n\cdot{n \choose n} p^{n}(1-p)^{n-n}$$

How can you possibly simplify that?! It turns that it's possible to grind through the algebra, as this <a href="https://www.khanacademy.org/math/statistics-probability/random-variables-stats-library/binomial-random-variables/v/expected-value-of-binomial-distribution">Khan Academy video</a> explains. But let's not do that. Instead:

1) Use what you know about Binomial random variables, linearity, and your answers to Q2 and Q3 to show, without doing any algebra, that if $Y \sim Binomial(n,p)$ then

$$E[Y] = np$$

2) [Open-ended] Explain in plain English why this formula makes sense.

---

<b>Q5)</b> This problem is related to the <a href="https://en.wikipedia.org/wiki/Expected_utility_hypothesis">Expected Utility Hypothesis</a> that you might have heard of in your micro theory class (if you haven't, you can still solve this problem).

A person is considering whether or not to buy insurance against burglary for their house. 

+ The house has 1000 dollars worth of stuff in it. If the house is not burgled, all the value remains intact.
+ If the house is broken in, a burglar can steal most of the valuables and leaves only 10 dollars in the house.
+ It's a risky neighborhood: the probability of a burglary is 0.1.
+ If the person pays $r$ dollars for insurance, then regardless of whether the house in burgled or not they end up with $1000 - r$ dollars (i.e., the original value of the house minus the insurance price). 

We'd like to know up to how much would the person would be willing to pay for insurance. 

1) We begin by modelling the value of the house without insurance like this:

$$
X_{Uninsured} = 
\begin{cases}
10 \qquad \text{ with probability } \qquad  0.1    \\\
1000 \qquad \text{with probability } \qquad  0.9     \\\
\end{cases}
$$

What's the expected value of the house without insurance?

2) Next, we can think about the value of the house with insurance.

$$
X_{Insured} = 
\begin{cases}
1000 - r \qquad \text{with probability } 1
\end{cases}
$$

In terms of $r$, what's $E[X_{Insured}]$? (Okay, that's an easy one)

3) What is the maximum value of $r$ such that $E[X_{Insured}] \geq E[X_{Uninsured}]$?

4) Presumably the $r$ you found above would be the maximum price anyone would be willing to pay for insurance, right? As a matter of fact, that's not what happens: in reality people are much more willing to pay for extra safety. This is called *risk aversion*, and it's a source of profit for insurance companies.

Economic theory explains this phenomenon like this. People's *utility* for value (i.e. how happy they are with the value they own) usually doesn't increase linearly with value. That is, a person with 1000 dollars is not 100 times happier than a person who has 10 dollars. Moreover, a person whose wealth increases from 10 to 11 dollars gets marginally happier than a person whose wealth increases from 1000 to 1001 dollars. 

For the purposes of this exercise, let's assume that a person's utility for value increases logarithmically, like this:

$$u(x) = \ln(x)$$

(You can draw a log curve and see that it conforms to the properties I described above.)

Now, here's what I want to get at: if the value a person owns is subject to random chance, like in the setup above, then their utility will also be random! Let's create two new random variables that will describe how happy or sad the person is, in each scenario.

$$Y_{Uninsured} = u(X_{Uninsured})$$
$$Y_{Insured} = u(X_{Insured})$$

What are the PMFs of these random variables? What are $E[Y_{Uninsured}]$ and $E[Y_{Insured}]$? 


5) What is the maximum value of $r$ such that $E[Y_{Insured}] \geq E[Y_{Uninsured}]$? (You might need a calculator)


---

<b>Q6)</b> This exercise will get you thinking about empirical probabilities, and it will also prep you for the topic of *conditional expectation* that we'll see in a few weeks. 

Here is a list of some of my friends, along with information about their heights and whether I met them in BC or not (BC friends are marked with a 1).

|  Name | BC  |  Height (cm) |
|---|---|---|---|---|
| Enkhmanlai Amarsaikhan  | 1  | 180  |
| Solvejg Wewel | 1  | 180  |
| Ratib Ali | 1 | 170  |
| Pierre De Leo | 1 | 190  |
| Michael Connolly | 1 | 170  |
| Dominique Brabant | 1 | 170  |
| Giselle Knowles-Carter  | 0  | 170  |
| Stefani Joanne Angelina Germanotta  | 0  | 155  |
| Hercules John  | 0  | 170  |
| Brian Hugh Warner  | 0  | 185  |
| Onika Tanya Maraj | 0  | 180  |
|  Christopher Depp II | 0  | 180  |
| Farrokh Bulsara | 0 | 170 |


Suppose I'd like to know what's the average height among all of my friends. There are two ways I could do that:

1. Take the average height of my BC friends; then take the average height of my non-BC friends; then average the two averages, remembering to give higher weights to my non-BC friends' average, since they are more numerous.
2. Don't divide my friends in groups at all, and just take the average of the seven numbers in the height column above.

Do both of these procedures give the same answer? Try it out, and if you can include an explanation (or a mathematical proof) for why or why not.

---

<b>Q7)</b> [Job interview question] Vitor’s phone has 1300 different songs in it, consisting of 100 albums of 13 songs each. While running on a treadmill at the Plex, he listens to 5 random songs (any more and he would collapse). Each song is equally likely and chosen independently, so repetitions may occur.

1) Let $X_1$ be a random variables that takes value 1 if the first song Vitor listens to comes from his currently favorite album (<a href="http://www.piazza.com/class_profile/get_resource/ixrnw1uhjtdyi/izngpicgppi364">*Shiny Eyed Babies*</a>, by Bent Knee), and 0 otherwise. What is the distribution of $X_1$? Give its name and its parameter(s).

2) What is the probability distribution of the number of songs that come from that particular album among the five songs Vitor listens to? Give its name and its parameter(s).

<b>Hint</b> Similarly to the first part, let $X_2$ through $X_5$ take value 1 if song number 2 through 5 come from that particular album, and take value 0 otherwise. Remember that $X_1, \cdots, X_5$ are all independent. 

3) What is the probability that at least two songs will belong to the same album (that's *any* album, not particularly Shiny Eyed Babies)?

<b>Hint</b> Think about the complement of this event.

4) [Variants of this question frequently come up in job interviews. Think hard about this one!] 

Call a pair of songs a *match* if they come from the same album. For example, if the 3rd and 5th songs come from the same album, that's one match. On average, how many matches will there be in five songs?

<b>Hint</b> Here's the trick to solve this sort of question. Let $X_{12}$ take value 1 if songs 1 and 2 match, zero otherwise. Similarly, let $X_{13}$, $X_{14}$, $\cdots$, $X_{45}$ take value $1$ if their subscripts are a match, and 0 otherwise. How many of these $X_{ij}$ random variables are there? What's the probability that each one takes value 1? Are they independent? How can you use them to solve the question?


