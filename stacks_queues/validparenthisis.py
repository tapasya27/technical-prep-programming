#Question

"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order."""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for i in s:
            if i in mapping and len(stack) != 0:
                top_element = stack.pop()
                if top_element != mapping[i]:
                    return False
            else:
                stack.append(i)

        if len(stack) == 0:
            return True
