class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] #height and startIndex

        for i, height in enumerate(heights):
            start = i
            while stack and height <= stack[-1][0]:
                h, ind = stack.pop()
                maxArea = max(maxArea, (i - ind) * h)
                start = ind
            stack.append([height, start])

        for i in range(len(stack) - 1, -1, -1):
            h, ind = stack.pop()
            maxArea = max(maxArea, (len(heights) - ind) * h)


        return maxArea
        