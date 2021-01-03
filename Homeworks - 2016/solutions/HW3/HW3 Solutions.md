# HW3 Solutions


### Q1 - Fundamentals

This is fundamentally an exercise in understanding notation. To make sure we understand what the symbols mean, let's use one of our running toy examples and translate it all into English. 

Imagine that we pick one employee at random from company with 100 employeees. Let:

+ $A$ be the event that the person is a man
+ $A^c$ be the event that the person is a woman
+ $B$ be the event that the person is an executive

Now, the exercise setup says that $P(A) = \frac{1}{2}$. For now, it's useful to interpret this as the fraction of men in the whole population: $\frac{1}{2} = 50\%$. So there's a 50-50 chance that a randomly chosen employee turns out to be a man.

Similarly, $P(B) = \frac{1}{3}$ implies that third of the employees are executives. For this example let's just round this to 33 people.

Finally, we also know that $P(A \cap B) = \frac{1}{5}$. In English, this means that a fifth of the whole pool of employees is both a man AND an executive. So 20 people belong to this category.

This setup is quite unimpressively illustrated on this Venn diagram [not to scale].

<img src="B.png" height = 200>

where the left rectangle is the set of men, the the blue evoid are the executives.

The first part of this question asks: what is $P(A|B)$?

Here's how to read the symbols: take an employee at random, but instead of picking from the whole pool of employees, pick them only from the pool of executives $B$. What are the chances that you've picked a guy?

Well, there are 33 executives and 20 male executives, so the probability is $\frac{20}{33} \approx 0.6$. If we think about the conditional probability formula,

$$P(A|B) = \frac{P(A \cap B)}{P(B)} = \frac{\frac{1}{5}}{\frac{1}{3}} = \frac{3}{5} = 0.6 = 60\%$$


that's precisely what we get. On the Venn diagram, we're saying that the dark blue part represents 60% *of the blue ovoid*.

<img src="AandB.png" width = 300>

Part b of this question asks something every similar: what is $P(A^c | B)$?

Again, translating into English, that's the same as asking: if we pick an employee at random *from the pool of executives*, what are the chances the person is not a man?

Well, there are 33 executives, and 20 are men. So 13 are not men. Therefore the probability is $\frac{20}{33} \approx 0.4$.

Note we had one small extra step before using the conditional probability formula. We used the fact that

$$\underbrace{P(B)}_{Execs} = \underbrace{P(A \cap B)}_{Male Execs} + \underbrace{P(A^c \cap B)}_{FemaleExecs}$$

or

$$\frac{1}{3} = \frac{1}{5} - P(A^c \cap B)$$

or, solving for the unknown,

$$P(A^c \cap B) = \frac{1}{3} - \frac{1}{5} = \frac{2}{15} \approx 13\%$$

Again, we're just saying that 13 employees *out of the whole pool of employees* are simultaneously "not men" AND "executives".

But the question asked for the "not men" fraction of the *executive subpopulation*, so to figure that out we compute

$$P(A^c|B) = \frac{P(A^c \cap B)}{P(B)} = \frac{\frac{2}{15}}{\frac{1}{3}} = 0.4$$ 

So we reached the same answer via math and via English: the beet-colored section below represents $40\%$ of the blue ovoid (or alternatively: of the executives, $40\%$ are not men; or yet: $A^c \cap B$ comprises $40\%$ of the set $B$.


---

## Q2 - Dice 

Keep in mind the following. Given a sample space $S$ (here, the collection of 36 elementary outcomes of a double dice roll), the symbols should be understook like this.

+ $P(A)$ is "what fraction of the elements of $S$ satisfy $A$?"
+ $P(B)$ is "what fraction of the elements of $S$ satisfy $B$?"
+ $P(A|B)$ is "what fraction of the elements of $B$ also satisfy $A$?"
+ $P(B|A)$ is what fraction of the elements of $A$ also satisfy $B$?"

Moreover, to figure out independence, check whether or not $P(A|B) = P(A)$ or equivalently whether or not $P(A \cap B) = P(A)P(B)$.


a) $A$ white die is <font size=5>&#9856;</font>, $B$: sum is $5$

+ $P(A) = \frac{1}{6}$ 

