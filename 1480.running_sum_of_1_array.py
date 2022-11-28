from typing import List

"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]
"""

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        """
        Input: nums = [1,2,3,4]
        Output: [1,3,6,10]
        Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

        We might have as the first instance to want to compute a new list, and for a certain idx position, make the sum of all the values until idx-1 of the initial list.

        But if we observe this, we can see that 1 + 2 + 3 = 1 + 2 + the actual value.
        And 1 + 2 = 1 + actual value.
        So instead of computing all the values for each new position, we could simply be adding to the before value the actual one.
        """
        
        if len(nums) <= 1:
            return nums

        for idx in range(1, len(nums)):
            nums[idx] += nums[idx-1]
        
        return nums