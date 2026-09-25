class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newList = set(nums)
        
        return len(newList) != len(nums)