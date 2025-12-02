class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = []

        index = {}
        
        # O (n)
        for word in strs:
            # O(k log n)
            s_word = ''.join(sorted(word))
            # O(1)
            index[s_word] = index.setdefault(s_word, []) + [word]

        return list(index.values())
    


from collections import Counter
class Solution2:
    def letter_counter(self, s) -> Dict[tuple[str, int]]:
        out = {}

        for letter in s:
            out[letter] = out.setdefault(letter, 0) + 1


        return out

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = []

        index = {}
        
        for word in strs:
            counter = self.letter_counter(word)
            letter_counter_tuple = frozenset((k, v) for k, v in counter.items())
            idx = (len(word), letter_counter_tuple)
            print(letter_counter_tuple)

            if idx in index:
                index[idx] += [word]
            else:
                index[idx] = [word]
            
        return list(index.values())