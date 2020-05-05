"""
Given a string, find the first non-repeating character 
in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase 
letters.
"""

# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         char_dict = {}
        
#         for char in s:
#             char_dict[char] = char_dict.get(char, 0) + 1
            
#         for char, count in char_dict.items():
#             if count == 1:
#                 return s.index(char)
            
#         return -1


class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_dict = {}
        
        for char in s:
            char_dict[char] = char_dict.get(char, 0) + 1
            
        for i, char in enumerate(s):
            if char_dict.get(char) == 1:
                return i
            
        return -1