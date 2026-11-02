class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def computeTime(rate):
            res = 0
            for pile in piles:
                res += math.ceil(pile / rate)
            return res


        right = max(piles)
        left = 1
        res = right

        while left <= right:
            middle = (left + right) // 2
            middle_time = computeTime(middle)

            if middle_time > h:
                left = middle + 1
            else:
                right = middle - 1
                res = min(middle, res)

        return res