Since $A$ = {(1,1), (1,2), ...., (1,6)}, six out of 36 elements satisfy $A$.

+ $P(B) = \frac{1}{9}$ 

Since $B$ = {(1,4), (4,1), (2,3), (3,2)}, so four out of 36.

+ $P(A|B) = \frac{1}{4}$ 

Since the white die is 1 in only one *out of the four elements in $B$*

+ $P(B|A) = \frac{1}{6}$

Since only one combination -- (1,4) -- satifies $B$ out of the 6 elements of $A$.

+ Independence? No, since $\frac{1}{6} = P(A) \neq P(A|B) = \frac{1}{4}$.


b) $A$ white die is <font size=5>&#9858;</font>, $B$: black is <font size=5>&#9858;</font>

+ $P(A) = \frac{1}{6}$
+ $P(B) = \frac{1}{6}$
+ $P(A|B) = \frac{1}{6}$ (why?)
+ $P(B|A) = \frac{1}{6}$
+ Independent? YES, since $P(A) = P(A|B) = \frac{1}{6}$.


c) $A$ sum is $7$, $B$: white die is <font size=5>&#9858;</font>

+ $P(A) = \frac{1}{6}$
+ $P(B) = \frac{1}{6}$
+ $P(A|B) = \frac{1}{6}$ 
+ $P(B|A) = \frac{1}{6}$ One outcome -- (3,4) -- out of six outcomes in  $A$
+ Independent? YES, since $P(A) = P(A|B) = \frac{1}{6}$.

d) $A$: of the two rolls, the smallest one is <font size=5>&#9857;</font>, $B:$ black die is <font size=5>&#9860;</font>

Note $A$ = {(2,2), (2,3), (2,4), (2,5), (2,6), (3,2), (4,2), (5,2), (6,2)

+ $P(A) = \frac{1}{9}$
+ $P(B) = \frac{1}{6}$
+ $P(A|B) = \frac{1}{6}$ Only (2,6) out of the six outcomes in $B$
+ $P(B|A) = \frac{1}{9}$ Only (2,6) out of the nine outcomes in $A$
+ Independent: Yep.

e) $A$: of the two rolls, the smallest one is <i>at least</i> <font size=5>&#9857;</font>, $B:$ black die is <font size=5>&#9860;</font>
 
Note $A$ is any outcome that doesn't have a &#9856; in it (right?) and there are 25 of those.

+ $P(A) = \frac{25}{36}$
+ $P(B) = \frac{1}{6}$
+ $P(A|B) = \frac{1}{5}$ Since there are five elements in $B$ -- ie., (2,6), (3,6), (4,6), (5,6), (6,6) -- that also satisfy $A$.
+ $P(B|A) = \frac{5}{6}$ Everyone except (1,6) 
+ Independent? NO, since $P(A|B) \neq P(A)$.
 
 
---

# Q4 IQ vs Grades

In this exercise, try to make your reasoning explicit in the notation. 

Parts a and b come from the law of total probability, and / or from the complement rule.

$P(A) = P(A \cap High) + P(A \cap Low) = 0.47 + 0.01 = 0.48$

$P(High) = P(A \cap High) + P(B \cap High) $
$\qquad \qquad  + P(C \cap High) + P(D \cap High) = 0.78$

$P(Low) = 1 - P(High) = 1 - 0.78  = 0.22$


Part c is really jut table lookup.

$P(High \cap B) = 0.23$.

Part d uses the CP formula and the law of total probability of the event $High$

$P(High | B) = \frac{0.23}{0.23 + 0.03}$

Part e uses the CP formula and the law of total probability of the event $B$

$P(B | High) = \frac{0.23}{0.78}$

----

## Q5 - Coins in a hat

Some cunning use of the law of total probability here, followed by the "chain rule".

$$P(Heads) = P(Heads \cap Fair) + P(Heads \cap Double)$$

$$P(Heads) = P(Heads | Fair)P(Fair) + P(Heads | Double)P(Double)$$

Therefore

$$P(Heads) = \frac{1}{2}\frac{10}{20} + 1\cdot \frac{10}{20}$$

----

## Q7 - Coat check problem


