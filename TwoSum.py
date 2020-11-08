#author - Tapasya Sharma
#Question - Given an array of integers nums and an integer target,
#return indices of the two numbers such that they add up to target.

#Input: nums = [2,7,11,15], target = 9
#Output: [0,1]
#Output: Because nums[0] + nums[1] == 9, we return [0, 1].


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_hold = {}
        for index,number in enumerate(nums):
            y = target - number
            if y in dict_hold:
                return index, dict_hold[y]
            else:
                dict_hold[number] = index