class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            length = len(word)
            block = str(length) + "#" + word
            result += block
        return result
    def decode(self, s: str) -> List[str]:
        result = []
        count = 0
        while count < len(s):
            start = count
            while s[count] != "#":
                count += 1
            num = int(s[start:count])
            block = s[count+1:count+1+num]
            result.append(block)
            count += num + 1


        return result