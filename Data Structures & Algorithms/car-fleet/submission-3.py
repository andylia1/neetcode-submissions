class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = [] # store time it takes
        sortedpos = [] # list with [pos, speed]
        

        for i in range(len(position)):
            sortedpos.append([position[i], speed[i]])

        sortedpos = sorted(sortedpos)[::-1]

        for i in range(len(sortedpos)):
            if stack and stack[-1] >= (target - sortedpos[i][0]) / sortedpos[i][1]:
                continue
            else:
                stack.append((target - sortedpos[i][0]) / sortedpos[i][1])
        
        return len(stack)