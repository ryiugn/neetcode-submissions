class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1count = [0] * 26
        windowcount = [0] * 26
        for ch in s1:
            s1count[ord(ch) - ord('a')] += 1
        for ch in s2[:len(s1)]:
            windowcount[ord(ch) - ord('a')] += 1
        if s1count == windowcount:
            return True
        for right in range(len(s1), len(s2)):
            windowcount[ord(s2[right]) - ord('a')] += 1
            windowcount[ord(s2[right - len(s1)]) - ord('a')] -= 1
            if s1count == windowcount:
                return True
        return False