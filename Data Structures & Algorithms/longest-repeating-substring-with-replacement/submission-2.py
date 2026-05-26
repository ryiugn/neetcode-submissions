class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = {}
        maxcount = 0
        result = 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            maxcount = max(maxcount, count[s[right]])
            if right-left+1 - maxcount > k:
                count[s[left]] -= 1
                left += 1
            else:
                result = max(right-left+1, result)
        return result