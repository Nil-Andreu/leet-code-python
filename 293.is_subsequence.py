"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        The logic here is that we will have two pointers, for s and t.
        We are looking at the beginning at the first character of the s (pointer_s = 0, pointer_t = 0).
        If the first position of t is not the s[pointer_s], we will move to the next position of t.
        If the next one is s[pointer_s], we will increment both.

        This way, we are keeping track of the order in s that needs to be followed in t.
        And the algorithm is only O(n).
        
        """
        if not len(s):
            return True

        pointer_s, pointer_t = 0, 0

        while pointer_t < len(t):
            if t[pointer_t] == s[pointer_s]:
                pointer_s += 1
                
                if pointer_s == len(s):
                    return True

            pointer_t += 1