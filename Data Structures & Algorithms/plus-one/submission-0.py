class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""
        for dig in digits:
            num += str(dig)
        
        num = str(int(num) + 1)

        ret = []

        for digit in num:
            ret.append(int(digit))


        return ret