## Sorting and Hashing
$ O(m * n \log n) $ - Time

## Two Hashing
$ O( m * n) $ - Time

## Why `Solution2` is Slower Despite Better Asymptotic Analysis

Examples of expensive operations performed:
* `dict.setdefault` per char
* creating `frozenset`
* creating pairs `(k, v)`
* hashing many times
* converting to tuple

Ideally you should use C-optimized operations, for example calling a `Counter` and sorting are C-optimized.

## Future Improvements
Better key:
```py
key = [0] * 26
for c in word:
    key[ord(c) - 97] += 1
index[tuple(key)].append(word)
```