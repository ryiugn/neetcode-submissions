class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for n in range(len(nums)):
            if n > 0 and nums[n] == nums[n-1]:
                continue
            start = n+1
            end = len(nums)-1
            while start < end:
                if nums[start] + nums[end] > -nums[n]:
                    end -= 1
                elif nums[start] + nums[end] < -nums[n]:
                    start += 1
                else:
                    result.append([nums[n], nums[start], nums[end]])
                    start += 1
                    while start < end and start > 0 and nums[start] == nums[start-1]:
                        start += 1
                    while start < end and end < len(nums)-1 and nums[end] == nums[end+1]:
                        end -= 1
        return result
