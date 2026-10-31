class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # height, startIndex
        maxArea = 0

        for i, height in enumerate(heights):
            start = i
            while stack and height < stack[-1][0]:
                h, startIndex = stack.pop()
                maxArea = max(maxArea, (i - startIndex) * h)
                start = startIndex
            
            stack.append([height, start])

        for height in stack[::-1]:
              h, endIndex = stack.pop()

              maxArea = max(maxArea, (len(heights) - endIndex) * h)
        return maxArea