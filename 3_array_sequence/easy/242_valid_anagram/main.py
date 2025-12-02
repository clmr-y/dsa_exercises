class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        index_s = {}
        index_t = {}

        for i in s:
            index_s[i] = index_s.get(i, 0) + 1
        for i in t:
            index_t[i] = index_t.get(i, 0) + 1

        return index_s == index_t