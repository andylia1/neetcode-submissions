class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        left = 0 
        right = len(s) - 1

        while left < right:
            while left < len(s) - 1 and not self.isAlphaNum(s[left]):
                left += 1
            while right >= 0 and not self.isAlphaNum(s[right]):
                right -= 1
                
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True




    def isAlphaNum(self, chr):
        if ((ord('z') >= ord(chr) and ord(chr) >= ord('a')) 
        or (ord('9') >= ord(chr) and ord(chr) >= ord('0'))):
            return True

        return False