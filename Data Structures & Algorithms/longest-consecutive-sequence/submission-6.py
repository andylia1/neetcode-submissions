class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        print(nums)
        counter = 1
        max = 1
        for i in range(len(nums) - 1):
            curr = nums[i]
            if curr + 1 == nums[i + 1]:
                counter += 1
            elif curr == nums[i + 1]:
                pass
            else:
                if counter > max:
                    max = counter
                counter = 1
        if counter > max:
            max = counter
        
        return max