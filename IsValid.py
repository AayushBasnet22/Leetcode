class Solution:
     def isValid(self, s: str) -> bool:
        stack = []
        top = -1
        for char in s:
            if top >= 0 and ((char == ')' and stack[top] == '(') or (char == '}' and stack[top] == '{') or (char == ']' and stack[top] == '[')):
                stack.pop()
                top -= 1
            else:
                stack.append(char)
                top += 1
        return True if top == -1 else False