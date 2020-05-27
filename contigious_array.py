"""
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.
"""

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sums_dict = {}
        sum_num = 0
        length = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                sum_num += 1
            else:
                sum_num -= 1

            if sum_num == 0: #if all sum to 0, equal amount of 0's and 1's
                length = i + 1

            if sum_num in sums_dict:
                length = max(length, i - sums_dict[sum_num])

            else:
                sums_dict[sum_num] = i

        return length