"""
438. Find All Anagrams in a String
(Medium complexity)

Given two strings s and p, return an array of all the start indices of p's anagrams in s. 
You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.
"""

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        len_s, len_p, hash_s, hash_p, result = len(s), len(p), 0, 0, []

        if len_s < len_p: return []
        for i in range(len_p): hash_s, hash_p = hash_s + hash(s[i-1]), hash_p + hash(p[i])

        for i in range(len_p-1, len_s):
            hash_s +=  hash(s[i]) - hash(s[i-len_p])
            if hash_s==hash_p: result.append(i-len_p+1)
        
        return result