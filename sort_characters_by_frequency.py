"""
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
"""
class Solution:
    def frequencySort(self, s: str) -> str:
        char_count = {}
        sorted_list = []
        
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
            
        
        for c in sorted(char_count, key=char_count.get, reverse=True):
            sorted_list.append(c*char_count[c])
            
        
        return "".join(sorted_list)