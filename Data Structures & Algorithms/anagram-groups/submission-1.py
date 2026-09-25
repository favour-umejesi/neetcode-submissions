"""
U - Given a list of words, group all anagrams together
M - Array, HashMap
P - Create an empty HashMap
  - Iterate through the list of words
  - create a key, which will be a sorted word
  - We check if the sorted word is in the dictionary
    - if so we append it to the value, which is a list of words
    - else we add the sorted word to a dictionary with a list as value
    - Return values of the dictionary, which contains list of sorted words
"""
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)

        for word in strs:
            sorted_word = "".join(sorted(word))

            anagram[sorted_word].append(word)

        return list(anagram.values())

        