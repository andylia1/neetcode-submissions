class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def time_to_eat(rate):
            time = 0
            for pile in piles:
                time += math.ceil(pile / rate)
            return time

        l, r = 1, max(piles)
        min_rate = r
        while l <= r:
            m = (l + r) // 2
            m_time = time_to_eat(m)

            if m_time > h:
                l = m + 1
            else:
                min_rate = min(min_rate, m)
                r = m - 1

        return min_rate 


