from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        newS = Counter(s)
        newT = Counter(t)

        return newS == newT
        