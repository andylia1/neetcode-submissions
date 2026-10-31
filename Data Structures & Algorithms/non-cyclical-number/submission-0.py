class Solution:
    def isHappy(self, n: int) -> bool:
        hmp = defaultdict(int)

        num = str(n)

        sum = 0
        while sum != 1:
            sum = 0
            for digit in num:
                sum += int(digit) ** 2
            if sum in hmp:
                return False
            hmp[sum] += 1
            num = str(sum)
            
        

        return True
