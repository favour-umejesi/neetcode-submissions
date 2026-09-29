from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        """
        create a hashmap
        sort each word, each sorted word will be a key, and the value will be a list of words that correlate
        check the list for words that correlate with sorted words
        if it matches, append word to list
        else add the key to the dictionary

        """
        dictionary = defaultdict(list)

        for word in strs:
            sorted_word = "".join(sorted(word))
            dictionary[sorted_word].append(word)

        return list(dictionary.values())



        