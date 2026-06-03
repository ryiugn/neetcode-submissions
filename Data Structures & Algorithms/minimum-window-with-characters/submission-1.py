class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        countT, window = {}, {}
        have = 0
        for ch in t:
            countT[ch] = countT.get(ch, 0) + 1
        need = len(countT)
        left = 0
        result = [0, 0]
        reslen = float("infinity")
        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1
            if s[right] in countT and window[s[right]] == countT[s[right]]:
                have += 1
            while have == need:
                if right - left + 1 < reslen:
                    result = [left, right]
                    reslen = right - left + 1
                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                left += 1
        l, r = result
        return s[l:r+1] if reslen < float("infinity") else ""