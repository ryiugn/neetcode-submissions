class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        leftmax = height[left]
        rightmax = height[right]
        result = 0
        while left < right:
            if leftmax < rightmax:
                left += 1
                water = min(leftmax, rightmax) - height[left]
                if water > 0:
                    result += water
                leftmax = max(leftmax, height[left])
            else:
                right -= 1
                water = min(leftmax, rightmax) - height[right]
                if water > 0:
                    result += water
                rightmax = max(rightmax, height[right])
        return result