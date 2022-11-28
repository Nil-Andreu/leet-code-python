from typing import List

"""
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11
Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
Example 3:

Input: nums = [2,1,-1]
Output: 0
Explanation:
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0
"""

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        """
        An easy solution would be to make for all the idx possible, sum(nums[:index]) == sum(nums[index+1:]).
        But this would be a very inefficient solution, as we would be doing a loop for trying all the possible idx, and then sum() which is also O(n).
        So would end up with O(n²), but no allocation of memory so O(1).

        But then, you might hink if it is necessary to be computing the sum of the lists all the time.
        When you move one position in the idx to the left, the left array now has the idx-1 value, and the right no longer has the idx value:
            [1, 2, 3, 4, 5]
            idx = 0: 0, 15
            idx = 1: value[idx-1] = 1, 15 - value[idx] = 14 
            idx = 2: 1 + value[idx-1] = 3, 14 - value[idx] = 9
        So this is what we could implement, thus having a O(n) on the running time, and O(1) on memory allocation.

        """
        if len(nums) == 1:
            return 0

        left_sum, right_sum = 0, sum(nums[1:])
        if left_sum == right_sum:
            return 0

        for idx in range(1, len(nums)):
            left_sum += nums[idx-1]
            right_sum -= nums[idx]

            if left_sum == right_sum:
                return idx

        return -1