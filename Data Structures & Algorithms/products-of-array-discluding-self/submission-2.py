class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = [1] * len(nums)
        acc = 1


        #prefix
        for i in range(1, len(nums)):
            ret[i] = nums[i - 1] * ret[i - 1]

        #postfix
        for j in range(len(nums) - 2, -1, -1):
            acc *= nums[j + 1]
            ret[j] *= acc
            
        return ret