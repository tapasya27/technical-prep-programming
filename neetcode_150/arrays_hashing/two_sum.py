"""
Problem:
Difficulty: Easy 
"""

from typing import List
class Solution:
	"""
	Solution: 
	Space Complexity: O(n)
	Time Complexity: O(n)
	"""
	class Solution:
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