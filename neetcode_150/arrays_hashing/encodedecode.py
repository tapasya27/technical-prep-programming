"""
Problem: Create an algorithm to encode decode a string
Difficulty: Medium
"""

from typing import List

class Solution:
    """
	Solution: My solution was creating a delimiter and using ord/chr for some sort of encoding. Ideal solution is appending the count of number in front
    of the list to avoid using a delimiter. 
	Space Complexity: O(n) for both functions
	Time Complexity: O(n^2) + O(n^2)
	"""
    def encode(self, strs: List[str]) -> str:
        word = 0
        encode = ""
        for index, value in enumerate(strs):
            for sub_index, sub_value in enumerate(value):
                word += ord(sub_value) + 6848
                word = str(word) + "%"
                encode += word
                word = 0
            encode+= "^"
            word = 0 
        return encode 


    def decode(self, s: str) -> List[str]:
        decode = []
        letter = ""
        word = ""
        for character in s:
            if character == "^":
                decode.append(word)
                word = ""
            elif character == "%":
                letter = int(letter) - 6848
                word += chr(letter)
                letter = ""
            else:
                letter += character

        return decode
    

    def encode_optimal(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
    
    def decode_optimal(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
            
        return res


solution = Solution()
result = solution.encode(["act","pots","tops","cat","stop","hat"])
result_decoded = solution.decode(["act","pots","tops","cat","stop","hat"])
print(result)   

