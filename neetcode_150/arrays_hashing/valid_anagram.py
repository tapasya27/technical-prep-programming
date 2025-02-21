"""
Problem: Given two strings s and t, return true 
if the two strings are anagrams of each other, otherwise return false.
Difficulty: Easy 
"""

from typing import List
class Solution:
	"""
	Solution: Create two dictionaries to tackle frequency of each word
	and compare the dictionary
	Space Complexity: O(1); O(c) is apprx O(1) if limited character sets 
	are used
	Time Complexity: O(n+m); O(n) for first for loop and O(m) for second for loop 
	= O(n+m)
	"""
	def isAnagram(self, s: str, t: str) -> bool:
		#Initial check: Unequal lengths
		if len(s) != len(t):
			return False
		dict1 = {}
		dict2 = {}
		for i in range(len(s)):
			if s[i] not in dict1:
				dict1[s[i]] = 0
			else:
				dict1[s[i]] += 1
		for i in range(len(t)):
			if t[i] not in dict2:
				dict2[t[i]] = 0
			else:
				dict2[t[i]] += 1

		if dict1 == dict2:
			return True
		else:
			return False

solution = Solution()
result = solution.isAnagram("jar","jam") # returns False
print(result)

"""
Cleaner solutions (same optimization):
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dict1, dict2 = {}, {}

        for i in range(len(s)):
            dict1[s[i]] = 1 + dict1.get(s[i], 0)
            dict2[t[i]] = 1 + dict2.get(t[i], 0)
        return dict1 == dict2
"""