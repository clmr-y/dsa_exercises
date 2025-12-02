## Bruteforce
$ O(n^2) $ - Time
$ O(n) $ - Space
```py
class Solution:
    def isValid(self, s: str) -> bool:
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()', '')
            s = s.replace('{}', '')
            s = s.replace('[]', '')
        return s == ''
```

## Stack
Valid parentheses must follow a last-opened, first-closed order — just like stacking plates.

$ O(n) $ - Time
$ O(n) $ - Space


## Future Improvements
1. You can add a check on top if the size of the string is odd. And if its is, return `false`:$ O(1) $ assuring that anything can be closed at all (you can't close each bracket if the sum of chars is not even).

2. Just changing the last return to: `return stack == []` makes the runtime MUCH BETTER