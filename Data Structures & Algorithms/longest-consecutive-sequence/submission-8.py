class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        uniques = set(nums)
        max = 1
        count = 1
        for i in range(len(nums)):
            if nums[i] - 1 not in uniques:
                j = 1
                while nums[i] + j in uniques:
                    count += 1
                    j += 1
            if max < count:
                max = count
            count = 1
            print(max)

        return max
