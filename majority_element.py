"""
Given an array of size n, find the majority element. 
The majority element is the element that appears more 
than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority 
element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ele_dict = {}
        
        for num in nums:
            ele_dict[num] = ele_dict.get(num, 0) + 1
            
        maj = max(ele_dict.values())
        
        for num in nums:
            if ele_dict.get(num) == maj:
                return num


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n_dict = {}
        k = len(nums)
        
        for i in nums:
            n_dict[i] = n_dict.get(i,0) + 1
            
        for key, value in n_dict.items():
            if value > k/2:
                return key