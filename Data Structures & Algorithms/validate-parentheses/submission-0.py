class Solution:
    def isValid(self, s: str) -> bool:
        check = {')': '(', '}': '{', ']': '['}
        if len(s)%2 != 0:
            return False                    
        result = []
        for ch in s:
            if ch in ('(', '{', '['):
                result.append(ch)
            else:
                if not result or check[ch] != result[-1]:
                    return False
                result.pop()
        if result == []:
            return True
        return False