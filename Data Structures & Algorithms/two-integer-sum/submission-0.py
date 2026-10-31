class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = {}
        for i in range(len(nums)):
            if target - nums[i] in indexes.keys():
                return [indexes[target - nums[i]], i]
            else:
                indexes[nums[i]] = i