#two approach - stack and two pointers

#Question -
"""Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty."""


def backspaceCompare(self, S: str, T: str) -> bool:
    return self.build(S) == self.build(T)


def build(self, string):
    empty_stack = []
    for i in string:
        if i != "#":
            empty_stack.append(i)
        else:
            empty_stack.pop()

    return "".join(empty_stack)


#two pointer approach
