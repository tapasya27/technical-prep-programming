"""
Problem: Given an array nums, find the k number of most frequently occuring elements in the array
Difficulty: Medium
Optimized result is a heap sort or bucket sort
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        My Solution: Create a hashmap that contains all frequencies of the occuring nums. Sort the dict by value, turn to a list and then slice to get k values
        Space Complexity: O(n + k)
        Time Complexity: O(n) + O(n log n)
        """

        if len(nums) == 0:
            return []

        result = []
        counts = {}

        for index, value in enumerate(nums):
            if value in counts:
                counts[value] +=1
            else:
                counts[value] = 1

        
        result = list(dict(sorted(counts.items(), key=lambda item: item[1])))[-k:]
        return result