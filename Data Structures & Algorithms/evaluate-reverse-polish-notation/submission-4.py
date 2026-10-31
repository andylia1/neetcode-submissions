class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "*", "-", "/"}
        for string in tokens:
            if string in operators:
                val2, val1 = int(stack.pop()), int(stack.pop())
                if string == "+":
                    stack.append(val1 + val2)
                elif string == "*":
                    stack.append(val1 * val2)
                elif string == "-":
                    stack.append(val1 - val2)
                elif string == "/":
                    stack.append(val1 / val2)
            else:
                stack.append(string)
        
        return int(stack[0])