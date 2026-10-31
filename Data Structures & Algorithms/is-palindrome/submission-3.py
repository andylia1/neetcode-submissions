class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        end = len(s) - 1

        while i < end:
            while i < end and not self.alphaNum(s[i]):
                i += 1
            while end > i and not self.alphaNum(s[end]):
                end -= 1
            if s[i].lower() != s[end].lower():
                return False
            end -= 1
            i += 1
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))