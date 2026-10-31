class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurrences = defaultdict(int)
        ret = []
        for num in nums:
            occurrences[num] = occurrences[num] + 1
        for i in range(0, k):
            max = 0
            maxKey = 0
            for j in occurrences:
                if occurrences[j] > max:
                    max = occurrences[j]
                    maxIndex = j
            occurrences.pop(maxIndex)
            ret.append(maxIndex)
            
        return ret