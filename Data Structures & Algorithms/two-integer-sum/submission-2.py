class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos = {}
        ret = []

        for i in range(len(nums)):
            if nums[i] in pos:
                return [pos[nums[i]], i]
            else:
                pos[target - nums[i]] = i

        return []