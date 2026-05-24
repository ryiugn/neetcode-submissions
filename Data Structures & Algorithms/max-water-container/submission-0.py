class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        left = 0
        right = len(heights)-1
        while right > left:
            area = (right-left)*min(heights[left], heights[right])
            if area > result:
                result = area  
            if heights[left] > heights[right]:
                right -= 1
            elif heights[right] > heights[left]:
                left += 1
            else:
                left += 1
        return result