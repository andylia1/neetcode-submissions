class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            
            if nums[middle] == target:
                return middle


            #Check if  I'm at left part
            if nums[middle] > nums[right]:
                #to move right pointer 
                if target > nums[middle] or target < nums[left]:
                    left += 1
                else:
                    right -= 1
            else:
                if target < nums[middle] or target > nums[right]:
                    right -= 1
                else:
                    left += 1

        



        return -1