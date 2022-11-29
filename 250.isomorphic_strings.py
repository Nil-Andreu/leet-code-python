"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        We need a data structure that maps effectively between the two words.
        So we will be storing this relationship, and if it holds for all the words length will be isomorphic.
        """

        # To maps to asses the relationship in O(1)
        mapping_s_t = {}
        mapping_t_s = {}

        # We iterate through all the characters (s & t have the same length)
        for idx in range(len(s)):
            char_s = s[idx]
            char_t = t[idx]

            # If we have a mapping and is not related to the actual char of t
            if mapped_s_t := mapping_s_t.get(char_s):
                if mapped_s_t is not char_t:
                    return False

            if mapped_t_s := mapping_t_s.get(char_t):
                if mapped_t_s is not char_s:
                    return False

            # We put which are the mappings
            mapping_s_t[char_s] = char_t
            mapping_t_s[char_t] = char_s

        # And we should have mappings that the set of keys are the same (unique & 1-to-1 relationship)
        return len(set(mapping_s_t.keys())) == len(set(mapping_t_s.keys()))
    
"""
There is also another solution, which is based on the idea of 1-to-1 and unique
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(s)) == len(set(zip(s, t))) == len(set(t))