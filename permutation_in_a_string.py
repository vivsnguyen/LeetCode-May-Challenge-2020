"""
Given two strings s1 and s2, write a function to return true 
if s2 contains the permutation of s1. In other words, one of 
the first string's permutations is the substring of the second 
string.

 

Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False
 

Note:

The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].

   Hide Hint #1  
Obviously, brute force will result in TLE. Think of something else.
   
   Hide Hint #2  
How will you check whether one string is a permutation of another string?
   
   Hide Hint #3  
One way is to sort the string and then compare. But, Is there a better way?
   
   Hide Hint #4  
If one string is a permutation of another string then they must one common metric. What is that?
   
   Hide Hint #5  
Both strings must have same character frequencies, if one is permutation of another. Which data structure should be used to store frequencies?
   
   Hide Hint #6  
What about hash table? An array of size 26?
"""

#time limit exceeded
#can use Counter object
# class Solution(object):
#     def checkInclusion(self, s1, s2):
#         """
#         :type s1: str
#         :type s2: str
#         :rtype: bool
#         """
        
#         """
#         if len s2 < len s1 
#         loop through string 1,2 and count each letter
        
#         """
        
#         s1_dict = {}
        
#         for char in s1:
#             s1_dict[char] = s1_dict.get(char, 0) + 1
            
#         for i in range(len(s2)):
#             substring = s2[i:i+len(s1)]
            
#             s2_dict = {}
            
#             for char in substring:
#                 s2_dict[char] = s2_dict.get(char, 0) + 1
        
#             if s1_dict == s2_dict:
#                 return True
            
#         return False


#sliding window
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
        from collections import Counter
        
        s1_dict = Counter(s1)
        k = len(s1)
        window = s2[:k]
        s2_dict = Counter(window)

        if s1_dict == s2_dict:
            return True
  
        for i in range(len(s2)-len(s1)):
        
            if s2_dict.get(s2[i]) == 1:
                del s2_dict[s2[i]]
            elif s2_dict.get(s2[i]) > 1:
                s2_dict[s2[i]] -= 1
            
            if s2[i+k] in s2_dict:
                s2_dict[s2[i+k]] += 1
            else:
                s2_dict[s2[i+k]] = 1
                
            if s1_dict == s2_dict:
                return True
                
        return False