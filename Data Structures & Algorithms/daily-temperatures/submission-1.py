class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] #temp, and index in temperatures
        ret = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                _, ind = stack.pop()
                ret[ind] = i - ind

            stack.append([temp, i])

        return ret
