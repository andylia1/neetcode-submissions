class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        right = 0
        left = len(numbers) - 1

        while right < left:
            sum = numbers[right] + numbers[left]
            if sum == target:
                return [right + 1, left + 1]
            elif sum > target:
                left -= 1
            else:
                right += 1
        

        return []