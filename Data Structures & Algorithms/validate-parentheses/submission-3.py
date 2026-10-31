class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        vals = {')': '(', '}': '{', ']': '['}
        for chr in s:
            if chr in vals.values():
                stack.append(chr)
            else: 
                if not stack:
                    return False
                else:
                    if vals.get(chr) != stack.pop():
                        return False


        return not stack
