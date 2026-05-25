class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        left = 0
        hashset = set()
        for right in range(len(s)):
            while s[right] in hashset:      # shrink window until duplicate gone
                hashset.remove(s[left])
                left += 1
            hashset.add(s[right])           # add new character
            result = max(result, right - left + 1)  # update result
        return result