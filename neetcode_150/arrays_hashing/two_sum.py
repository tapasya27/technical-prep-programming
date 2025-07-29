"""
Problem: Given a number and a target sum, find the other num in a given array
Difficulty: Easy 
"""

from typing import List

class Solution:
	"""
	Solution: Find the complement of the number that matches the target to find the actual value that matches the target
	Space Complexity: O(n)
	Time Complexity: O(n)
	"""
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		num_map = {}
		for i, num in enumerate(nums):
			complement = target - num
			if complement in num_map:
				return [num_map[complement], i]
			num_map[num] = i  # Store current number's index
		return [] 

solution = Solution()
result = solution.twosum([3,4,5,6],7) # returns [0,1]
print(result)