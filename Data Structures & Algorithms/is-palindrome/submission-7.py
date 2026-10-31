class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()
        left = 0
        right = len(s) - 1

        while left < right:
            while not self.isAlphaNum(s[left]) and left < len(s) - 1:
                left += 1
            while not self.isAlphaNum(s[right]) and right >= 0:
                right -= 1
            if s[left] != s[right]:
                return False
            else:
                left += 1
                right -= 1
        return True



    def isAlphaNum(self, chr):
        print(chr)
        if ((ord('a') <= ord(chr) and ord(chr) <= ord('z')) 
            or (ord('0') <= ord(chr) and ord(chr) <= ord('9'))):
            return True
        return False