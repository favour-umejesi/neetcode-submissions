"""
U - Check if any value in the list appears more than once in the list, 
    if so return True, else False
M - Array, HashMap
P - Create a HashMap to store freqeuncy of each company
  - Check if the value of any key is greater than 1, return True else false
"""
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        seen = {}

        for num in nums:
            seen[num] = 1 + seen.get(num, 0)

        for k, v in seen.items():
            if v > 1:
                return True
        return False


        