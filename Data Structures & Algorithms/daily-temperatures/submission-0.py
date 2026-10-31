class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # [temp, currIndex]
        ret = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                _, currIndex = stack.pop()
                ret[currIndex] = i - currIndex
                
            stack.append([temp, i])

        return ret