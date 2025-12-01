# Recursion

The **recursive definition** can be formalized as

$$ n! = 
    \begin{cases}
        1 & \text{ if } n = 0\\
        n \cdot (n-1)! & \text{ if } n \geq 1 
    \end{cases}  
$$

Recursive definition must contain
1. One or more **base cases**
2. One or more **recursive cases**

## Ruler problem
### Analysis
First lets consider how to draw the 'tics'.

A single cm is composed of three types of ticks of $L\geq1$ length:
* An **interval** with a central tick of length $L-1$
* A single tick of length $L$
* An interval with a central tick length $L-1$

```py
def draw_line(tick_length, tick_label=''):
    line='-'*tick_length
    if tick_label:
        # add label if needed
        line += ' ' + tick_label
    print(line)

def draw_interval(central_length):
    if central_length > 0:
        # draw the left interval
        draw_interval(central_length - 1) 
        # draw the middle tick
        draw_line(central_length)
        # draw the right interval
        draw_interval(central_length - 1)

def draw_ruler(num_inches, major_length):
    draw_line(major_length, 'O')
    for j in range(1, 1 + num_inches):
        draw_interval(major_length - 1)
        draw_line(major_length, str(j))

```
```py
>>> draw_ruler(1,1)
- O
- 1
```

```py
>>> draw_ruler(1,2)
-- O
- #  interval_length - 1
-- 1
```

```py
>>> draw_ruler(1,3)
--- O
-
-- #  interval_length - 1
-
--- 1
```

```py
>>> draw_ruler(1,4)
---- O
-
--
-
--- #  interval_length - 1
-
--
-
---- 1
```

```py
>>> draw_ruler(1,5)
----- O
-
--
-
--- #  interval_length - 1
-
--
-
----
-
--
-
---
-
--
-
----- 1
```

## Analyzing Recursive Algorithms


### Drawing an English Ruler

We know that a call to `draw_interval(c)` for $ c>0 $ spawns two calls to `draw_interval(c-1)` and a single call to `draw_line`.

#### Proposition
For $ c \geq 0 $ a call to `draw_interval(c)` results in $ 2^c - 1 $ lines of output.

#### Justification
Proof by induction. 

Let's compute a few to see a pattern:
* $ T(0) = 0 $
* $ T(1) = 2 T(0) + 1 = 1$
* $ T(3) = 2 T(2) + 1 = 7$
* $ T(4) = 2 T(3) + 1 = 15$

We notice a pattern: $ T(c) = 2^c - 1$
1) `draw_interval(0)`: $ 2^0 - 1 = 0$ - Base claim
2) For $ c > 0 $:
* `draw_interval(c-1)` $ \to T(c-1)$ lines
* `draw_interval(c)` $ \to 1$ line
* `draw_interval(c-1)` $ \to T(c-1)$ lines
The number of lines is $$ T(c) = T(c -1) + 1 + T(c-1) = $$ $$ = 1 + 2 \cdot (2^{c-1} - 1 ) = 1 + 2^c - 2 = 2^c - 1 $$


### Performing a Binary Search

[Finish this]