Here's a crucial insight: *in this problem, the order in which the guests take their coats does not matter*. Let's see why.

My first guest, Ms. One, picks one coat out of $n$, so there's a $P(X_1) = \frac{1}{n}$ probability that she gets her coat. 

My second guest, Mr. Two, picks another coat. But the probability of that coat being the correct one is *still* $\frac{1}{n}$, since we don't know yet if Ms. One picked out her coat correctly. Hence $P(X_2) = \frac{1}{n}$.

The same argument proceeds until we reach the $n$th guest, who also doesn't know if anyone else picked out their coat correctly or not, so he still faces a $P(X_n) = \frac{1}{n}$ of picking their own coat.

Okay, but what if we knew Ms. One chose her own coat? Then Mr. Two can only choose one out of $n-1$ possible coats, and therefore $P(X_2 | X_1) = \frac{1}{n-1}$ (pay close attention to the notation here).

Note also that we didn't have to use Ms. One and Mr. Two above. If we knew that Mr. Seven had picked out his coat correctly, then the probability of Ms. Four picking her own coat is also $P(X_3 | X_7) = \frac{1}{n-1}$.

<b>Alternative solution</b>

Ok, but you still don't believe me. Fine, here's a purely combinatorial solution. Instead of having the guests like up sequentially, have them stand side-by-side, and randomly throw coats at them.

<centeR>
&#128104;&#128112;&#128113;&#128103;&#128114;&#128115;&#128116;
&#128084;&#128085;&#128086;&#128087;&#128088;&#128090;&#128089;
&#128085;&#128086;&#128087;&#128088;&#128090;&#128089;&#128084;
&#128085;&#128090;&#128084;&#128089;&#128086;&#128087;&#128088;
&#128089;&#128084;&#128085;&#128086;&#128087;&#128088;&#128090;
$\cdots$
</center>

<font size=1>
[Not really coats but you get the idea]
</font>

The sample space is the set of permutations of the $n$ coats. There are $n!$ such permutations.

What's the probability that Mr. One gets his coat? Consider all permutations that give him his coat.

