class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def speed_finder(rate):
            time = 0
            for num in piles:
                time += math.ceil(num / rate)
            return time

        plates = len(piles)
        minSpeed = max(piles)

        left = 1
        right = minSpeed

        while left <= right:
            middle = (left+right) // 2
            middle_time = speed_finder(middle)

            if middle_time > h:
                left = middle + 1
            elif middle_time <= h:
                minSpeed = min(minSpeed, middle)
                right = middle - 1
        
        return minSpeed