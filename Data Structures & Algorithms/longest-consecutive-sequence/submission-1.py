class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set()
        for num in nums:
            hashset.add(num)
        starters = []
        for num in hashset:
            if num-1 not in hashset:
                starters.append(num)
        longest = 0
        for num in starters:
            check = True
            counter = 1
            temp = num
            while check:
                if num+1 in hashset:
                    counter += 1
                    num += 1
                else:
                    longest = max(longest, counter)
                    check = False
        return longest


            
