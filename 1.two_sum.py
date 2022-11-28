from typing import List
"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        One simple solution would be to do two for loops, and compare the sum for both index values.
        But this would be an algorithm of O(n²), which is not the most efficient.

        One possible solution would be to store in a map the values that we already had seen.
        So when we compute the difference between a certain value and the target, we could check if we have this difference value in that map (so it is available).
        """

        diff_map = {}
        for idx in range(len(nums)):
            actual_diff = target-nums[idx]

            # We check if this value is already stored in the map
            if actual_diff in diff_map:
                return [diff_map[actual_diff], idx]
            
            diff_map[nums[idx]] = idx