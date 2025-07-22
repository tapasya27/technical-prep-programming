"""
Problem:
Difficulty: Medium
"""

from collections import defaultdict
from typing import List
class Solution:
    """
	Solution: Uses a default dict to store lists and fix an edge case. Sorts the word and create a reverse dictionary
    where the word becomes the values and the count becomes the list key. But dictionary can't store a list as keys (not hashable) so we use tuple and append 
    to the default dict whenever we see an instance. This uses sorting so is the worse solution out of the two. 
	Space Complexity: O(n*k) per word per character
	Time Complexity: For looping through words - O(n), for sorting - O(k log k), creating a tuple: O(k), appending: O(1) = O (n* k log k)
	"""
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = defaultdict(list)

        for word in strs:
            # Use sorted characters as the key
            key = tuple(sorted(word))  # e.g., 'act' -> ('a', 'c', 't')
            grouped[key].append(word)

        return list(grouped.values())


    def groupAnagramsRecommendedSol(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())


solution = Solution()
result = solution.groupAnagrams(["act","pots","tops","cat","stop","hat"]) # returns [["act","cat"],["pots","tops","stop"],["hat"]]
print(result)   