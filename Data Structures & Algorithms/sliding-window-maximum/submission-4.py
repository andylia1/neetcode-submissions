class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ret = []
        deque = collections.deque() #Stores indices
        maxVal = 0

        for i in range(k):
            while deque and nums[i] > nums[deque[-1]]:
                deque.pop()
            deque.append(i)
        
        ret.append(nums[deque[0]])
        
        left = 1

        for right in range(k ,len(nums)):
            if deque[0] < left:
                deque.popleft()
            left += 1

            while deque and nums[right] > nums[deque[-1]]:
                deque.pop()
            deque.append(right)
            ret.append(nums[deque[0]])
        
        return ret

            
