class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ret = []
        happenings = defaultdict(int)

        for num in nums:
            happenings[num] += 1
        
        for i in range(k):
            maxVal = 0
            maxKey = 0
            for key in happenings:
                if happenings[key] > maxVal:
                    maxVal = happenings[key]
                    maxKey = key
            happenings.pop(maxKey)
            ret.append(maxKey)

        return ret