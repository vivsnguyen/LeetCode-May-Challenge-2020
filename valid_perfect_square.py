"""
Given a positive integer num, write a function which returns 
True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false
"""

#initial solution O(sqrt(N))
class Solution:
    def isPerfectSquareInitial(self, num: int) -> bool:
        i = 1
        
        while i*i < num:
            i += 1
            
        return i*i == num


#binary search
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low = 1
        high = num
        
        while low <= high:
            mid = (low+high)//2
            
            if mid**2 == num:
                return True
            
            elif mid**2 > num:
                high = mid-1
                
            else:
                low = mid+1
                
        return False