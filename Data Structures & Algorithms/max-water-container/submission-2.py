class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxVol = 0

        while left < right:
            if heights[left] >= heights[right]:
                maxVol = max(maxVol, heights[right] * (right - left))
                right -= 1
            else: #heigh[left] < height[right]
                maxVol = max(maxVol, heights[left] * (right-left))
                left += 1


        
        return maxVol