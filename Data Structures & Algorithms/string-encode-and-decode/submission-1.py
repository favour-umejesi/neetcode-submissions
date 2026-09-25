class Solution:
    def encode(self, strs: List[str]) -> str:
        """
        P - convert the list to a string
          - To ensure we can decode it later on, and get each word,
          add length of string and #.
        """
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word
        print(res)
        return res
        

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res


            

