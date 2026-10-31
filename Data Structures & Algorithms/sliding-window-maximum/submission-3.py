class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ret = []
        deque = collections.deque()
        left = 1

        for right in range(k):
            while deque and nums[right] > nums[deque[-1]]:
                deque.pop()
            deque.append(right)
        ret.append(nums[deque[0]])

        for right in range(k, len(nums)):
            if left > deque[0] :
                deque.popleft()

            while deque and nums[right] > nums[deque[-1]]:
                deque.pop()
            deque.append(right)
            ret.append(nums[deque[0]])
            left += 1

        return ret