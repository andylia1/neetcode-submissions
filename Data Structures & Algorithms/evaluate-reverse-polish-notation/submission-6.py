class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for chr in tokens:
            if chr == '+':
                num2, num1 = int(stack.pop()), int(stack.pop())
                stack.append(num1 + num2)
            elif chr == '-':
                num2, num1 = int(stack.pop()), int(stack.pop())
                stack.append(num1 - num2)

            elif chr == '*':
                num2, num1 = int(stack.pop()), int(stack.pop())
                stack.append(num1 * num2)

            elif chr == '/':
                num2, num1 = int(stack.pop()), int(stack.pop())
                stack.append(num1 / num2)
            else:
                stack.append(chr)

        return int(stack[0])