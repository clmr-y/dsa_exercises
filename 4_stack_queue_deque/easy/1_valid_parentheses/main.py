class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            '(':')',
            '{':'}',
            '[':']'
        }
        
        # O(n)
        for bracket in s:
            if bracket in pairs:
                stack.append(bracket)

            else:
                if stack:
                    opening_bracket = stack.pop(-1)
                
                    if bracket != pairs[opening_bracket]:
                        return False
                        
                else:
                    return False

        return len(stack) == 0