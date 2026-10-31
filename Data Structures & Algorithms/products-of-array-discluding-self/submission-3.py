class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = [1] * len(nums)

        #prefix
        for i in range(1, len(nums)):
            ret[i] = nums[i-1] * ret[i-1]

        #postfix
        postfix = 1
        for i in range(len(nums) - 1, 0, -1):
            postfix *= nums[i]
            ret[i - 1] *= postfix

        return ret