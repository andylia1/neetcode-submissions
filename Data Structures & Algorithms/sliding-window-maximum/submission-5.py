class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        ret = []
        deque = collections.deque()

        for i in range(k):
            while deque and nums[i] > nums[deque[-1]]:
                deque.pop()
            deque.append(i)

        ret.append(nums[deque[0]])

        for right in range(k, len(nums)):
            left += 1
            if left > deque[0]:
                deque.popleft()

            while deque and nums[right] > nums[deque[-1]]:
                deque.pop()

            deque.append(right)
            ret.append(nums[deque[0]])



        return ret


            
