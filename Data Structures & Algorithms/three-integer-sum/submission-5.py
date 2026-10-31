class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ret = []
        print(nums)
        for i, num in enumerate(nums):
            left = i + 1
            right = len(nums) - 1
            if i > 0 and num == nums[i - 1]:
                continue
            while left < right:
                # target = -num
                if -num > nums[left] + nums[right]:
                    left += 1
                elif -num < nums[left] + nums[right]:
                    right -= 1
                else:
                    ret.append([num, nums[left], nums[right]])
                    while right > 0 and nums[right] == nums[right - 1]:
                        right -= 1
                    right -= 1

        return ret