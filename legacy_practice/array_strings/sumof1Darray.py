#returning the sum of a 1D array

#Example - Input  - [1,1,4]
#Output - [1,2,6] (1,1+1, 1+1+4)

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        count = 0
        for i in range(len(nums)):
            count += nums[i]
            nums[i] = count

        return nums