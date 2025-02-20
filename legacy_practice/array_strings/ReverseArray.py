import re
def backspaceCompare(S: str, T: str) -> bool:
    pattern = re.compile(r'.#')
    a = re.sub(pattern,"",S)
    b = re.sub(pattern,"",T)
    print(a==b)

backspaceCompare("ab#c","ad#c")