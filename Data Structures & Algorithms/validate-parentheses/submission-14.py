class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = {')': '(', '}': '{', ']': '['}


        for chr in s:
            if chr in valid:
                if stack and valid[chr] == stack.pop():
                    continue
                else:
                    return False
            else:
                stack.append(chr)

        
        return not stack