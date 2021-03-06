"""
Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

Example 1:
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output: 
"apple"
Example 2:
Input:
s = "abpcplea", d = ["a","b","c"]

Output: 
"a"
Note:
All the strings in the input will only contain lower-case letters.
The size of the dictionary won't exceed 1,000.
The length of all the strings in the input won't exceed 1,000.
"""

def isValid(s, t):
    i = j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]: j += 1
        i += 1
    return j == len(t)
    
class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        longest = ""
        for t in d:
            if len(longest) > len(t) or (len(longest) == len(t) and longest < t): continue
            if isValid(s, t): longest = t
        return longest
    