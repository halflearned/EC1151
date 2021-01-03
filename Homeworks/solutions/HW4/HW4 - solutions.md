<font face="times">

Okay, se the expression "50% of the time, there's a 90% chance of a 1" is sounds a bit weird, like "60% of the time I'm right 100% of the time".

To write this in a more mathematically precise way, I'd write:

Let A0, A1 denote the events that Alice sends a zero or a one. We know that P(A0) = P(A1) = 0.5.
Let B0, B1 denote the events that Bob receives a zero or a one. We know that:
+ If Alice sends a zero (i.e., conditioning on A0):
   + Bob receives a zero with probability P(B0|A0) = 0.95
   + Bob receives a one with probability P(B1|A0) = 0.05

+ If Alice sends a one (i.e., conditioning on A1):
   + Bob receives a zero with probability P(B0|A1) = 0.10
   + Bob receives a one with probability P(B1|A1) = 0.90

We're looking for P(A1 | B1).

P()
0.5 * 0.95 / (0.5 * 0.95 + 0.5 * .1)

# HW4 - Solutions

## Q2 - Spam

These three come straight from the problem statement.

$P(\text{spam}) = 0.8$

$P(\text{"extra cash"} | \text{spam}) = 0.08$

$P(\text{"extra cash"} \cap \text{spam}) = P(\text{"extra cash"} | \text{spam})P(\text{spam}) = 0.1 \times 0.8 = 0.08$ 

By the law of total probability

$
\begin{align*}
P(\text{"extra cash"}) 
&= P(\text{"extra cash"} \cap \text{spam} ) + P(\text{"extra cash"} \cap \text{spam}^{c}) \\\
&= P(\text{"extra cash"} | \text{spam} )P(\text{spam}) + P(\text{"extra cash"} \cap \text{spam}^{c})P(\text{spam}^c) \\\
&= 0.1 \times 0.8 + 0.01 \times 0.2 \\\
\end{align*}
$

By Bayes,

$P(\text{spam}\  | \ \text{"extra cash"} \ ) 
=\frac{0.1 \times 0.8}{0.1 \times 0.8 + 0.01 \times 0.2}
$

## Q3 - Coins in a hat [<font color="red">Updated Mar 2</font>]

The answer is $\frac{1}{3}$. Behold!

<img src="coinsinahat2.tiff">

$P(Heads) = \frac{3}{4}$

$P(Heads \cap Fair) = \frac{1}{4}$

Therefore the answer is $P(Fair | Heads) = \frac{\frac{1}{4}}{\frac{3}{4}} = \frac{1}{3}$

## Q4 - Smokers

I'll solve this by simply plugging what we know into Bayes' Theorem.

Problem setup:

$A$: Person develops cancer

$B$: Person smokes

We know 

$P(A|B) = 26\cdot P(A|B^c)$

$P(B) = 0.216$

Plug it into Bayes:

$
\begin{align}
P(B|A) &= \frac{P(A|B)P(B)}{P(A|B)P(B) + P(A|B^c)P(B^c)} \\\ 
      &= \frac{P(A|B) \times 0.216}{P(A|B)\times 0.216 + P(A|B^c)\times 0.784} \\\
      &= \frac{26\times P(A|B^c) \times 0.216}{26\times P(A|B^c)\times 0.216 + P(A|B^c)\times 0.784}
\end{align}
$

Note we can cancel out the $P(A|B^c)$, so the answer is
$
\begin{align}
P(B|A) &= \frac{26 \times 0.216}{26\times 0.216 + 0.784}
\end{align}
$

## Q7 - Forensics

<b>Part 1</b>

Setup:

+ $A$: event that $A$ is guilty
+ $B$: event that $B$ is guilty
+ $M_A$: event that $A$'s blood matches the crime scene blood

We know

+ $P(A) = P(B) = \frac{1}{2}$ before seeing the blood match results

+ $P(M_A | A) = 1$, i.e. if $A$ committed the crime, his blood type will match the crime scene's

+ $P(M_A) = \frac{1}{10}$ the probability of a match, regardless of $A$ having committed the crime or not, is $10\%$.

We want to know $P(A|M_A)$. From Bayes:

$
\begin{align}
P(A|M_A) 
&= \frac{P(M_A | A)P(A)}{P(M_A)} \\\ 
&= \frac{1 \times \frac{1}{2}}{\frac{1}{10}} \\\ 
& = \frac{10}{11}
\end{align}  \\\
$
 <br>
<b>Part 2 (Cancelled)</b>

I haven't found an intuitive way to get to the solution. If you'd like a tentative solution that simply manipulates formulas to get to the answer, let me know.

---

# Programming

## Q8 - Favorite months

```python
months = ["January", "February", "March", "April", "May", "June",
"July", "August", "September", "October", "November", "December"]

for m in months:
    msg = "My favorite month is " + str(m)
    print(m)
```

## Q10 - Factorials


```python
total = 1
for x in range(1, 11):
    total = total * x
    msg = "Factorial: " + str(value)
    print(msg)
```


In both Q9 and Q10 it's important to understand the lines.

```python
total = total + x  # Q9
total = total * x  # Q10
```

The Python interpreter first looks at the right-hand side of these expressions and evaluates them using their current values. It then creates a *new* variable (also) called `total` and stores the results there. 











<bR><br><br><br><br><bR><bR>
<bR><br><br><br><br><bR><bR>