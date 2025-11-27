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

# todo: this is brain numbing
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

