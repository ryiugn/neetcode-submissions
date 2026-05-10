class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for n in range(len(nums)):
            i = n-1
            j = n+1
            pre = 1
            suf = 1
            while i >= 0:
                pre *= nums[i]
                i -= 1
            while j < len(nums):
                suf *= nums[j]
                j += 1
            result.append(pre*suf)
        return result