"""
Problem: Given an integer array nums, return true if any value 
appears more than once in the array, otherwise return false
Difficulty: Easy 
"""

from typing import List

class Solution:
	"""
	Solution: Sort array and check each element to its next element; if match return True else False
	Space Complexity: O(1); no new object created
	Time Complexity:  O(n log n); sorting increases the time complexity
	"""
	def hasDuplicate(self, nums: List[int]) -> bool:
		if len(nums) == 0:
			print("empty array")
			return False
		nums.sort()
		for i in range(len(nums)-1):
			if nums[i] == nums[i+1]:
				return True
		return False

solution = Solution()
result = solution.hasDuplicate([4,7,2]) # returns False
print(result)

"""
Optimized solutions:
	def hasDuplicate(self, nums: List[int]) -> bool:
		seen = set()
		for i in nums:
			if i in seen:
				return True
			seen.add(i)
		return False

	def hasDuplicate(self, nums: List[int]) -> bool:
		return len(set(nums)) < len(nums)
"""