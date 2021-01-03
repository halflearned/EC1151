# HW2 - Solutions

## Q3

There are several ways of getting to the final solution in this exercise. The important thing is to try to use the properties of sets and of the probability function we learned in class.

<font face="times"><b>a)</b>No die rolls a <font size=5>&#9861;</font>

If we define:

$A$: {(&#9856;, &#9861;), (&#9857;, &#9861;), (&#9858;, &#9861;), (&#9859;, &#9861;), (&#9860;, &#9861;), (&#9861;, &#9861;),
 (&#9861;, &#9860;), (&#9861;, &#9859;), (&#9861;, &#9858;), (&#9861;, &#9857;), (&#9861;, &#9856;)}
 
 Then we're interested in:
 
 $P(A^C) = 1 - P(A) = 1 - \frac{11}{36} = \frac{25}{36}$
 
 <br><br>
 
 <b>d)</b> At least one die is a <font size=5>&#9860;</font> but no die is <font size=5>&#9858;</font>.
  
Take these two events:
  
$A$: At least one die is ⚄ 
$B$: One die is ⚂

We want the first event, and the opposite of the second event. This can be represented by $A \backslash B$ or $A \cap B^c$ (draw a Venn diagram and convince yourself that this is true).

Let's go ahead and list everyone one these sets:

There are 11 elements in $A$:

A = {(&#9856;, &#9860;), (&#9857;, &#9860;), (&#9858;, &#9860;), (&#9859;, &#9860;), (&#9860;, &#9856;), (&#9860;, &#9857;), (&#9860;, &#9858;), (&#9860;, &#9859;), (&#9860;, &#9860;), (&#9860;, &#9861;), (&#9861;, &#9860;)}

There are 25 elements in $B^c$:

B^c = {(&#9856;, &#9856;), (&#9856;, &#9857;), (&#9856;, &#9859;), (&#9856;, &#9860;), (&#9856;, &#9861;), (&#9857;, &#9856;), (&#9857;, &#9857;), (&#9857;, &#9859;), (&#9857;, &#9860;), (&#9857;, &#9861;), (&#9859;, &#9856;), (&#9859;, &#9857;), (&#9859;, &#9859;), (&#9859;, &#9860;), (&#9859;, &#9861;), (&#9860;, &#9856;), (&#9860;, &#9857;), (&#9860;, &#9859;), (&#9860;, &#9860;), (&#9860;, &#9861;), (&#9861;, &#9856;), (&#9861;, &#9857;), (&#9861;, &#9859;), (&#9861;, &#9860;), (&#9861;, &#9861;)}

Their intersection consists of these 9 elements:

$A \cap B^c$ = {(&#9856;, &#9860;), (&#9857;, &#9860;), (&#9859;, &#9860;), (&#9860;, &#9856;), (&#9860;, &#9857;), (&#9860;, &#9859;), (&#9860;, &#9860;), (&#9860;, &#9861;), (&#9861;, &#9860;)}
 
Therefore the answer is $P(A \backslash B)= \frac{9}{36} = \frac{1}{4}$.

 
---

## Q4: Bonferroni Inequality

Following the hints, we start with this (now uncontroversial) statement:

$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

All the elements on the right-hand side are in the formula that we want to prove, but the left-hand side is different.

When we're stuck, we take a step back and evaluate what we know about probabilities. Let's see. They must be nonnegative...

$$P(C ) \geq 0 \qquad \text{For any event }C$$

Can that help us? Hmm...	&#x1f914;

$$P(A \cup B) \geq 0$$ 

$$P(A) + P(B) - P(A \cap B) \geq 0$$

....yeah, that doesn't look like what we need. What else do we know about probabilities? Well, they had better be smaller than one.

$$P(C ) \leq 1 \qquad \text{For any event }C$$

Can *that* help us?...

$$P(A \cup B) \leq 1$$ 

$$P(A) + P(B) - P(A \cap B) \leq 1$$

Aha, there we go. Rearranging the second statement:

$$P(A \cap B) \geq P(A) + P(B) - 1$$

Done.

This is pretty much what you have to do when trying to prove this properties. When it helps, you can also try first drawing a Venn diagram and figuring out what the formula *means*, and then proceeding to prove why it must be true (or false, sometimes!).

---

## Q6 *TypeError*

The fourth line was the problematic one. The result of the `input` function is a string, so whenever we want to perform calculations with it we must change it to an `int` or a `float`, and when we want to print it out, we must convert it back to a string.

This is the fastest solution. Can you figure out the order of operations in the fourth line? 

```python
n = input("Please tell me your favorite number.")
msg1 = "Got it. Your favorite number is " + n
print(msg1)
msg2 = "The square of your favorite number is " + str(float(n)**2)
print(msg2)
```
First the `float` function is evaluated and makes `n` and float, then the power `**` function squares the float, which is then converted into string by `str`, and finally concatenated to the rest of the text by `+`.

A more verbose solution could have been something like this

```python
n_text = input("Please tell me your favorite number.")
msg1 = "Got it. Your favorite number is " + n_text
print(msg1)
n_float = float(n_text)  
n_squared = n_float ** 2
n_squared_text = str(n_squared)
msg2 = "The square of your favorite number is " + n_squared_text
print(msg2)
```
where I put the suffix `_text` to indicate to the reader that this variable is a string. But I did this out of convenience to you. Experienced programmers usually don't need this level of detail. You'll get the hang of it, don't worry!

---


## Q8-9 *Clock time*

Note the `int` function wrapping `input`, making sure that the variable `current_time` is a number.

```python
current_time = int(input("Tell me the current hours (0-23): "))
alarm_hours = int(input("In How many hours will the alarm go off?"))
total_time = current_time + alarm_hours
clock_time = total_time % 24
print("The time will be " + str(clock_time))
```





