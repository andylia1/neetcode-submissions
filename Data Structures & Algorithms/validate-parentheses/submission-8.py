class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valids = {')': '(', ']': '[', '}': '{'}

        for chr in s:
            if chr not in valids:
                stack.append(chr)
            else:
                if stack:
                    char = stack.pop()
                    if valids[chr] != char:
                        return False
                else:
                    stack.append(chr)
        
        return not stack