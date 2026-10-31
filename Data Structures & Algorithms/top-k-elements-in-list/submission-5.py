class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurrences = {}
        ret = []
        for num in nums:
            occurrences[num] = occurrences.get(num, 0) + 1
        
        for i in range(k):
            max = 0
            maxIndex = 0
            for key in occurrences:
                if occurrences[key] > max:
                    max = occurrences[key]
                    maxIndex = key
            ret.append(maxIndex)
            occurrences.pop(maxIndex)
        
        return ret