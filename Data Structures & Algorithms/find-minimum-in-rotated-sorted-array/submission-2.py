class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        if nums[l] < nums[r]:
            return nums[l]


        min_val = nums[r]

        while l <= r:
            m = (l + r) // 2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                min_val = min(min_val, nums[m])
                r = m - 1



        return min_val