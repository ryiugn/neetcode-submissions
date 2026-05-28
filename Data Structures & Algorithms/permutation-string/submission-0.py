class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count = [0] * 26
        left = 0
        right = left + len(s1) - 1
        while right < len(s2):
            for ch in s1:
                count[ord(ch) - ord('a')] += 1
            for ch in s2[left:right+1]:
                count[ord(ch) - ord('a')] -= 1
            if all(x == 0 for x in count):
                return True
            else:
                left += 1
                right += 1
                count = [0] * 26
        return False