class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        maxVal = 1
        occurrences = set()
        for num in nums:
            occurrences.add(num)

        for num in occurrences:
            if num - 1 not in occurrences:
                i = 1
                curr = 1
                while num + i in occurrences:
                    curr += 1
                    i += 1
                maxVal = max(maxVal, curr)

        return maxVal
