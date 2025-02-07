class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {'(': ')', '{': '}', '[': ']'}
        stack = []

        for char in s:
            if char in mapping:  # If it's an opening parenthesis
                stack.append(char)
            elif char in mapping.values():  # If it's a closing parenthesis
                if not stack or mapping[stack.pop()] != char:  # Check if it matches the top of the stack
                    return False

        return not stack 


        