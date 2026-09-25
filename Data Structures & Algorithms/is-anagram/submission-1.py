"""
Create a dictionary for each string, to store their frequencies
if the dictionaries are equal, return True else False
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        seenA = {}
        seenB = {}

        for num in s:
            seenA[num] = 1 + seenA.get(num, 0)

        for letter in t:
            seenB[letter] = 1 + seenB.get(letter, 0)

        
        return seenA == seenB


        