<centeR>
(&#128104;) &#128112;&#128113;&#128103;&#128114;&#128115;&#128116;
(&#128084;) &#128085;&#128086;&#128087;&#128088;&#128090;&#128089;
(&#128084;)&#128085;&#128086;&#128087;&#128088;&#128090;&#128089;
(&#128084;)&#128085;&#128090;&#128089;&#128086;&#128087;&#128088;
(&#128084;)&#128089;&#128085;&#128086;&#128087;&#128088;&#128090;
$\cdots$
</center>

There are $n!$ ways of permuting everything else, so that's the size of our favorable event.

Put all of this information together and boom $P(X_1) = \frac{(n-1)!}{n!} = \frac{1}{n}$.

How about the conditional probability? I'll let you continue the argument above and figure it out by yourself.

---

# Q8 - Cards

<font size=1>
The solutions to Q8 and Q6 are basically the same, with cards instead of balls.
</font>

<b>Conditional probability solution</b>

Remember I said that within every hard problem there's a smaller problem you can solve? It turns out that conditional probability is an excellent tool to decompose hard problems into smaller ones. Let's see.

To draw four cards, we must first draw one card, and then a second card, and so on. So then:

1) Suppose you have no cards yet. What's the probability that the first card you pick will be (e.g.) blue?

Let's call this event $B_1$ ("blue-one"). A little thought should reveal that $$P(B_1) = \frac{10}{40}$$

2) Now suppose you've drawn a blue card. What's the probability that the *second* card you pick will be of a different color, like (e.g.) pink?

Let's call the event of drawin a pink ball in the second draw $P_2$. Since there are 39 balls in the bag and 10 of them are pink, $$P(P_2 | B_1) = \frac{10}{39}$$ (see how the sample space has been reduced by conditioning?)

3) You drew a blue card AND then you drew a pink one. What's the probability that the next one is of a new color again, like (e.g.) red?

I'll let you convince yourself that this should be
 $$P(R_3 | B_1 \cap P_2) = \frac{10}{38}$$ 
 
(once again: the state space has been reduced further, so the denominator is even smaller).

4) You drew a blue card AND you drew a pink card AND you drew a red card. What's the probability that the last one is green?

$$P(G_4 | B_1 \cap P_2 \cap R_3) = \frac{10}{37}$$.

We just learned that the probability of drawing the exact sequence blue-pink-red-green is 

$P(B_1 \cap P_2 \cap R_3 \cap G_4) = P(B_1) \cdot P(P_2 | B_1) \cdot P(R_3 | B_1 \cap P_2) \cdot P(G_4 | B_1 \cap P_2 \cap R_3)$
$\qquad \qquad \qquad \qquad \ = \frac{10}{40}\cdot \frac{10}{39}\cdot \frac{10}{38}\cdot \frac{10}{37}$

We are not quite done yet, because we now we have to think about the probability of drawing four different colors in whichever order: blue-pink-red-green OR pink-red-green-blue OR red-blue-green-pink OR... and since there are $4!$ different color permutations, our final answer is:

$$P(\{Four Colors \} ) = 4! \frac{10}{40}\cdot \frac{10}{39}\cdot \frac{10}{38}\cdot \frac{10}{37} \approx 0.1094$$


<b>Purely combinatorial solution</b>

While the previous solution style will turn out to be more useful in this class, it might be interesting to know that you could have although thought like this.

+ There are $\binom{40}{4}$ ways of picking 4 cards from the deck of 40 cards.
+ There are $\binom{10}{1}$ ways of picking one red card from the 10 red cards. Similarly for all other colors.
+ By the multiplication rule, there are $\binom{10}{1}\binom{10}{1}\binom{10}{1}\binom{10}{1}$ of choosing one card from each color.

Put it together and you'll find out that:

$$P(\{Four Colors \} ) = \frac{\binom{10}{1}\binom{10}{1}\binom{10}{1}\binom{10}{1}}{\binom{40}{4}}$$
$$\qquad \qquad  \qquad= \frac{\frac{10!}{1!9!}\frac{10!}{1!9!}\frac{10!}{1!9!}\frac{10!}{1!9!}}{\frac{40!}{36!4!}}$$
$$\qquad \qquad \qquad = \frac{10\cdot 10 \cdot 10 \cdot 10}{\frac{40 \cdot 39 \cdot 38 \cdot 37}{4!}}$$
$$\qquad \qquad  \qquad= 4!\frac{10\cdot 10 \cdot 10 \cdot 10}{40 \cdot 39 \cdot 38 \cdot 37}$$
$$\qquad \approx 0.1094$$

Pretty.

<b> simpler solution</b>

The both solutions are great except... they're kinda fancy, right? You'd like an explanation that my great-grandma can understand. Very well.

First, there are four slots, and 40 balls to choose from. So there are $40 \cdot 39 \cdot 38 \cdot 37$ ways of filling those slots.

When I'm filling the first slot, I can choose any ball so there are 40 possible options. Say I pick red. I can't pick red again, so for the next slot there are 30 options. Say I pick blue. For the next slot there are 20 options. And then there are 10 options for the last slot.

$$\frac{40 \cdot 30 \cdot 20 \cdot 10}{40 \cdot 39 \cdot 38 \cdot 37} \approx 0.1094$$.

<center>
\* mic drop \*

👋
.
.
.
.
🎤
</center>

_____


# Programming Practice

### Q9 - Extracting items

```
xs = ["word", 1, [3.14, 2017]]
s = xs[0]
i = xs[1]
tmp = xs[2]
x = tmp[1]
```
Or putting the last two lines together

```
xs = ["word", 1, [3.14, 2017]]
s = xs[0]
i = xs[1]
x = xs[2][1]
```

### Q10 - Printing Odds

```python
for n in range(7, 22, 2):
    print(n)
```

### Q11 - Printing "L"

My solution

```python
for i in range(6):
    print("*")
print("*" * 5)
```

Your solution

```python
xs = ["*", "*","*","*","*","*","*****"]
for item in xs:
    print(item)
```

My take on your solution

```python
xs = ["*"] * 6 + ["*" * 5]
for item in xs:
    print(item)
```

### Q12 - Slicing lists

```python
xs = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
xs1 = xs[2:6]
xs2 = xs[:4]
xs3 = xs[4:]
```


