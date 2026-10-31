class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return False
        chars = {')': '(', '}': '{', ']': '['}
        stack = []
        print(len(s))
        for chr in s:
            if chr not in chars:
                stack.append(chr)
            else:
                if not stack:
                    return False
                if chars[chr] != stack.pop():
                    return False


        return not stack