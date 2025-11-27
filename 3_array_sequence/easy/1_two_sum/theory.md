## Approach 1: Brute Force

Time complexity: $ O(n^2) $
Space complexity: $ O(1) $

## Approach 2: Two-pass Hash Table

We reduce lookup from $ O(n) $ to $ O(1) $ by *trading* **space** for **speed**.  

The first iteration/pass fills the hash table.
Second - checks if `target - value` exists in the hash table.

Time complexity: $ O(n) $
Space complexity: $ O(n) $

## Approach 3: One-pass Hash Table
Combines the approach #2 seperate iterations.