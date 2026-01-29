OPENING_BRACKETS = ['(', '{', '[']
CLOSING_BRACKETS = [')', '}', ']']

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i, ch in enumerate(s):
            if ch in OPENING_BRACKETS:
                stack.append(ch)
            else:
                match ch:
                    case ']' if stack and stack[-1] == '[':
                        stack.pop()
                    case '}' if stack and stack[-1] == '{':
                        stack.pop()
                    case ')' if stack and stack[-1] == '(':
                        stack.pop()
                    case _:
                        return False

        return len(stack) == 0
