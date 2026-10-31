class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '/', '-', '*'}
        stack = []
        for i in range(len(tokens)):
            if tokens[i] not in operators:
                stack.append(tokens[i])
            else:
                second_num = int(stack.pop())
                first_num = int(stack.pop())
                if tokens[i] == '+':
                    stack.append(first_num + second_num)
                elif tokens[i] == '/':
                    stack.append(first_num / second_num)
                elif tokens[i] == '-':
                    stack.append(first_num - second_num)
                else:
                    stack.append(first_num * second_num)
        return int(stack[0])