class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = defaultdict(int)
        stack = []

        for i in range(len(position)):
            cars[position[i]] = speed[i]
        sorted_cars = sorted(cars)[::-1]

        for i, pos in enumerate(sorted_cars):
            if stack and (target - pos) / cars[pos] <= (target - stack[-1]) / cars[stack[-1]]:
                pass
            else:
                stack.append(pos)

        return len(stack)

