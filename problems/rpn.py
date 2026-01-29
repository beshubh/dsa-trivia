
OPERATORS = ['+', '-', '*', '/']


class Solution:

    def helper(self, left: int, right: int, op: str):
        match op:
            case '-':
                return left - right
            case '+':
                return left + right
            case '*':
                return left * right
            case '/':
                return int(left / right)

    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        res = None
        if len(tokens) == 1:
            return int(tokens[0])
        for token in tokens:
            if token in OPERATORS:
                right = stack.pop()
                left = stack.pop()
                res = self.helper(int(left), int(right), token)
                stack.append(res)
            else:
                stack.append(token)
        return stack[-1]
